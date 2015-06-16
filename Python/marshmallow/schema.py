from marshmallow import Schema, fields

class UserSchema(Schema):

        name = fields.Str()
        email = fields.Email()
        created_at = fields.DateTime()

