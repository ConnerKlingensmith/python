from flask import Flask, render_template, request

app = Flask(__name__)

api_keys = [
    {'value': 'key1', 'permissions': ['read']},
    {'value': 'key2', 'permissions': ['read', 'write']}
]

@app.route('/dashboard')
def dashboard():
    username = request.args.get('username', 'alice')
    return render_template('dashboard.html', username=username, api_keys=api_keys)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Dummy check for demonstration
        if username == 'alice' and password == 'password1':
            return render_template('dashboard.html', username=username, api_keys=api_keys)
        else:
            error = 'Invalid credentials'
    return render_template('login.html', error=error)

# ...other endpoints as needed for your app...

if __name__ == '__main__':
    app.run(debug=True)
