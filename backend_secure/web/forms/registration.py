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

def validate_strong_password(form, field):
    """ Check if password is strong """
    special_characters = "@#$%^&+="
    validation_error = "Password must contain:"
    password_checks = (
        (re.compile(r"[a-z]+"), "atleast one lowercase character,"),
        (re.compile(r"[A-Z]+"), "atleast one uppercase character,"),
        (re.compile(r"[0-9]+"), "atleast one digit character,"),
        (
            re.compile(r"[@#$%^&+=]+"),
            f"atleast one of these special characters: {special_characters}."
        )
    )
    strong_password = True
    for (check, error_msg) in password_checks:
        if not check.findall(field.data):
            strong_password = False
            validation_error = f"{validation_error} {error_msg}"
    if not strong_password:
        raise ValidationError(validation_error)


class RegistrationForm(Form):
    """ Validate registration form """
    email = EmailField('Email address',
        [validators.DataRequired(), validators.Email(), validators.Length(min=4, max=35)],
        render_kw={"class": "form-control", "id": "email", "placeholder": "Email address"}
    )
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.Length(min=8, max=25),
        validate_strong_password,
        validators.EqualTo('password2', message='Passwords must match')],
        render_kw={"class": "form-control", "id": "password1", "placeholder": "Password"}
    )
    password2 = PasswordField('Confirm Password',
        [validators.DataRequired(),],
        render_kw={"class": "form-control", "id": "password2", "placeholder": "Password"}
    )
