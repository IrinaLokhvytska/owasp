from wtforms import Form, StringField, PasswordField, validators


class LogInForm(Form):
    """ Validate registration form """
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [validators.DataRequired()])

class RegistrationForm(Form):
    """ Validate registration form """
    first_name = StringField('First Name', [validators.Length(min=4, max=25)])
    last_name = StringField('Last Name', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('password2', message='Passwords must match')
    ])
    password2 = PasswordField('Repeat Password')
