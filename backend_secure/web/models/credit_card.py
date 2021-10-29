"""CreditCard db model"""
from cryptography.fernet import Fernet
from flask import current_app as app

from web.models import db


class CreditCard(db.Model):
    """CreditCard Model for storing credit cards related details"""

    __tablename__ = "credit_cards"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    credit_card_number = db.Column(db.String(255), nullable=False)
    credit_card_cvv = db.Column(db.Integer, nullable=False)
    credit_card_date = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __init__(self, credit_card_number, credit_card_cvv, credit_card_date, user_id):
        """Init CreditCard db model"""
        fernet = Fernet(app.config["FERNET_KEY"])
        self.credit_card_number = fernet.encrypt(bytes(credit_card_number, "UTF-8"))
        self.credit_card_cvv = fernet.encrypt(bytes(credit_card_cvv, "UTF-8"))
        self.credit_card_date = fernet.encrypt(bytes(credit_card_date, "UTF-8"))
        self.user_id = user_id

    def get_card_info(self):
        """Decrypt credit card information"""
        fernet = Fernet(app.config["FERNET_KEY"])
        return {
            "credit_card_id": self.id,
            "credit_card_number": fernet.decrypt(self.credit_card_number),
            "credit_card_cvv": fernet.decrypt(self.credit_card_cvv),
            "credit_card_date": fernet.decrypt(self.credit_card_date),
        }
