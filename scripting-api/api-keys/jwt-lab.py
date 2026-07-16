import jwt, datetime
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)
SECRET = 'dev-secret-change-me'

users = {'alice': 'password1', 'bob': 'password2'}

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if users.get(username) == password:
        payload = {
            'username': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
        }
        token = jwt.encode(payload, SECRET, algorithm='HS256')
        resp = make_response({'message': 'Logged in'})
        resp.set_cookie('jwt', token, httponly=True, samesite='Lax')
        return resp
    return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/protected')
def protected():
    token = request.cookies.get('jwt')
    if not token:
        return jsonify({'error': 'Missing token'}), 401
    try:
        payload = jwt.decode(token, SECRET, algorithms=['HS256'])
        return jsonify({'message': f'Hello, {payload["username"]}!'}), 200
    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'Token expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Invalid token'}), 401

@app.route('/logout')
def logout():
    resp = make_response({'message': 'Logged out'})
    resp.set_cookie('jwt', '', expires=0)
    return resp

if __name__ == '__main__':
    app.run(debug=True)

"""
# Example curl commands for login and using JWT cookie:
# curl is not a browser, so cookies must be explicitly saved and reused using -c and -b.
#
# Login and save JWT cookie:
curl -i -X POST http://localhost:5000/login 
   -H "Content-Type: application/json" 
   -d '{"username":"alice","password":"password1"}' 
   -c cookies.txt

# Access a protected endpoint using the saved cookie:
curl -i http://localhost:5000/protected -b cookies.txt
"""
