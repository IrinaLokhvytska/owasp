import re

from wtforms import (
    Form, StringField, PasswordField, validators,
    ValidationError
)
from wtforms.fields.html5 import EmailField


class LogInForm(Form):
    """ Validate registration form """
    email = EmailField('Email address',
        [validators.DataRequired(), validators.Email()],
        render_kw={"class": "form-control", "id": "inputEmail", "placeholder": "Email address"}
    )
    password = PasswordField('Password',
        [validators.DataRequired()],
        render_kw={"class": "form-control", "id": "inputPassword", "placeholder": "Password"}
    )


def check_password(form, field):
    special_characters = "@#$%^&+="
    if not re.fullmatch(r"[A-Za-z0-9@#$%^&+=]{8,25}", field.data):
        error_msg = f"Password should contains uppercase and lowercase letters, \
            numbers and any of the special characters: {special_characters}"
        raise ValidationError(error_msg)


class RegistrationForm(Form):
    """ Validate registration form """
    email = EmailField('Email address',
        [validators.DataRequired(), validators.Email(), validators.Length(min=4, max=35)],
        render_kw={"class": "form-control", "id": "email", "placeholder": "Email address"}
    )
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.Length(min=8, max=25),
        check_password,
        validators.EqualTo('password2', message='Passwords must match')],
        render_kw={"class": "form-control", "id": "password1", "placeholder": "Password"}
    )
    password2 = PasswordField('Confirm Password',
        [validators.DataRequired(),],
        render_kw={"class": "form-control", "id": "password2", "placeholder": "Password"}
    )
