from http.server import HTTPServer, BaseHTTPRequestHandler
import json
class abchandler(BaseHTTPRequestHandler):

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length)    # data sent by client
        
        try: 
            data = json.loads(body)
            response = {
                "message": "hello " + data["servername"]
            }
            status = 200

        except Exception:
            response = "Invalid json"
            status = 400

        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        self.wfile.write(json.dumps(response).encode())

server=HTTPServer(("localhost",8081),abchandler)

print("Server Running on http://localhost:8081")

server.serve_forever()
