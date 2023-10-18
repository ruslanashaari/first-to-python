from flask import (
    Flask,
    url_for,
    request,
    jsonify
)
from markupsafe import escape
from sqlalchemy import create_engine
from users_model import UserModel

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello/')
def hello():
    return 'Hello, World'

@app.route('/welcome')
def welcome():
    return 'Welcome to a new world'

@app.route('/konichiwa')
def konichiwa():
    return 'Konichiwa desu'

@app.route('/user/<username>')
def show_user_profile(username):
    # show user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {escape(post_id)}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Path {escape(subpath)}'

with app.test_request_context():
    print(url_for('hello'))
    print(url_for('welcome'))
    print(url_for('konichiwa', next='/'))
    print(url_for('show_user_profile', username = 'John Doe'))

# @app.route('/login', methods=['GET','POST'])
# def login():
#     if request.method == 'GET':
#         return 'GET LOGIN PAGE'
#     else:
#         return 'processing login'

@app.get('/login')
def get_login():
    return 'show login form'

@app.post('/login')
def post_login():
    return 'processing login'

@app.get('/api/test/<user_id>')
def api_test(user_id):
    return {
        "user_id": escape(user_id),
        "username": 'JohnDoe',
        "user_type": 'unknown',
        "is_active": True,
    }

@app.get('/api/users')
def api_get_users():
    model = UserModel()
    
    users = model.get_users()
    return jsonify(users)

@app.get('/api/user/<int:user_id>')
def api_get_user(user_id):
    model = UserModel()

    user = model.get_user(user_id)
    return jsonify(user)

@app.post('/api/user/create')
def api_create_user():
    model = UserModel()

    status = model.create_user(request.form)
    return status

@app.post('/api/user/update/<int:user_id>')
def api_update_user(user_id):
    model = UserModel()

    user = model.update_user(user_id, request.form)
    return user

@app.get('/api/user/delete/<int:user_id>')
def api_delete_user(user_id):
    model = UserModel()

    status = model.delete_user(user_id)
    return status