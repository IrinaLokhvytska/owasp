from wtforms import Form, StringField, PasswordField, validators
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

class RegistrationForm(Form):
    """ Validate registration form """
    first_name = StringField('First Name', [validators.Length(min=4, max=25)])
    last_name = StringField('Last Name', [validators.Length(min=4, max=25)])
    email = EmailField('Email address', [validators.Length(min=6, max=35)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('password2', message='Passwords must match')
    ])
    password2 = PasswordField('Confirm Password')
