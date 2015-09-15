#Today I learned

Content-Disposition: Proposed as a means for the origin server to suggest a default file name 
(http://www.w3.org/Protocols/rfc2616/rfc2616-sec19.html)


In Vim, use 'n' for forward search and 'N' for backward search


`find -iname` to ignore the case when searching for files


When using "top", use "c" to toggle between process name and the command line


If your tests has docstrings, nose will display the string instead of
the default function/method name:http://bit.ly/1VfJnfr


puppet's nginx resource module's `vhost_cfg_prepend` can be used to enter arbitrary configuration. For example, for parameters not defined by the module such as `large_client_header_buffers`


when you do a `git commit --amend`, you are creating a new commit with a new SHA. HEAD then points to the new SHA instead of the old one.


To upload a file simulating form upload via `httpie`, `http -f POST example.com/jobs name='John Smith' cv@~/Documents/cv.pdf`


`MultiDict`: http://werkzeug.pocoo.org/docs/0.10/datastructures/#werkzeug.datastructures.MultiDict


Demo of a Flask app to handle file uploads:

```python
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
```


