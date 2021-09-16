""" Helpers functions """
from functools import wraps

from flask import session, url_for, redirect

from web.models.user import User


def check_login(func):
    """ Check if user is authorized """
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if not session.get("login", False):
            return redirect(url_for("login"))
        return func(*args, **kwargs)
    return decorated_function


def check_user_role(func):
    """ Check if user has permission to view data """
    @wraps(func)
    def decorated_function(*args, **kwargs):
        user_id = session.get("user_id", "")
        user = User.query.filter_by(id=user_id).first()
        if not user.admin:
            msg = "You do not have permission"
            return {"error": msg}, 500
        return func(*args, **kwargs)
    return decorated_function


def check_user_permission(func):
    """ Check if user has permission to view data """
    @wraps(func)
    def decorated_function(*args, **kwargs):
        user_id = session.get("user_id", "")
        if user_id != kwargs["user_id"]:
            msg = "You do not have permission"
            return {"error": msg}, 500
        return func(*args, **kwargs)
    return decorated_function
