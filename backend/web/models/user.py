"""User db model"""
import datetime

from sqlalchemy.sql import func

from web.models import db


class User(db.Model):
    """User Model for storing user related details"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False, default=func.now())
    admin = db.Column(db.Boolean, nullable=False, default=False)
    todos = db.relationship("ToDo", backref="users", lazy=True)
    credit_cards = db.relationship("CreditCard", backref="users", lazy=True)

    def __init__(self, email, password, admin=False):
        """Init User db model"""
        self.email = email
        self.password = password
        self.registered_on = datetime.datetime.now()
        self.admin = admin

    def get_user_info(self):
        """Get user info"""
        return {
            "id": self.id,
            "email": self.email,
            "registered_on": self.registered_on,
            "role": "admin" if self.admin else "regular user",
            "password": self.password,
        }
