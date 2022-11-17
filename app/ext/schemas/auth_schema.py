from app.ext.serializer import ma
from app.models import User
from .validators import not_blank

from marshmallow.fields import String 

class AuthSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    username = ma.auto_field(validate=[not_blank])
    password = ma.auto_field('password_hash', validate=[not_blank], attribute='password')

auth_schema = AuthSchema()
