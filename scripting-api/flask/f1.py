from flask import Flask, abort, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app) # enables flask CORS

@app.before_request
def log_request():    # Shows the method and the path requested by client in the server logs 
    print("Method: ", request.method)
    print("Path: ", request.path)    

@app.route("/")
def home():
    return "<p>Welcome to the default webpage</p>"

@app.route("/about")
def about():
    return "<p>This is the about page</p>"

@app.route("/server")
def server():
    return "servername: webserver1"

# Error Handling
@app.route("/switches/<id>")
def switches(id):
    abort(404)

@app.errorhandler(404)
def page_not_found(error):
    return jsonify({
        "error": "page not found"
        }),404

if __name__ == "__main__":
    app.run(debug=True, host="172.17.0.1", port=8080)
