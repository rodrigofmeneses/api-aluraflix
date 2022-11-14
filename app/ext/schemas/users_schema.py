from app.ext.serializer import ma
from app.models import User

from marshmallow import post_load
from .validators import not_blank


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
    id = ma.auto_field(dump_only=True)
    username = ma.auto_field(validate=[not_blank])
    password = ma.auto_field('password_hash', validate=[not_blank], load_only=True)
    
    
    @post_load
    def make_user(self, data, **kwargs):
        data['password'] = data.pop('password_hash')
        return User(**data)
        

user_schema = UserSchema()