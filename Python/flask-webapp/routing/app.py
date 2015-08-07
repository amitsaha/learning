from flask import Flask, abort, render_template, request, jsonify

app = Flask(__name__, static_url_path='')
app.debug = True

@app.route('/projects/')
def projects():
    return 'Hit /projects'

@app.route('/projects/<path:project_name>/')
def projects_get(project_name):
    return 'Hit /projects/<project_name>'


@app.route('/projects/create/', methods=['GET', 'POST'])
def projects_create():
    return 'Hit /projects/create/'

if __name__ == '__main__':
    app.run(port=8000)
