from flask.ext.wtf import Form # , RecaptchaField
from wtforms import TextField, PasswordField #, BooleanField
from wtforms.validators import Required, Email, EqualTo


class LoginForm(Form):
    email       = TextField('Email Address', [Email(),
                    Required(message='Forgot your email address?')])
    password    = PasswordField('Password', [
                    Required(message='Must provide a password.')])
                    

class RegisterForm(Form):
    email               = TextField('Email Address', [Email(),
                            Required(message='Forgot your email address?')])
    password            = PasswordField('Password', [
                            Required(message='Must provide a password.')])
    password_repeat     = PasswordField('Please Repeat your Password',[
                            Required(message="You must type your password again")])                            
    name                = TextField('Name', [Required(message='Please add your name')])
    second_name         = TextField('Middle Name')
    lastname            = TextField('last Name', [Required(message='Please add your Last Name')])
    second_lastname     = TextField('Second Surname')
    rfc                 = TextField('RFC', [Required(message='Please add your RFC')])
    