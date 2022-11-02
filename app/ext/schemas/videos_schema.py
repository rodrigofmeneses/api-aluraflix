from app.ext.serializer import ma
from app.models import Videos

from marshmallow import validates_schema, ValidationError
from .videos_validators import titulo_validate, descricao_validate, url_validate


class VideoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Videos
    
    @validates_schema
    def validate(self, data, **kwargs):
        errors = {}
        if not titulo_validate(data['titulo']):
            errors['titulo'] = ['Titulo invalido']
        if not descricao_validate(data['descricao']):
            errors['descricao'] = ['Descrição inválida']
        if not url_validate(data['url']):
            errors['url'] = ['URL inválida']
        if errors:
            raise ValidationError(errors)
        


video_schema = VideoSchema()