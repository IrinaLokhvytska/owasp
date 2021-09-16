""" User registration """
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
from web.helpers import (
    create_user_token,
    check_user_token
)
from web.forms.registration import RegistrationForm, LogInForm


class RegistrationAPI(MethodView):
    """ Endpoints for the user API """
    def post(self):
        """ Register User """
        reg_form = RegistrationForm(request.form)
        if not reg_form.validate():
            return jsonify({"answer": "error", "msg": str(reg_form.errors)}), 500
        try:
            user = User(email=reg_form.email.data, password=reg_form.password.data)
            db.session.add(user)
            db.session.flush()
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return jsonify({"answer": "error", "msg": "The user with this email already exists"}), 500
        token = create_user_token(user.id, user.email)
        return jsonify({"answer": "success", "token": token}), 200


class UserAPI(MethodView):
    """ Endpoints for the user API """
    def get(self, user_id):
        """ Get user info """
        jwt_payload = check_user_token()
        if "answer" in jwt_payload:
            return redirect(url_for("login"))
        if jwt_payload.get("user_id") != user_id:
            return jsonify({"answer": "error", "msg": "You do not have permission"}), 500
        user = User.query.filter_by(id=user_id).first()
        credit_cards = CreditCard.query.filter_by(user_id=user_id).all()
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
            user=user.get_user_info(),
            credit_cards_info=credit_cards_info
        )
