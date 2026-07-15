"""
Part 5 Challenge: Network API

A REST API built with http.server (BaseHTTPRequestHandler) that exposes
networking data gathered via psutil (interfaces, MAC addresses, routes).
All data lives in a single in-memory dictionary — nothing touches disk,
and nothing changes the real network configuration of the machine.

Endpoints
---------
GET    /interfaces        -> list all interfaces (with addresses/stats)
GET    /macs               -> list all MAC addresses, keyed by interface
GET    /routes              -> list all routes (simulated, in-memory)
POST   /routes              -> add a route                {destination, gateway, interface}
GET    /routes/<id>        -> get a single route
PUT    /routes/<id>        -> update a route (partial or full body)
DELETE /routes/<id>        -> delete a route

Run:
    python3 network_api.py [port]      # default port 9000

Try it:
    curl http://localhost:9000/interfaces
    curl http://localhost:9000/macs
    curl http://localhost:9000/routes
    curl -X POST http://localhost:9000/routes \
         -H "Content-Type: application/json" \
         -d '{"destination": "10.0.0.0/24", "gateway": "10.0.0.1", "interface": "eth0"}'
    curl -X PUT http://localhost:9000/routes/1 \
         -H "Content-Type: application/json" \
         -d '{"gateway": "10.0.0.254"}'
    curl -X DELETE http://localhost:9000/routes/1
"""

import json
import re
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

import psutil


# ---------------------------------------------------------------------------
# In-memory data store
# ---------------------------------------------------------------------------
# Everything the API serves/mutates lives in this single dictionary.
# It is (re)built from psutil at startup, and only the "routes" section
# is ever mutated afterwards (interfaces/macs are treated as read-only
# snapshots of the real system).

DB = {
    "interfaces": {},   # name -> {addresses: [...], is_up, speed, mtu}
    "macs": {},          # name -> mac address string
    "routes": {},         # id (str) -> {destination, gateway, interface}
    "_next_route_id": 1,
}


def load_network_data():
    """Populate DB['interfaces'] and DB['macs'] from psutil. Called once
    at startup so the API has real data to serve; requests never re-query
    psutil, they just read/write the in-memory dict."""

    addrs = psutil.net_if_addrs()
    stats = psutil.net_if_stats()

    for name, addr_list in addrs.items():
        interface_entry = {"addresses": [], "is_up": None, "speed": None, "mtu": None}
        mac = None

        for a in addr_list:
            family_name = a.family.name if hasattr(a.family, "name") else str(a.family)
            interface_entry["addresses"].append(
                {
                    "family": family_name,
                    "address": a.address,
                    "netmask": a.netmask,
                    "broadcast": a.broadcast,
                }
            )
            # AF_LINK / AF_PACKET is the hardware (MAC) address family
            if family_name in ("AF_LINK", "AF_PACKET") and a.address:
                mac = a.address

        if name in stats:
            s = stats[name]
            interface_entry["is_up"] = s.isup
            interface_entry["speed"] = s.speed
            interface_entry["mtu"] = s.mtu

        DB["interfaces"][name] = interface_entry
        if mac:
            DB["macs"][name] = mac

    # Simulate a couple of starter routes (psutil has no native routing
    # table API), so /routes has something to GET before any POSTs.
    starter_routes = [
        {"destination": "0.0.0.0/0", "gateway": "192.168.1.1", "interface": next(iter(DB["interfaces"]), "eth0")},
        {"destination": "192.168.1.0/24", "gateway": "0.0.0.0", "interface": next(iter(DB["interfaces"]), "eth0")},
    ]
    for route in starter_routes:
        add_route(route)


def add_route(route):
    route_id = str(DB["_next_route_id"])
    DB["_next_route_id"] += 1
    DB["routes"][route_id] = {"id": route_id, **route}
    return DB["routes"][route_id]


# ---------------------------------------------------------------------------
# HTTP handler
# ---------------------------------------------------------------------------

ROUTES_ITEM_RE = re.compile(r"^/routes/([^/]+)/?$")


class NetworkAPIHandler(BaseHTTPRequestHandler):

    # ---- helpers ----------------------------------------------------

    def _send_json(self, status, payload):
        body = json.dumps(payload, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _read_json_body(self):
        length = int(self.headers.get("Content-Length", 0))
        if length == 0:
            return {}
        raw = self.rfile.read(length)
        try:
            return json.loads(raw.decode("utf-8"))
        except json.JSONDecodeError:
            return None  # signals bad JSON to the caller

    def _error(self, status, message):
        self._send_json(status, {"error": message})

    # ---- routing ------------------------------------------------------

    def do_GET(self):
        path = self.path.rstrip("/") or "/"

        if path == "/interfaces":
            self._send_json(200, DB["interfaces"])
        elif path == "/macs":
            self._send_json(200, DB["macs"])
        elif path == "/routes":
            self._send_json(200, list(DB["routes"].values()))
        elif ROUTES_ITEM_RE.match(path):
            route_id = ROUTES_ITEM_RE.match(path).group(1)
            route = DB["routes"].get(route_id)
            if route is None:
                self._error(404, f"No route with id '{route_id}'")
            else:
                self._send_json(200, route)
        else:
            self._error(404, f"Unknown endpoint: GET {self.path}")

    def do_POST(self):
        path = self.path.rstrip("/") or "/"

        if path != "/routes":
            self._error(404, f"Unknown endpoint: POST {self.path}")
            return

        body = self._read_json_body()
        if body is None:
            self._error(400, "Malformed JSON body")
            return

        required = {"destination", "gateway", "interface"}
        missing = required - body.keys()
        if missing:
            self._error(400, f"Missing fields: {sorted(missing)}")
            return

        route = add_route(
            {
                "destination": body["destination"],
                "gateway": body["gateway"],
                "interface": body["interface"],
            }
        )
        self._send_json(201, route)

    def do_PUT(self):
        path = self.path.rstrip("/") or "/"
        match = ROUTES_ITEM_RE.match(path)

        if not match:
            self._error(404, f"Unknown endpoint: PUT {self.path}")
            return

        route_id = match.group(1)
        if route_id not in DB["routes"]:
            self._error(404, f"No route with id '{route_id}'")
            return

        body = self._read_json_body()
        if body is None:
            self._error(400, "Malformed JSON body")
            return

        # Partial update: only overwrite fields the caller supplied.
        allowed_fields = {"destination", "gateway", "interface"}
        updates = {k: v for k, v in body.items() if k in allowed_fields}
        DB["routes"][route_id].update(updates)

        self._send_json(200, DB["routes"][route_id])

    def do_DELETE(self):
        path = self.path.rstrip("/") or "/"
        match = ROUTES_ITEM_RE.match(path)

        if not match:
            self._error(404, f"Unknown endpoint: DELETE {self.path}")
            return

        route_id = match.group(1)
        if route_id not in DB["routes"]:
            self._error(404, f"No route with id '{route_id}'")
            return

        deleted = DB["routes"].pop(route_id)
        self._send_json(200, {"deleted": deleted})

    # Quieter default logging (still shows method/path/status).
    def log_message(self, fmt, *args):
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9000

    load_network_data()

    server = HTTPServer(("0.0.0.0", port), NetworkAPIHandler)
    print(f"Network API running on http://0.0.0.0:{port}")
    print(f"Loaded {len(DB['interfaces'])} interfaces, {len(DB['routes'])} starter routes.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down.")
        server.server_close()


if __name__ == "__main__":
    main()
