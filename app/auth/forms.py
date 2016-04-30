from flask.ext.wtf import Form # , RecaptchaField
from wtforms import StringField, PasswordField #, BooleanField
from wtforms.validators import Required, Email, EqualTo


class LoginForm(Form):
    email       = StringField('Email Address', [Email(),
                    Required(message='Forgot your email address?')])
    password    = PasswordField('Password', [
                    Required(message='Must provide a password.')])
                    

class RegisterForm(Form):
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