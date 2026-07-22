import os
import secrets
import time
import requests

from functools import wraps
from flask import Flask, request, redirect, session, url_for, render_template, abort

app = Flask(__name__)

# Session cookie encryption key (for lab only). Use env var in real apps.
app.secret_key = os.getenv("FLASK_SECRET_KEY", secrets.token_hex(32))

GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID", "")
GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET", "")
GITHUB_REDIRECT_URI = os.getenv("GITHUB_REDIRECT_URI", "http://localhost:8080/callback")


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "github_user" not in session:
            return redirect(url_for("login_page"))
        return func(*args, **kwargs)
    return wrapper


@app.before_request
def before():
    request.start = time.time()
    ua = request.headers.get("User-Agent", "unknown")
    ip = request.remote_addr
    print(f"[REQ] {request.method} {request.path} from {ip} UA={ua}")


@app.after_request
def after(resp):
    dur = (time.time() - request.start) * 1000
    print(f"[DONE] {request.method} {request.path} {resp.status_code} in {dur:.2f}ms")
    return resp


@app.route("/")
def login_page():
    """
    Shows login page.

    Example:
      Open in browser:
        http://localhost:8080/
    """
    return render_template("login.html")


@app.route("/login")
def login():
    """
    Redirects user to GitHub authorization screen.

    Example:
      Open in browser:
        http://localhost:8080/login
    """
    if not GITHUB_CLIENT_ID or not GITHUB_CLIENT_SECRET:
        abort(500, description="Missing GITHUB_CLIENT_ID or GITHUB_CLIENT_SECRET env vars")

    state = secrets.token_urlsafe(24)
    session["oauth_state"] = state

    params = {
        "client_id": GITHUB_CLIENT_ID,
        "redirect_uri": GITHUB_REDIRECT_URI,
        "scope": "read:user",
        "state": state,
        "allow_signup": "true",
    }

    url = "https://github.com/login/oauth/authorize"
    req = requests.Request("GET", url, params=params).prepare()
    return redirect(req.url)


@app.route("/callback")
def callback():
    """
    OAuth callback endpoint.
    GitHub redirects here with ?code=...&state=...

    Example:
      This is hit by GitHub automatically after login.
    """
    code = request.args.get("code", "")
    state = request.args.get("state", "")
    expected_state = session.get("oauth_state", "")

    if not code:
        abort(400, description="Missing code")
    if not state or state != expected_state:
        abort(400, description="Invalid state")

    token_url = "https://github.com/login/oauth/access_token"
    token_resp = requests.post(
        token_url,
        headers={"Accept": "application/json"},
        data={
            "client_id": GITHUB_CLIENT_ID,
            "client_secret": GITHUB_CLIENT_SECRET,
            "code": code,
            "redirect_uri": GITHUB_REDIRECT_URI,
        },
        timeout=10,
    )
    token_resp.raise_for_status()
    token_json = token_resp.json()
    access_token = token_json.get("access_token")

    if not access_token:
        abort(401, description="Failed to obtain access token")

    user_resp = requests.get(
        "https://api.github.com/user",
        headers={
            "Authorization": f"Bearer {access_token}",
            "Accept": "application/vnd.github+json",
        },
        timeout=10,
    )
    user_resp.raise_for_status()
    user = user_resp.json()

    session["github_user"] = {
        "login": user.get("login"),
        "id": user.get("id"),
    }

    return redirect(url_for("dashboard"))


@app.route("/dashboard")
@login_required
def dashboard():
    """
    Protected page. Requires OAuth login.

    Example:
      Open in browser:
        http://localhost:8080/dashboard
    """
    username = session["github_user"]["login"]
    return render_template("dashboard.html", username=username)


@app.route("/logout")
def logout():
    """
    Logs user out by clearing session.

    Example:
      Open in browser:
        http://localhost:8080/logout
    """
    session.clear()
    return redirect(url_for("login_page"))


@app.errorhandler(400)
@app.errorhandler(401)
@app.errorhandler(500)
def handle_error(e):
    # For a web lab, keep it simple and readable.
    return f"{e.code} {e.name}: {e.description}", e.code


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
