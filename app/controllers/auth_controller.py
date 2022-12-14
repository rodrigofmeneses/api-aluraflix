from flask import Blueprint, request
from marshmallow import ValidationError
from werkzeug.exceptions import BadRequest
from app.ext.database import db
from app.ext.schemas.users_schema import user_schema
from app.ext.schemas.auth_schema import auth_schema
from app.models import User
from app.controllers.helpers import token_required



auth = Blueprint("auth", __name__, url_prefix="/auth")
auth.before_app_request(token_required)

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

    return {"user": user_schema.dump(user), "token": user.encode_auth_token()}, 201


@auth.post("/login/")
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

    try:
        auth = auth_schema.load(json_data)
    except ValidationError as err:
        return err.messages, 400
    
    username = auth.get('username')
    password = auth.get('password')
    user = User.query.filter_by(username=username).first()
    if not user or not user.verify_password(password):
        return {"message": "Please send valids username and password"}, 401
    
    return {
        "message": f"user {username} authenticated, please, send this token for all requisitions except /videos/free",
        "token": f"{user.encode_auth_token()}"
        }, 200
