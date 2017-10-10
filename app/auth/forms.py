from flask_wtf import FlaskForm # , RecaptchaField
from wtforms import StringField, PasswordField #, BooleanField
from wtforms.validators import Required, Email, EqualTo


class LoginForm(FlaskForm):
    email       = StringField('Email Address', [Email(),
                    Required(message='Forgot your email address?')])
    password    = PasswordField('Password', [
                    Required(message='Must provide a password.')])
                    

class RegisterForm(FlaskForm):
    email               = StringField('Email Address', [Email(),
                            Required(message='Forgot your email address?')])
    password            = PasswordField('Password', [
                            Required(message='Must provide a password.')])
    password_repeat     = PasswordField('Please Repeat your Password',[
                            Required(message="You must type your password again")])                            
    name                = StringField('Name', [Required(message='Please add your name')])
    second_name         = StringField('Second Name')
    lastname            = StringField('last Name', [Required(message='Please add your Last Name')])
    second_lastname     = StringField('Second Lastname')
    rfc                 = StringField('RFC', [Required(message='Please add your RFC')])
    company             = StringField('Company', [Required(message="Please add your Company's Name")])