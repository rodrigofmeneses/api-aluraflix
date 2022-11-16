from flask import Flask
from dynaconf import FlaskDynaconf


def create_app(**config):
    app = Flask(__name__)
    FlaskDynaconf(app, **config)
    app.config.load_extensions("EXTENSIONS")
    return app
