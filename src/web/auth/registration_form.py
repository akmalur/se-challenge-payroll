# src/auth/registration_form.py

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from src.common.database import Database
from src.domain.users import createUserService


class RegistrationForm(FlaskForm):
    userService = createUserService(Database)
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm_password')])
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Register')

    def validate_email(self, field):
        if self.userService.findUserByEmail(field.data):
            raise ValidationError('Email is already in use.')
