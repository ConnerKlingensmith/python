from flask import Flask, jsonify

app=Flask(__name__)

request_count=0

@app.route("/hello")
def hello():
    global request_count

    request_count += 1
    return jsonify({
        "message": "demo example",
        "request_number": request_count
        })

if __name__ == "__main__":
    app.run(debug=True)
