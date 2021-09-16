""" Initialize the application """
import logging
import traceback

from flask_migrate import Migrate
from flask import jsonify

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

@app.errorhandler(Exception)
def error_handler(exc):
    """ Error Handler """
    code = 500
    app.logger.error(traceback.format_exc())
    msg = getattr(exc, "message", str(exc))
    return jsonify({"answer": "error", "msg": msg}), code
