from flask import Flask
from dynaconf import FlaskDynaconf
from app.models import Videos


def create_app():
    app = Flask(__name__)
    FlaskDynaconf(app)
    app.config.load_extensions('EXTENSIONS')
    return app