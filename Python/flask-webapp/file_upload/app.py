from flask import Flask, request
app = Flask(__name__, static_url_path='')
app.debug = True

# File uploading using httpie:
# http -f POST http://127.0.0.1:8000 filedata@app.py
@app.route('/', methods=['POST'])
def index():
    # the files uploaded
    # request.files is a MultiDict:
    # http://werkzeug.pocoo.org/docs/0.10/datastructures/#werkzeug.datastructures.MultiDict
    return str([f.filename for f in request.files.getlist('filedata')])

if __name__ == '__main__':
    app.run(port=8000)
