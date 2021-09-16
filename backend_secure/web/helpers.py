import datetime
from functools import wraps

import jwt

from flask import session, url_for, redirect, jsonify, request
from flask import current_app as app

from web.models.user import User


def check_user_role(user_id):
    """ Check if user has permission to view data """
    user = User.query.filter_by(id=user_id).first()
    return True if user.admin else False


def create_user_token(user_id, user_email):
    """ Create token for user session """
    token = jwt.encode(
        {
            "user_id": user_id,
            "user_email": user_email
        },
        app.config["SECRET_KEY"],
        algorithm="HS256",
    )
    return token


def check_user_token():
    """ Check user session token from cookies """
    try:
        jwt_payload = jwt.decode(
            request.cookies.get('token'), app.config["SECRET_KEY"], algorithms=["HS256"]
        )
    except jwt.ExpiredSignatureError:
        return {"answer": "error", "msg": "Your token is expired"}
    except jwt.exceptions.DecodeError:
        return {"answer": "error", "msg": "Token is not valid"}
    print(request.cookies.get('token'))
    return jwt_payload
