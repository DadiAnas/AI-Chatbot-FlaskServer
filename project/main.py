from flask import Blueprint, jsonify, request, render_template

from project.auth import is_logged_in

main = Blueprint('main',__name__)

@main.route('/')
def chatbot_home():
    responses=["hi","hello","how are you ?","good to see you here"]
    response = [
        {'id':0 ,'message': 'Hello','trigger':1},
                ]
    return jsonify(response)
