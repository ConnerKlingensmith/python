from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", message="Hello from Flask behind Nginx")

@app.route("/api/data")
def data():
    return jsonify({
        "service": "flask-backend",
        "status": "ok",
        "message": "Hello from the API"
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

# Test Directly in Browser
    # http://localhost:5000/
    # http://localhost:5000/api/data

# Ensure HTTPD service is NOT running

# Add Config file
#   sudo vi /etc/nginx/conf.d/flask_proxy.conf
