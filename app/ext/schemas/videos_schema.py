from app.ext.serializer import ma
from app.models import Video

from marshmallow import post_load, validates_schema, ValidationError, fields
from .validators import must_not_blank


class VideoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Video
    id = ma.auto_field(dump_only=True)
    titulo = ma.auto_field(required=True, validate=[must_not_blank])
    descricao = ma.auto_field(required=True, validate=[must_not_blank])
    url = fields.Url(required=True)
    
    @post_load
    def make_user(self, data, **kwargs):
        return Video(**data)
        

video_schema = VideoSchema()