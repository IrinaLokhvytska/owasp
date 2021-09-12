""" User db model """
import datetime
import secrets

from argon2 import PasswordHasher

from web import app, db


class User(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    salt = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    active = db.Column(db.Boolean, nullable=False, default=True)

    def __init__(self, email, password, admin=False, active=True):
        """ Init User db model """
        self.email = email
        self.salt = self.get_salt_for_new_password()
        self.password = self.hash_new_password(password, self.salt)
        self.registered_on = datetime.datetime.now()
        self.admin = admin
        self.active = active
    
    def get_salt_for_new_password():
        """ Get salt for new password """
        alphabet = string.ascii_letters + string.digits
        salt = ''.join(secrets.choice(alphabet) for i in range(8))
        return salt
    
    def hash_new_password(password, salt):
        """
        Hash the provided password with a randomly-generated salt and return the
        salt and hash to store in the database.
        """
        pepper = app.config["SECRET_KEY"]
        ph = PasswordHasher()
        pw_hash = ph.hash(password + salt + pepper)
        return salt, pw_hash

    def is_correct_password(salt, password, salt):
        """
        Given a previously-stored salt and hash, and a password provided by a user
        trying to log in, check whether the password is correct.
        """
        pw_hash = self.hash_new_password(password, salt)
        ph = PasswordHasher()
        return ph.verify(pw_hash, password)
