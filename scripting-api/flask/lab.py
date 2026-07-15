"""
User API Example (Flask)

# Create a new user
curl -X POST -H "Content-Type: application/json" -d '{"username": "alice", "role": "user"}' http://localhost:8000/newuser

# Get user details by username
curl http://localhost:8000/users/alice

# Update username by id
curl -X PUT -H "Content-Type: application/json" -d '{"username": "alice2"}' http://localhost:8000/users/1

# Delete user by id
curl -X DELETE http://localhost:8000/users/1

# Get all users
curl http://localhost:8000/users

# Get user details by username (again)
curl http://localhost:8000/users/alice

# Note: Both GET endpoints above can also be accessed directly in your browser by navigating to:
#   http://localhost:8000/users
#   http://localhost:8000/users/alice
#   You can replace localhost with public ip
#   if port and firewall is open
"""

from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# In-memory user database (lost on restart)
user_database = {
    1: {"id": 1, "username": "admin", "role": "admin"},
    2: {"id": 2, "username": "bob", "role": "user"}
}
next_id = 3

@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    """Get user details by username"""
    for user in user_database.values():
        if user["username"] == username:
            return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.get('/users')
def get_users():
    """Get all users"""
    return jsonify(user_database)

@app.route('/newuser', methods=['POST'])
def create_user():
    """Create a new user"""
    global next_id
    data = request.get_json()
    if not data or "username" not in data:
        return jsonify({"error": "Missing username"}), 400
    user = {"id": next_id, "username": data["username"], "role": data.get("role", "user")}
    user_database[next_id] = user
    next_id += 1
    return jsonify(user), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Update a user's username by id"""
    user = user_database.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    data = request.get_json()
    if not data or "username" not in data:
        return jsonify({"error": "Missing username"}), 400
    user["username"] = data["username"]
    return jsonify(user)

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete a user by id (forbid deleting admin)"""
    user = user_database.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    if user["role"] == "admin":
        return jsonify({"error": "Cannot delete admin user"}), 403
    del user_database[user_id]
    return '', 204

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=1000)
