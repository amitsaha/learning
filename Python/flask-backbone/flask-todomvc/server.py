from flask import Flask, abort, render_template, request, jsonify
import dataset
db = dataset.connect('sqlite:///todos.db')
todos = db['todos']

app = Flask(__name__, static_url_path='')
app.debug = True

@app.route('/')
def index():
    return render_template('index.html', todos=list(todos.all()))

@app.route('/todos/', methods=['POST'])
def todo_create():
    todo = request.get_json()
    todos.insert(todo)
    return _todo_response(todo)

@app.route('/todos/<int:id>')
def todo_read(id):
    todo = todos.find_one(id=id)
    if todo is None:
        abort(404)
    return todo

@app.route('/todos/<int:id>', methods=['PUT', 'PATCH'])
def todo_update(id):
    todo = request.get_json()
    todos.update(todo, ['id'])
    return _todo_response(todo)

@app.route('/todos/<int:id>', methods=['DELETE'])
def todo_delete(id):
    todos.delete(id=id)
    return _todo_response({})

def _todo_response(todo):
    return jsonify(**todo)

if __name__ == '__main__':
    app.run(port=8000)
