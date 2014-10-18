import json
import pprint

json_string = '{"menu": {"header": "menu", "items": [{"id": 27}, {"id": 0, "label": "Label 0"}, null, {"id": 93}, {"id": 85}, {"id": 54}, null, {"id": 46, "label": "Label 46"}]}}'

s = json.loads(json_string)
pprint.pprint(s)
