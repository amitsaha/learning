from sympy import Symbol, pprint
from flask import Flask, request
app = Flask(__name__, static_url_path='')
app.debug = True

@app.route('/')
def index():
    x = Symbol('x')
    pprint(x**2)    
    return unicode(x**2)

if __name__ == '__main__':
    app.run(port=8000)
