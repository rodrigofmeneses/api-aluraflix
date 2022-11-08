from app.ext.serializer import ma
from app.models import Category

from marshmallow import post_load
from .validators import not_blank


class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Category
    id = ma.auto_field(dump_only=True)
    title = ma.auto_field(validate=[not_blank])
    color = ma.auto_field(validate=[not_blank])
    
    @post_load
    def make_user(self, data, **kwargs):
        return Category(**data)
        

category_schema = CategorySchema()