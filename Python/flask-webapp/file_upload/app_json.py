import json
from flask import Flask, request
app = Flask(__name__, static_url_path='')
app.debug = True

# Python client: client_json.py
@app.route('/', methods=['POST'])
def index():
    metadata_json = json.loads(request.values.get('data'))
    # the files uploaded
    # request.files is a MultiDict:
    # http://werkzeug.pocoo.org/docs/0.10/datastructures/#werkzeug.datastructures.MultiDict
    for f in request.files:
        for attribute in ['x', 'y', 'crop_width', 'crop_height']:
            #print dir(request.files[f])
            print request.files[f].filename, request.files[f].content_type, \
                '%s: ' % attribute, metadata_json[f][attribute]
    return 'OK'

if __name__ == '__main__':
    app.run(port=8000)
