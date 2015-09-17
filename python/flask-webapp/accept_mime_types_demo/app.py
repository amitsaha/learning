from flask import Flask, request

app = Flask(__name__, static_url_path='')
app.debug = True

@app.route('/')
def index():
    return str(request.accept_mimetypes)

if __name__ == '__main__':
    app.run(port=8000)
