import datetime

from flask.views import MethodView
from flask import (
    render_template, session, request,
    redirect, url_for, jsonify
)
from flask import current_app as app
from sqlalchemy.exc import IntegrityError

from web.models import db 
from web.models.user import User
from web.models.credit_card import CreditCard
from web.helpers import check_login


class RegistrationAPI(MethodView):
    """ Endpoints for the user API """
    def post(self):
        """ Register User """
        email = request.json.get("email")
        password = request.json.get("password")
        registered_on = datetime.datetime.now()
        admin = False
        try:
            with db.engine.connect() as connection:
                user = connection.execute(
                    f"INSERT INTO users (email, password, registered_on, admin) VALUES ('{email}', '{password}', '{registered_on}', '{admin}') RETURNING id"
                )
            session.update({
                "login": True,
                "user_id": user.fetchone()[0]
            })
        except IntegrityError:
            return jsonify({"answer": "error", "msg": "The user with this email already exists"}), 500
        return jsonify({"answer": "success"}), 200


class UserAPI(MethodView):
    """ Endpoints for the user API """
    @check_login
    def get(self, user_id):
        """ Get user info """
        # user/8;SELECT%20*%20FROM%20USERS
        with db.engine.connect() as connection:
            user = connection.execute(f"SELECT * FROM users WHERE id={user_id}").first()
            credit_cards = connection.execute(f"SELECT * FROM credit_cards WHERE user_id={user_id}").all()
        user_info = {
            "id": user.id,
            "email": user.email,
            "registered_on": user.registered_on,
            "role": "admin" if user.admin else "regular user"
        }
        credit_cards_info = []
        for credit_card in credit_cards:
            credit_cards_info.append({
                "credit_card_id": credit_card.id,
                "credit_card_number": credit_card.credit_card_number,
                "credit_card_cvv": credit_card.credit_card_cvv,
                "credit_card_date": credit_card.credit_card_date,
            })
        return render_template(
            'user.html',
            user_id=user_id,
            user=user_info,
            credit_cards_info=credit_cards_info
        )
