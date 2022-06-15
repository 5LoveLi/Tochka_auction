from marshmallow import Schema, fields
from marshmallow import ValidationError

def must_not_be_blank(data):
    if not data:
        raise ValidationError("Data not provided.")


class LotSchema(Schema):
    id = fields.Int(dump_only=True)
    id_author = fields.Str() # UserSchema(only=('id'))
    name = fields.Str(validate=must_not_be_blank)
    description = fields.Str()
    price = fields.Str(validate=must_not_be_blank)
    time = fields.Str()
    status = fields.Bool()