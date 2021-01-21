from flask import request, jsonify, Blueprint
from werkzeug.security import generate_password_hash
from project.config import add_object, get_objects, update_object, get_object, delete_object
from project.controllers.auth import is_logged_in
from project.model import user_model

user = Blueprint('user', __name__)


@user.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    an_user = get_object(user_model.User, user_id)
    if an_user:
        user_format = {'user_id': an_user.user_id,
                       'username': an_user.username,
                       'user_email': an_user.user_email,
                       'user_first_name': an_user.user_first_name,
                       'user_last_name': an_user.user_last_name}
        return jsonify({'response': user_format})

    else:
        return jsonify({'error': f'user_id={user_id} not exist', 'code': 400})


@user.route('/users', methods=['GET'])
def get_users():
    users = []
    fetched_users = get_objects(user_model.User)
    if fetched_users:
        for an_user in fetched_users:
            user_format = {'user_id': an_user.user_id,
                           'username': an_user.username,
                           'user_email': an_user.user_email,
                           'user_first_name': an_user.user_first_name,
                           'user_last_name': an_user.user_last_name}

            users.append(user_format)
        return jsonify({'response': users})
    else:
        return jsonify({'error': 'Cannot fetch users', 'code': 400})


@user.route('/users', methods=['POST'])
def user_add():
    username = request.json.get('username')
    user_first_name = request.json.get('user_first_name')
    user_last_name = request.json.get('user_last_name')
    user_email = request.json.get('user_email')
    user_password = request.json.get('user_password')
    user_hashed_password = generate_password_hash(user_password, method='sha256')
    a_user = user_model.User(username=username, user_first_name=user_first_name, user_last_name=user_last_name,
                             user_email=user_email, user_password=user_hashed_password)
    try:
        add_object(a_user)
        return jsonify({'response': a_user.username + ' added','code':200})
    except:
        return jsonify({'error': 'cannot add user', 'code': 400})


@user.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    username = request.json.get('username')
    user_first_name = request.json.get('user_first_name')
    user_last_name = request.json.get('user_last_name')
    user_email = request.json.get('user_email')
    user_password = request.json.get('password')
    user_hashed_password = generate_password_hash(user_password, method='sha256')
    try:
        a_user = user_model.User(user_id=user_id, username=username, user_first_name=user_first_name,
                                 user_last_name=user_last_name,
                                 user_email=user_email, user_password=user_hashed_password)
        update_object(a_user)
        return jsonify({'response': f'user_id {user_id} updated'})
    except:
        return jsonify({'error': f'error updating user_id={user_id}', 'code': 400})


@user.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        delete_object(user_model.User, user_id)
        return jsonify({'respponse': f'{user_id} deleted'})
    except:
        return jsonify({'error': f'user_id={user_id} not exist', 'code': 400})
