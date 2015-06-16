from schema import ColorSchema
from marshmallow import pprint
from ColorEnum import ColorEnum

class Color(object):

    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return 'Color: {0}'.format(self.color)


color = Color(ColorEnum.red)
schema = ColorSchema()
result = schema.dump(color)
print(type(result.data['color']))
