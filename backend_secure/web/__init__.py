"""Initialize the application"""
import logging
import traceback

from flask_migrate import Migrate
from flask import jsonify

from web.setup_app import create_app
from web.models import db
from web.routes import add_endpoints_to_app


# Database
app = create_app()
db.init_app(app)
migrate = Migrate(app, db)

# Logging
root = logging.getLogger()
root.setLevel(logging.INFO)
sh = logging.StreamHandler()
sh.setLevel(logging.INFO)
root.addHandler(sh)


# add endpoints
add_endpoints_to_app(app)
app.debug = True


@app.errorhandler(Exception)
def error_handler(exc):
    """Error Handler"""
    code = 500
    app.logger.error(traceback.format_exc())
    msg = getattr(exc, "message", str(exc))
    return jsonify({"answer": "error", "msg": msg}), code


@app.after_request
def add_secure_headers_to_response(response):
    """Add secure headers to response"""
    # https://flask.palletsprojects.com/en/2.0.x/security/
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    return response
