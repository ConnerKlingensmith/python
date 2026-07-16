"""
Simple API Key Example (intentionally lacks proper hashing and events/hooks)

USAGE:
# Try with a valid key
curl -H "Username: alice" -H "Authorization: Bearer secretkey1" http://localhost:5000/hello

# Try with an invalid key
curl -H "Username: alice" -H "Authorization: Bearer wrongkey" http://localhost:5000/hello
"""

from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# In-memory user/key database
user_db = {
    "alice": {"api_key": "b7f3e2c1a9d4f6e8b2c7a1e3d5f8b6c4", "role": "admin"},
    "bob": {"api_key": "e4c2b1a7d9f3c6e8a2b5d7f1e3c8a6b4", "role": "user"}
}

def check_api_key():
    auth = request.headers.get('Authorization', '')
    username = request.headers.get('Username', '')
    if not username:
        abort(401, description="Missing Username header")
    if auth.startswith('Bearer '):
        key = auth.split(' ', 1)[1]
        info = user_db.get(username)
        if info and info["api_key"] == key:
            return username  # Authenticated
    abort(401, description="Invalid or missing API key or username")

@app.route('/hello')
def hello():
    user = check_api_key()
    return jsonify({"message": f"Hello, {user}!"})

if __name__ == '__main__':
    app.run(debug=True)
