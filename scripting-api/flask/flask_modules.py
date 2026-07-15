## Use request.args to access parameters
@app.route('/search')
def search():
    term = request.args.get('q', '')
    return jsonify({'results': [], 'query': term})

## Access headers with request.headers
@app.route('/whoami')
def whoami():
    agent = request.headers.get('User-Agent', 'unknown')
    return jsonify({'user_agent': agent})

## Custom Response and Status
from flask import make_response
@app.route('/custom')
def custom():
    resp = make_response(jsonify({'msg': 'hi'}), 202)
    resp.headers['X-Custom'] = 'value'
    return resp

## Custom Error Handlers
@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(400)
def bad_request(e):
    return jsonify({'error': 'Bad request'}), 400
    
    ## Raise Errors with abort()
    from flask import abort
    @app.route('/fail')
    def fail():
        abort(400, description='You failed!')

## Blueprints for Modular Apps
from flask import Blueprint
user_bp = Blueprint('user', __name__)

@user_bp.route('/users')
def list_users():
    return jsonify(list(user_database.values()))

app.register_blueprint(user_bp)

## Before/After Request Hooks
@app.before_request
def log_request():
    print(f"{request.method} {request.path}")

@app.after_request
def add_header(response):
    response.headers['X-Processed-By'] = 'Flask'
    return response

## Flask Config and Environment
app.config['MY_SETTING'] = 'value'
import os
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev')
