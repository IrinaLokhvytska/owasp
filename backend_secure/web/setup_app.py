"""Set up flask application"""
from flask import Flask
from flask_wtf.csrf import CSRFProtect


def create_app():
    """Create the  simple flask application"""
    app = Flask(
        __name__,
        template_folder="templates",
        static_folder='ui/static'
    )
    app.config.from_pyfile('config.py')
    # csrf
    csrf = CSRFProtect()
    csrf.init_app(app)
    return app
