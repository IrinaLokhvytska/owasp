""" Initialize the application """
import logging

from flask_migrate import Migrate

from web.setup_app import create_app
from web.routes import add_endpoints_to_app
from web.models import db


app = create_app()
db.init_app(app)
migrate = Migrate(app, db)

root = logging.getLogger()
root.setLevel(logging.INFO)
sh = logging.StreamHandler()
sh.setLevel(logging.INFO)
root.addHandler(sh)

# add endpoints
add_endpoints_to_app(app)
