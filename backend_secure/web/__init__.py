""" Initialize the application """
import logging

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from web.setup_app import create_app


# Database
app = create_app()
db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db)

# Logging
root = logging.getLogger()
root.setLevel(logging.INFO)
sh = logging.StreamHandler()
sh.setLevel(logging.INFO)
root.addHandler(sh)

# csrf
csrf = CSRFProtect()
csrf.init_app(app)

@app.route('/')
def index():
    return 'index'
