""" User registration """
from flask.views import MethodView
from flask import (
    render_template, session, request,
    redirect, url_for
)
from flask import current_app as app
from sqlalchemy.exc import IntegrityError

from web.models.user import User
from web.models import db
from web.helpers import (
    check_login, login_page_message, check_user_permission
)
from web.forms.registration import RegistrationForm, LogInForm


class RegistrationAPI(MethodView):
    """ Endpoints for the registration API """
    def post(self):
        """ Register User """
        form = LogInForm()
        reg_form = RegistrationForm(request.form)
        if not reg_form.validate():
            return login_page_message(str(reg_form.errors))
        try:
            user = User(email=reg_form.email.data, password=reg_form.password.data)
            db.session.add(user)
            db.session.flush()
            db.session.commit()
            session.update({
                "login": True,
                "user_id": user.id
            })
        except IntegrityError:
            db.session.rollback()
            return login_page_message("The user with this email already exists")
        return redirect(url_for("home"))


class UserAPI(MethodView):
    """ Endpoints for the user API """
    @check_login
    @check_user_permission
    def get(self, user_id):
        """ Get user info """
        user = User.query.filter_by(id=user_id).first()
        return render_template(
            'user.html',
            user_id=user_id,
            user=user.get_user_info()
        )
