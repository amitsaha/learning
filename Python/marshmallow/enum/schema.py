from marshmallow import Schema, fields
from ColorEnum import ColorEnum as C
class ColorSchema(Schema):
    color = fields.Select([C.red, C.blue, C.green])
