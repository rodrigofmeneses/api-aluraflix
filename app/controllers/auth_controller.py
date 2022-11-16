from flask import Blueprint, request
from marshmallow import ValidationError
from werkzeug.exceptions import BadRequest
from app.ext.database import db
from app.ext.schemas.users_schema import user_schema


auth = Blueprint("auth", __name__, url_prefix="/auth")


@auth.post("/register/")
def register():
    """Register a user with POST method.
    Return:
        Response JSON with added user or error message
    """
    try:
        json_data = request.get_json()
    except BadRequest:
        return {
            "message": "Bad Request, JSON with username and password fields expected"
        }, 400

    try:
        user = user_schema.load(json_data)
    except ValidationError as err:
        return err.messages, 400

    db.session.add(user)
    db.session.commit()

    return user_schema.dump(user), 201


@auth.post("/")
def authenticate():
    """Authenticate user with POST method. Using authorization header.
    Return:
        Response JSON with acept with JWT TOKEN or refuse autentication
    """
    try:
        json_data = request.get_json()
    except BadRequest:
        return {
            "message": "Bad Request, JSON with username and password fields expected"
        }, 400

    if not json_data or not json_data['username'] or not json_data['password']:
        return {"message": "Please send valids username and password"}, 401
    return {
        "message": "user authenticated",
        "token": "123"
        }, 200
