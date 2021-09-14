from flask.views import MethodView
from flask import (
    render_template, session, request,
    redirect, url_for
)
from flask import current_app as app
from sqlalchemy.exc import IntegrityError

from web.models.user import User
from web.models import db
from web.helpers import check_login, login_page_message


class RegistrationAPI(MethodView):
    """ Endpoints for the user API """
    def post(self):
        """ Register User """
        email = request.form.get("email")
        password = request.form.get("password")
        try:
            user = User(email=email, password=password)
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
