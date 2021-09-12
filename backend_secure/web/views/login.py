from flask.views import MethodView
from flask import (
    render_template, session, request,
    redirect, url_for
)

from web.models.user import User
from web.helpers import check_login, login_page_message
from web.forms.registration import LogInForm


class LoginAPI(MethodView):
    """ View for the /login endpoint """
    def get(self):
        """ Get login page """
        form = LogInForm(request.form)
        return render_template('login.html', form=form)

    def post(self):
        """ Log in user """
        form = LogInForm(request.form)
        if not form.validate():
            return render_template('login.html', form=form)
        user = User.query.filter_by(email=form.email.data).first()
        if not user or not user.is_correct_password(form.password.data, user.salt):
            return login_page_message("Invalid Email/password combination.")
        if not user.active:
            return login_page_message(
                "Inactive account. Please wait for activation from the admin."
            )
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
