from app.ext.serializer import ma
from app.models import Video

from marshmallow import post_load, fields
from .validators import not_blank


class VideoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Video
    id = ma.auto_field(dump_only=True)
    title = ma.auto_field(validate=[not_blank])
    description = ma.auto_field(validate=[not_blank])
    url = fields.URL(required=True)
    category_id = ma.auto_field()
    
    @post_load
    def make_video(self, data, **kwargs):
        return Video(**data)
        

video_schema = VideoSchema()