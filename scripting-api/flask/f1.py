from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Welcome to the default webpage</p>"

@app.route("/about")
def about():
    return "<p>This is the about page</p>"

@app.route("/server")
def server():
    return "servername: webserver1"


if __name__ == "__main__":
    app.run(debug=True, host="172.17.0.1", port=8080)
