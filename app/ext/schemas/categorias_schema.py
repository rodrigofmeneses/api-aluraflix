from app.ext.serializer import ma
from app.models import Categoria

from marshmallow import post_load
from .validators import must_not_blank


class CategoriaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Categoria
    id = ma.auto_field(dump_only=True)
    titulo = ma.auto_field(required=True, validate=[must_not_blank])
    descricao = ma.auto_field(required=True, validate=[must_not_blank])
    
    @post_load
    def make_user(self, data, **kwargs):
        return Categoria(**data)
        

categoria_schema = CategoriaSchema()