""" Initialize the application """
import logging

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from web.setup_app import create_app


app = create_app()
db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db)

root = logging.getLogger()
root.setLevel(logging.INFO)
sh = logging.StreamHandler()
sh.setLevel(logging.INFO)
root.addHandler(sh)

@app.route('/')
def index():
    return 'index'
