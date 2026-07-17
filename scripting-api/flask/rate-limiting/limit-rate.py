from flask import Flask, jsonify, make_response

app = Flask(__name__)

LIMIT = 5
request_count = 0

@app.route("/hello")
def hello():
    global request_count

    if request_count >= LIMIT:
        response = make_response(jsonify({
            "error": "Rate limit exceeded"
            }), 429)

        response.headers["Retry-After"] = "30"
        return response

    request_count += 1

    return jsonify({
        "message": "Hello from Flask!",
        "request_number": request_count
    })

if __name__ == "__main__":
    app.run(debug=True)
