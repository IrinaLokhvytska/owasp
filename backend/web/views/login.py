from flask.views import MethodView
from flask import (
    render_template, session, request,
    redirect, url_for
)

from web.models.user import User
from web.models import db
from web.helpers import check_login, login_page_message


class LoginAPI(MethodView):
    """ View for the /login endpoint """
    def get(self):
        """ Get login page """
        return render_template('login.html')

    def post(self):
        """ Log in user """
        email = request.form.get("email")
        password = request.form.get("password")
        with db.engine.connect() as connection:
            query = connection.execute(f"SELECT * FROM users WHERE email='{email}'")
            user = query.first()
        if not user:
            return login_page_message("Invalid email")
        with db.engine.connect() as connection:
            query = connection.execute(f"SELECT * FROM users WHERE email='{email}' AND password='{password}'")
            # query = connection.execute("SELECT * FROM users WHERE email=%(email)s AND password=%(password)s", {"email": email, "password": password})
            user = query.first()
        if not user:
            return login_page_message("Invalid password")
        session.permanent = True
        session["login"] = True
        session["user_id"] = user.id
        return redirect(url_for("home"))


class LogoutAPI(MethodView):
    """ Logout view """
    @check_login
    def get(self):
        """ Log out user"""
        session.pop("login", None)
        session.pop("user_id", None)
        return redirect(url_for("login"))
