from marshmallow import ValidationError


def must_not_blank(data):
    if not data:
        raise ValidationError('Must not blank.')