"""A starting demo for flask app application with basic flask syntax and modification"""
from flask import Flask

app = Flask(__name__)


@app.route('/greet')
def hello_world():
    """Return a welcome string message."""
    return '<h1>Hello World :)</h1>'


@app.route('/greet/<name>')
def greet(name=""):
    """Return a greeting string message based on 'name' args."""
    return "<h1>Hello {}</h1>".format(name)


if __name__ == '__main__':
    app.run()