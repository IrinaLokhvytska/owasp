""" Login, logout, render login page """
from flask.views import MethodView
from flask import (
    render_template, session, request,
    redirect, url_for, jsonify,
    make_response
)
from flask import current_app as app

from web.models.user import User
from web.models import db
from web.helpers import check_user_token, create_user_token
from web.forms.registration import LogInForm, RegistrationForm


class LoginAPI(MethodView):
    """ View for the /login endpoint """
    def _make_user_inactive_for_max_login_failure(self, user):
        """ Make user inactive for the max login failure """
        if session.get("login_attempt", 0) >= app.config["MAX_LOGIN_FAILURE"]:
            user.active = False
            db.session.flush()
            db.session.commit()
            app.logger.error(f"{user.email} has reached the maximum sign in attempts.")

    def get(self):
        """ Get login page """
        form = LogInForm()
        reg_form = RegistrationForm()
        return render_template('login.html', form=form, reg_form=reg_form)

    def post(self):
        """ Log in user """
        form = LogInForm(request.form)
        if not form.validate():
            return jsonify({"answer": "error", "msg": str(form.errors)}), 500
        user = User.query.filter_by(email=form.email.data).first()
        login_error_msg = "Invalid Email/password combination."
        if not user:
            return jsonify({"answer": "error", "msg": login_error_msg}), 500
        if not user.active:
            return jsonify(
                {
                    "answer": "error",
                    "msg": "You’ve reached the maximum sign in attempts. Please contact the admin for activation."
                }), 500
        self._make_user_inactive_for_max_login_failure(user)
        if not user.is_correct_password(form.password.data, user.salt):
            session["login_attempt"] = session.get('login_attempt', 0) + 1
            return jsonify({"answer": "error", "msg": login_error_msg}), 500
        session.pop("login_attempt", None)
        token = create_user_token(user.id, user.email)
        return jsonify({"answer": "success", "token": token}), 200


class LogoutAPI(MethodView):
    """ Logout view """
    def get(self):
        """ Log out user """
        return redirect(url_for("login"))
