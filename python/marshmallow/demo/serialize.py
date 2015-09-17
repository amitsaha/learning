from user import User
from schema import UserSchema

from marshmallow import pprint

user = User(name='M K', email='mk@email.com')
schema = UserSchema()
result = schema.dump(user)
pprint(result.data)

json_result = schema.dumps(user)
pprint(json_result.data)

