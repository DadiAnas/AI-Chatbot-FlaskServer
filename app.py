from flask import Flask
from os import urandom
from project.main import main as main_blueprint
from project.controllers.auth import auth as auth_blueprint
from project.controllers.chat_bot import chat_bot as chatbot_blueprint
from project.controllers.user import user as user_blueprint


app = Flask(__name__)

# blueprint for non-auth parts of app
app.register_blueprint(main_blueprint)
app.register_blueprint(auth_blueprint)
app.register_blueprint(chatbot_blueprint)
app.register_blueprint(user_blueprint)
app.secret_key = urandom(12).hex()


if __name__ == '__main__:
    app.run(threaded=True, port=5000)
