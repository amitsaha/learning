from flask import Flask, request
app = Flask(__name__, static_url_path='')
app.debug = True

# Python client: client_form.py
@app.route('/', methods=['POST'])
def index():
    # the files uploaded
    # request.files is a MultiDict:
    # http://werkzeug.pocoo.org/docs/0.10/datastructures/#werkzeug.datastructures.MultiDict
    for f in request.files:
        for attribute in ['x', 'y', 'crop_width', 'crop_height']:
            #print dir(request.files[f])
            print request.files[f].filename, request.files[f].content_type, \
                '%s: ' % attribute, request.form.get('%s.%s' % (f, attribute), None)
    return 'OK'

if __name__ == '__main__':
    app.run(port=8000)
