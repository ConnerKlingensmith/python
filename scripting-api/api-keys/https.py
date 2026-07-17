from flask import Flask, request, jsonify, make_response
import ssl

app = Flask(__name__)

@app.route('/')
def index():
    resp = make_response({'message': 'Hello, HTTPS world!'})
    # Example: set a secure, HttpOnly cookie
    resp.set_cookie('jwt', 'demo-token', httponly=True, secure=True, samesite='Lax')
    return resp

if __name__ == '__main__':
    context = ('cert.pem', 'key.pem')  # Path to your cert and key
    app.run(ssl_context=context, debug=True)
