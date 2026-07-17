from flask import Flask, request, jsonify

app = Flask(__name__)

def get_api_key():
    key = request.headers.get("X-API-Key")
    if not key:
        return None
    return key

@app.route("/data")
def data():
    api_key = get_api_key()

    # replace code below with real API key validation
    if not api_key:
        return jsonify({"error": "missing_api_key"}), 401

    #Choose one strategy for the lab demo
    allowed, retry = sliding_window_check(api_key)
    #allowed, retry = buckets[api_key].consume()

    if not allowed:
        resp = jsonify({"error": "rate_limited", "retry_after": retry})
        resp.status_code = 429
        resp.headers["Retry-After"] = str(retry)
        return resp

    return jsonify({"data": "ok"})

if __name__ == "__main__":
    app.run(debug=True)
