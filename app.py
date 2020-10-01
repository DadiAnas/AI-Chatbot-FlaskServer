from flask import Flask
from flask_material import Material

def create_app():
    app = Flask(__name__, static_url_path='/static')
    Material(app)
    app.config['UPLOAD_FOLDER'] = '/static/styles/images/products'
    app.config['MAX_CONTENT_PATH'] = '25,165,824'
    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


if __name__ == '__main__':
    create_app.run(host="0.0.0.0")
