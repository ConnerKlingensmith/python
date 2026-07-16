from flask import Flask, request, session, jsonify
import secrets

app = Flask(__name__)

# Secret key used to sign session cookies
app.secret_key = "my-secret-key"

VALID_SESSION_IDS = set()

@app.route("/")
def home():
    return "Session Authentication Demo"

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username == "admin" and password == "password":
        sid = secrets.token_hex(16)
        VALID_SESSION_IDS.add(sid)

        session.clear()
        session["user"] = username
        session["sid"] = sid

        return jsonify({
            "message": "Login Successful"
        }), 200

    return jsonify({
        "message": "Invalid Credentials"
    }), 401


@app.route("/profile")
def profile():
    sid = session.get("sid")
    if "user" not in session or sid not in VALID_SESSION_IDS:
        return jsonify({
            "message": "Unauthorized"
        }), 401

    return jsonify({
        "message": f"Welcome {session['user']}"
    })

@app.route("/logout", methods=["POST"])
def logout():
    sid = session.get("sid")
    VALID_SESSION_IDS.discard(sid)
    session.clear()
    return jsonify({
        "message": "Logged Out"
        })

if __name__ == "__main__":
    app.run(debug=True)


# curl -c cookie.txt -X POST http://127.0.0.1:5000/login -H "Content-Type: application/json" -d "{\"username\":\"admin\",\"password\":\"password\"}"
# curl -b cookie.txt http://127.0.0.1:5000/profile
# curl http://127.0.0.1:5000/profile
# curl -b cookie.txt -X POST http://127.0.0.1:5000/logout
# curl -b cookie.txt http://127.0.0.1:5000/profile
