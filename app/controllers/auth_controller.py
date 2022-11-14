from flask import Blueprint, request
from marshmallow import ValidationError
from app.ext.database import db
from app.ext.schemas.users_schema import user_schema


auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.post('/register/')
def register():
    '''Register a user with POST method.
        Return:
            Response JSON with added user or error message
    '''
    json_data = request.get_json()

    try:
        user = user_schema.load(json_data)
    except ValidationError as err:
        return err.messages, 400
    
    db.session.add(user)
    db.session.commit()
    
    return user_schema.dump(user), 201