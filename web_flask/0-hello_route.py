#!/usr/bin/python3
""" Start a flask app"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run('0.0.0.0')
    app.url_map.strict_slashes = False
