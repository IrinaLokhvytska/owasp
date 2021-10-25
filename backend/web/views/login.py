"""View for the /login endpoint"""
from flask.views import MethodView
from flask import (
    render_template, session, request,
    redirect, url_for, jsonify
)

from web.models import db
from web.helpers import check_login


class LoginAPI(MethodView):
    """View for the /login endpoint"""
    def get(self):
        """Get login page"""
        return render_template('login.html')

    def post(self):
        """Log in user"""
        email = request.json.get("email")
        password = request.json.get("password")
        with db.engine.connect() as connection:
            query = connection.execute(f"SELECT * FROM users WHERE email='{email}'")
            user = query.first()
        if not user:
            return jsonify({"answer": "error", "msg": "Invalid email"}), 500
        with db.engine.connect() as connection:
            query = connection.execute(
                f"SELECT * FROM users WHERE email='{email}' AND password='{password}'"
            )
            # query = connection.execute("SELECT * FROM users WHERE email=%(email)s AND password=%(password)s", {"email": email, "password": password})
            user = query.first()
        if not user:
            return jsonify({"answer": "error", "msg": "Invalid password"}), 500
        session["login"] = True
        session["user_id"] = user.id
        return jsonify({"answer": "success"}), 200


class LogoutAPI(MethodView):
    """Logout view"""
    @check_login
    def get(self):
        """Log out user"""
        session.pop("login", None)
        session.pop("user_id", None)
        return redirect(url_for("login"))
