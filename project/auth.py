from flask import Blueprint, make_response, render_template, redirect, url_for, request, abort, session, jsonify
from werkzeug.security import check_password_hash
from functools import wraps
from .config import cursor


auth = Blueprint('auth', __name__)

# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if not 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return jsonify({'response': 'Unauthorized, Please login'})
    return wrap


@auth.route('/login')
def login_template():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
@is_logged_in
def login():
    if not request.json:
        abort(400)
    user_email = request.json.get('user_email')
    user_password = request.json.get('user_password')
    try:
        cursor.execute(f"select * from users where username='{user_email}' and user_password='{user_password}';")
        user = cursor.fetchone()
        if user[0] == 0 or not check_password_hash(user[6], user_password):
            return jsonify({'response': 'wrong password'})
        session['logged_in'] = True
        return jsonify({'user_info': user})
    except:
        return jsonify({"user_info": 'error'})


@auth.route('/logout')
@is_logged_in
def logout():
    session.clear()
    resp = make_response(redirect(url_for('auth.login')))
    return resp
