"""User registration"""
from flask.views import MethodView
from flask import (
    render_template, session, request, jsonify
)
from sqlalchemy.exc import IntegrityError

from web.models import db
from web.models.user import User
from web.models.credit_card import CreditCard
from web.helpers import (
    check_login, check_user_permission
)
from web.forms.registration import RegistrationForm


class RegistrationAPI(MethodView):
    """Endpoints for the user API"""
    def post(self):
        """Register User"""
        reg_form = RegistrationForm(request.form)
        if not reg_form.validate():
            return jsonify({"answer": "error", "msg": str(reg_form.errors)}), 500
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
            return jsonify(
                    {
                        "answer": "error",
                        "msg": "The user with this email already exists"
                    }), 500
        return jsonify({"answer": "success"}), 200


class UserAPI(MethodView):
    """Endpoints for the user API"""
    @check_login
    @check_user_permission
    def get(self, user_id):
        """Get user info"""
        user = User.query.filter_by(id=user_id).first()
        credit_cards = CreditCard.query.filter_by(user_id=user_id).all()
        credit_cards_info = []
        for credit_card in credit_cards:
            credit_cards_info.append(
                credit_card.get_card_info()
            )
        return render_template(
            'user.html',
            user_id=user_id,
            user=user.get_user_info(),
            credit_cards_info=credit_cards_info
        )
