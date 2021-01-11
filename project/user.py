from flask import request, jsonify, Blueprint
from werkzeug.security import generate_password_hash

from project.auth import is_logged_in
from project.config import cursor, db

user = Blueprint('user', __name__)


@user.route('/users', methods=['GET'])
@is_logged_in
def user_adds():
    return jsonify({'response': 'Il y a déja un utilisateur avec le même username'})

@user.route('/users', methods=['POST'])
def user_add():
    username = request.json.get('username')
    user_first_name = request.json.get('nom')
    user_last_name = request.json.get('prenom')
    user_email = request.json.get('email')
    user_password = request.json.get('password')
    user_hashed_password = generate_password_hash(user_password, method='sha256')
    try:
        cursor.execute(
            "INSERT INTO users(username, user_first_name, user_last_name, user_email,user_password) VALUES(%s, %s, %s, %s, %s)",
            (username, user_first_name, user_last_name, user_email, user_hashed_password))
        db.commit()
        return jsonify({'response': cursor.lastrowid})
    except:
        return jsonify({'response': 'Il y a déja un utilisateur avec le même username'})


@user.route("/users/<int:user_id>", methods=["PUT"])
@is_logged_in
def update_user(user_id):
    username = request.json.get('username')
    user_first_name = request.json.get('user_first_name')
    user_last_name = request.json.get('user_last_name')
    user_email = request.json.get('user_email')
    user_password = request.json.get('password')
    user_hashed_password = generate_password_hash(user_password, method='sha256')
    cursor.execute(
        f"update users set user_first_name = '{user_first_name}', user_last_name = '{user_last_name}', user_email = '{user_email}', user_password = {user_hashed_password} where  user_id = '{user_id}'")

    db.commit()
    return jsonify({'response': list(cursor.fetchone())})
