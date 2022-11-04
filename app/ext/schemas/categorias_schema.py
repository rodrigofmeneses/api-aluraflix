from app.ext.serializer import ma
from app.models import Categoria

from marshmallow import post_load
from .validators import not_blank


class CategoriaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Categoria
    id = ma.auto_field(dump_only=True)
    titulo = ma.auto_field(validate=[not_blank])
    cor = ma.auto_field(validate=[not_blank])
    
    @post_load
    def make_user(self, data, **kwargs):
        return Categoria(**data)
        

categoria_schema = CategoriaSchema()