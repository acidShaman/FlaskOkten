from marshmallow import Schema, fields
from marshmallow.validate import Length


class UserSchema(Schema):
    class Meta:
        load_only = ('password', )

    id = fields.Integer()
    email = fields.Email(required=True)
    name = fields.String(required=True, validate=Length(2, 50))
    password = fields.String(required=True, validate=Length(6, 50))


class PostSchema(Schema):
    id = fields.Integer()
    title = fields.String(required=True)
    text = fields.String(required=True, validate=Length(3, 400))
    user_id = fields.Integer(required=True)