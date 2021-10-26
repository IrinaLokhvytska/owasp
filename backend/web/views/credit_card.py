"""Endpoints for the CreditCard API"""
from flask.views import MethodView
from flask import session, jsonify, request
from flask import current_app as app
from sqlalchemy.exc import IntegrityError

from web.models import db
from web.models.credit_card import CreditCard
from web.helpers import check_login


class AddCreditCardAPI(MethodView):
    """Endpoints for the add CreditCard API"""

    @check_login
    def post(self):
        """Add CreditCard item info"""
        data = request.json
        try:
            credit_card = CreditCard(
                credit_card_number=data.get("credit_card_number"),
                credit_card_cvv=data.get("credit_card_cvv"),
                credit_card_date=data.get("credit_card_date"),
                user_id=session.get("user_id"),
            )
            db.session.add(credit_card)
            db.session.flush()
            db.session.commit()
        except IntegrityError as exc:
            app.logger.error(str(exc))
            db.session.rollback()
            return jsonify({"answer": "error", "msg": str(exc)}), 500
        return jsonify({"answer": "success"}), 200


class CreditCardAPI(MethodView):
    """Endpoints for the CreditCard API"""

    @check_login
    def delete(self, card_id):
        """Delete CreditCard item info"""
        try:
            CreditCard.query.filter_by(
                id=card_id, user_id=session.get("user_id")
            ).delete()
            db.session.flush()
            db.session.commit()
        except IntegrityError as exc:
            app.logger.error(str(exc))
            db.session.rollback()
            return jsonify({"answer": "error", "msg": str(exc)}), 500
        return jsonify({"answer": "success"}), 200

    @check_login
    def put(self, card_id):
        """Update CreditCard info"""
        data = request.json
        try:
            CreditCard.query.filter_by(
                id=card_id, user_id=session.get("user_id")
            ).update(
                dict(
                    credit_card_number=data.get("credit_card_number"),
                    credit_card_cvv=data.get("credit_card_cvv"),
                    credit_card_date=data.get("credit_card_date"),
                )
            )
            db.session.flush()
            db.session.commit()
        except IntegrityError as exc:
            app.logger.error(str(exc))
            db.session.rollback()
            return jsonify({"answer": "error", "msg": str(exc)}), 500
        return jsonify({"answer": "success"}), 200
