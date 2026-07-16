"""
User API Example (Flask) with API Key Authentication

# Create a new user (PUBLIC - returns the API key ONCE, store it safely)
curl -X POST -H "Content-Type: application/json" -d '{"username": "alice", "role": "user"}' http://localhost:8000/newuser

# Reset a user's API key (PUBLIC by design - see note below - returns new key)
curl -X POST http://localhost:8000/users/alice/reset-key

# All endpoints below require a valid API key in the Authorization header:
#   Authorization: Bearer <api_key>

# Get user details by username
curl -H "Authorization: Bearer <api_key>" http://localhost:8000/users/alice

# Update username by id
curl -X PUT -H "Content-Type: application/json" -H "Authorization: Bearer <api_key>" \
     -d '{"username": "alice2"}' http://localhost:8000/users/1

# Delete user by id
curl -X DELETE -H "Authorization: Bearer <api_key>" http://localhost:8000/users/1

# Get all users
curl -H "Authorization: Bearer <api_key>" http://localhost:8000/users
"""

import hashlib
import logging
import secrets
from datetime import datetime, timezone

from flask import Flask, request, jsonify, g

app = Flask(__name__)

# ---------------------------------------------------------------------------
# Logging setup
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger("api_auth")

# ---------------------------------------------------------------------------
# In-memory user database (lost on restart)
# Each user record stores api_key_hash instead of the raw API key.
# ---------------------------------------------------------------------------
user_database = {
    1: {"id": 1, "username": "admin", "role": "admin", "api_key_hash": None},
    2: {"id": 2, "username": "bob", "role": "user", "api_key_hash": None},
}
next_id = 3

# Endpoints that do NOT require an API key.
# NOTE: reset-key is intentionally public here (mirrors "password reset"
# UX where you prove identity via username). In a real system you'd want
# to gate this behind something stronger (email verification, the old key,
# an admin key, etc.) since anyone who knows a username could otherwise
# lock out that user by resetting their key. Flagging this tradeoff rather
# than silently shipping it.
PUBLIC_ENDPOINTS = {
    ("create_user", "POST"),
    ("reset_key", "POST"),
}


# ---------------------------------------------------------------------------
# API key helpers
# ---------------------------------------------------------------------------
def generate_api_key():
    """Generate a secure random API key."""
    return secrets.token_hex(16)


def hash_api_key(raw_key):
    """Hash an API key for storage/comparison. Never store the raw key."""
    return hashlib.sha256(raw_key.encode("utf-8")).hexdigest()


def find_user_by_username(username):
    for user in user_database.values():
        if user["username"] == username:
            return user
    return None


def authenticate(raw_key):
    """Return the matching user dict for a raw API key, or None."""
    if not raw_key:
        return None
    candidate_hash = hash_api_key(raw_key)
    for user in user_database.values():
        stored_hash = user.get("api_key_hash")
        if stored_hash and secrets.compare_digest(stored_hash, candidate_hash):
            return user
    return None


def extract_key_from_header():
    """
    Pull the API key out of the Authorization header.
    Supports both "Authorization: Bearer <key>" and a bare "Authorization: <key>".
    """
    auth_header = request.headers.get("Authorization", "")
    if not auth_header:
        return None
    parts = auth_header.split()
    if len(parts) == 2 and parts[0].lower() == "bearer":
        return parts[1]
    if len(parts) == 1:
        return parts[0]
    return None


# ---------------------------------------------------------------------------
# Hooks: auth check, logging
# ---------------------------------------------------------------------------
@app.before_request
def check_api_key():
    endpoint = request.endpoint
    method = request.method

    # Let Flask's own error handling deal with unmatched routes.
    if endpoint is None:
        return None

    g.auth_user = None
    g.request_started_at = datetime.now(timezone.utc)

    if (endpoint, method) in PUBLIC_ENDPOINTS:
        return None  # no auth required

    raw_key = extract_key_from_header()
    user = authenticate(raw_key)

    if user is None:
        logger.warning(
            "AUTH FAILURE endpoint=%s method=%s path=%s remote_addr=%s",
            endpoint, method, request.path, request.remote_addr,
        )
        return jsonify({"error": "Missing or invalid API key"}), 401

    g.auth_user = user
    logger.info(
        "AUTH OK user=%s endpoint=%s method=%s",
        user["username"], endpoint, method,
    )
    return None


@app.after_request
def log_response(response):
    duration_ms = None
    started_at = getattr(g, "request_started_at", None)
    if started_at is not None:
        duration_ms = (datetime.now(timezone.utc) - started_at).total_seconds() * 8080

    auth_user = getattr(g, "auth_user", None)
    logger.info(
        "REQUEST path=%s method=%s status=%s user=%s duration_ms=%s",
        request.path,
        request.method,
        response.status_code,
        auth_user["username"] if auth_user else "anonymous/public",
        f"{duration_ms:.2f}" if duration_ms is not None else "n/a",
    )
    return response


# ---------------------------------------------------------------------------
# Public endpoints
# ---------------------------------------------------------------------------
@app.route('/newuser', methods=['POST'])
def create_user():
    """Create a new user and issue an API key. Key is shown ONCE."""
    global next_id
    data = request.get_json(silent=True)
    if not data or "username" not in data:
        return jsonify({"error": "Missing username"}), 400

    if find_user_by_username(data["username"]) is not None:
        return jsonify({"error": "Username already exists"}), 409

    raw_key = generate_api_key()
    user = {
        "id": next_id,
        "username": data["username"],
        "role": data.get("role", "user"),
        "api_key_hash": hash_api_key(raw_key),
    }
    user_database[next_id] = user
    next_id += 1

    response_body = {
        "id": user["id"],
        "username": user["username"],
        "role": user["role"],
        "api_key": raw_key,  # only time the raw key is ever returned
    }
    return jsonify(response_body), 201


@app.route('/users/<username>/reset-key', methods=['POST'])
def reset_key(username):
    """Generate and store a new API key for a user. Key is shown ONCE."""
    user = find_user_by_username(username)
    if not user:
        return jsonify({"error": "User not found"}), 404

    raw_key = generate_api_key()
    user["api_key_hash"] = hash_api_key(raw_key)

    return jsonify({
        "id": user["id"],
        "username": user["username"],
        "api_key": raw_key,
    }), 200


# ---------------------------------------------------------------------------
# Protected endpoints (require Authorization header, enforced by before_request)
# ---------------------------------------------------------------------------
def public_view(user):
    """Strip the api_key_hash out of a user record before returning it."""
    return {k: v for k, v in user.items() if k != "api_key_hash"}


@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    """Get user details by username"""
    user = find_user_by_username(username)
    if user:
        return jsonify(public_view(user))
    return jsonify({"error": "User not found"}), 404


@app.get('/users')
def get_users():
    """Get all users"""
    return jsonify({uid: public_view(u) for uid, u in user_database.items()})


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Update a user's username by id"""
    user = user_database.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    data = request.get_json(silent=True)
    if not data or "username" not in data:
        return jsonify({"error": "Missing username"}), 400
    user["username"] = data["username"]
    return jsonify(public_view(user))


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

# ---------------------------------------------------------------------------
# Error handlers
# ---------------------------------------------------------------------------
@app.errorhandler(401)
def unauthorized_error(error):
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(500)
def internal_error(error):
    logger.exception("Internal server error")
    return jsonify({"error": "Internal server error"}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
