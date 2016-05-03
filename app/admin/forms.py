from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, IntegerField, \
                    SelectField
from wtforms.validators import Required, NumberRange, Optional, Email

class NewSubsidiaryForm(Form):
    name = StringField('Name', [Required(message="Please add your Company's Name")])
    street = StringField('Street', [Required(message="Please add your Company's Name")])
    suburb = StringField('Suburb', [Required(message="Please add your Company's Name")])
    ext_number = IntegerField('Exterior Number', [Required(message="Please supply the exterior number")])
    interior_number =IntegerField('Interior Number',[Required(message="Please supply the interior number")])
    postal_code = IntegerField('Postal Code',[Required(message="Please supply your postal code")])
    city = StringField('City', [Required(message="Please add your Company's Name")])
    country = StringField('Country', [Required(message="Please add your Company's Name")])
    
class EditSubsidiaryForm(Form):
    name = StringField('Name', [Optional()])
    street = StringField('Street', [Optional()])
    suburb = StringField('Suburb', [Optional()])
    ext_number = IntegerField('Exterior Number', [Optional()])
    interior_number =IntegerField('Interior Number', [Optional()])
    postal_code = IntegerField('Postal Code', [Optional()])
    city = StringField('City', [Optional()])
    country = StringField('Country', [Optional()])
    
class EditCompanyForm(Form):
    new_name = StringField('Email Address', [Required(message='Please add the new name of the company')])
    

class NewEmployeeForm(Form):
    email = StringField('Email Address', [Email(),Required(message="Please write the email.")])
    password = PasswordField('Password', [Required(message="Write the password")])
    password_repeat = PasswordField("Please Repeat your password", [Required(message="Write the password again please")])
    name = StringField('Name', [Required(message="Please add the Name")])
    second_name = StringField('Second Name', [Optional()])
    lastname =StringField('Last Name',[Required(message="Please write the last name")])
    second_lastname = StringField('Second Last Name',[Optional()])
    rfc = StringField('RFC', [Required(message="Please add the RFC")])
    job_name = StringField('job name', [Required(message="Please add the job's Name")])
    subsidiary_id = SelectField('Subsidiary Name',[Required(message="Please select the subsidiary")], choices=[], coerce=int)
    
class EditEmployeeForm(Form):
    email = StringField('Email Address', [Optional()])
    password = PasswordField('Password', [Optional()])
    password_repeat = PasswordField("Repeat the Password", [Optional()])
    name = StringField('Name', [Optional()])
    second_name = StringField('Second Name', [Optional()])
    lastname =StringField('Last Name', [Optional()])
    second_lastname = StringField('Second Last Name', [Optional()])
    rfc = StringField('RFC', [Optional()])
    job_name = StringField('job name', [Optional()])
    subsidiary_id = SelectField('Subsidiary Name',  [Optional()], choices=[], coerce=int)
    