""" Set up flask application """
from flask import Flask


def create_app():
    """ Create the  simple flask application """
    app = Flask(
        __name__,
        template_folder="templates",
        static_folder='ui/static'
    )
    app.config.from_pyfile('config.py')
    return app
