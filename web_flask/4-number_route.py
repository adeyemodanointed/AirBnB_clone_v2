#!/usr/bin/python3
""" Start a flask app"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    """Return string when route '/' is queried"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Return string when route /hbnb is queried"""
    return 'HBNB'


@app.route('/c/<string:text>')
def cisfun(text):
    """Return C with the sring passed"""
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<string:text>')
def python_route(text='is cool'):
    """Return Python with the string passed"""
    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:n>')
def number_route(n):
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run('0.0.0.0')
    app.url_map.strict_slashes = False
