import os
from flask import Flask

from app.ext.database import init_app as init_db
from app.ext.serializer import init_app as init_serializer
from app.ext.commands import init_app as init_commands
from app.controllers import init_app as init_controllers


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    init_db(app)
    init_serializer(app)
    init_commands(app)
    init_controllers(app)
    return app
