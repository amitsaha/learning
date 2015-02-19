from flask import Flask, abort, render_template, request, jsonify

app = Flask(__name__, static_url_path='')
app.debug = True

@app.route('/')
def index():
    msg = {'host1:8000': 'Request from host1',
           'host2:8000': 'Request from host2',
           }
    return msg[request.host]

if __name__ == '__main__':
    app.run(port=8000)
