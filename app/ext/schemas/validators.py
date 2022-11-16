from app.models import User
from marshmallow import ValidationError


def not_blank(data):
    if not data:
        raise ValidationError("Must not blank.")

def unique_username(username):
    if not User.query.filter(User.username == username).first():
        raise ValidationError("Username must be unique")
