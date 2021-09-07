""" Set up flask application """
from flask import Flask


def create_app():
    """ Create the  simple flask application """
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    return app
