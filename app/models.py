import datetime
import os

import jwt
from werkzeug.security import generate_password_hash, check_password_hash

from app.ext.database import db


class Video(db.Model):
    __tablename__ = "videos"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), default=1)


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    videos = db.relationship("Video", backref="category")


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)

    @property
    def password(self):
        raise AttributeError("password is not a readable attribute")

    @password.setter
    def password(self, password):
        """Create a password hash to criptograph user password."""
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password: str) -> str:
        return check_password_hash(self.password_hash, password)

    def encode_auth_token(self):
        """Generates the Auth Token
        exp: expiration date of the token
        iat: the time the token is generated
        sub: the subject of the token (the user whom it identifies)
        """
        payload = {
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=300),
            "iat": datetime.datetime.utcnow(),
            "sub": self.id,
        }
        return jwt.encode(payload, os.getenv("SECRET_KEY"))

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(
                auth_token, os.getenv("SECRET_KEY"), algorithms="HS256"
            )
            return payload["sub"]
        except jwt.ExpiredSignatureError:
            return "Signature expired. Please log in again."
        except jwt.InvalidTokenError:
            return "Invalid token. Please log in again."
