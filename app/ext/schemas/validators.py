from marshmallow import ValidationError


def not_blank(data):
    if not data:
        raise ValidationError('Must not blank.')