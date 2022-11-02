from app.models import Videos
from marshmallow import validate, ValidationError


def must_not_blank(data):
    if not data:
        raise ValidationError('Must not blank.')