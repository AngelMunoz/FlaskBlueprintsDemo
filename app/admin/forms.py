from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import Required, NumberRange, Optional


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