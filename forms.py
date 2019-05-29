from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField, validators

class LoginForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25), validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])
    submit = SubmitField('Sign In')
