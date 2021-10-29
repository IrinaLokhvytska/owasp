"""Initialize the application"""
import json
import logging
import traceback

from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask import jsonify, request, make_response

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


# csrf
csrf = CSRFProtect()
csrf.init_app(app)


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


@csrf.exempt
@app.route("/xss_atack", methods=["POST"])
def csp_report():
    app.logger.error(json.loads(str(request.data, "utf-8")))
    response = make_response()
    response.status_code = 200
    return response


@app.after_request
def add_secure_headers_to_response(response):
    """Add secure headers to response"""
    # https://flask.palletsprojects.com/en/2.0.x/security/
    # SETTINGS_CSP = {
    #     'default-src': [
    #         '\'self\'',
    #     ],
    #     'script-src': [
    #         '\'self\'',
    #         '\'sha256-pu1SeSVRQwuLmgKFdpgMzTi7ghm2F3Ldi/iw1Ff6Myc=\''
    #     ]
    # }
    # csp_header = ''
    # for directive, policies in SETTINGS_CSP.items():
    #     csp_header += f'{directive} '
    #     csp_header += ' '.join(
    #         (policy for policy in policies)
    #     )
    #     csp_header += ';'
    # csp_header += " report-uri /xss_atack"
    # response.headers["Content-Security-Policy"] = csp_header
    response.headers[
        "Strict-Transport-Security"
    ] = "max-age=31536000; includeSubDomains"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    return response
