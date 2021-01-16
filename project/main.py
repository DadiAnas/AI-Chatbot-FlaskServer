from flask import Blueprint, render_template

from project.controllers.auth import is_logged_in

main = Blueprint('main',__name__)

@main.route('/')
@is_logged_in
def index():
    return render_template('login.html')
