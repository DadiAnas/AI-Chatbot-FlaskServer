from flask import Flask
from project.main import main as main_blueprint


app = Flask(__name__, static_url_path='/project/static/')

# blueprint for non-auth parts of app
app.register_blueprint(main_blueprint)

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
