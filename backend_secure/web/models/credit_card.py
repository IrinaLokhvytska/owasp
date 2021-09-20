"""CreditCard db model"""
from web.models import db


class CreditCard(db.Model):
    """CreditCard Model for storing credit cards related details"""
    __tablename__ = "credit_cards"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    credit_card_number = db.Column(db.String(255), nullable=False)
    credit_card_cvv = db.Column(db.Integer, nullable=False)
    credit_card_date = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, credit_card_number, credit_card_cvv, credit_card_date, user_id):
        """Init CreditCard db model"""
        self.credit_card_number = credit_card_number
        self.credit_card_cvv = credit_card_cvv
        self.credit_card_date = credit_card_date
        self.user_id = user_id
