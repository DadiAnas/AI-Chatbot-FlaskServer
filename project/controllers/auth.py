from flask import Blueprint, make_response, render_template, redirect, url_for, request, abort, session, jsonify
from werkzeug.security import check_password_hash
from functools import wraps
from project.config import session_factory
from project.model import user_model

auth = Blueprint('auth', __name__)


# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return jsonify({'response': 'Unauthorized, Please login', 'code':  403})
    return wrap


@auth.route('/login')
def login_template():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login():
    if not request.json:
        abort(400)
    user_email = request.json.get('user_email')
    user_password = request.json.get('user_password')
    try:
        new_session = session_factory()
        an_user = new_session.query(user_model.User).filter_by(user_email=user_email).first()
        if not check_password_hash(an_user.user_password, user_password):
            return jsonify({'response': 'wrong password'})
        user_format = {'user_id': an_user.user_id,
                       'username': an_user.username,
                       'user_email': an_user.user_email,
                       'user_first_name': an_user.user_first_name,
                       'user_last_name': an_user.user_last_name}
        session['logged_in'] = True
        return jsonify({'response': user_format,'code':200})
    except:
        return jsonify({"error": f'wrong data', 'code': 400})


@auth.route('/logout')
@is_logged_in
def logout():
    session.clear()
    resp = make_response(redirect(url_for('auth.login')))
    return resp
