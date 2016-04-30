from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import Required, NumberRange


class NewSubsidiaryForm(Form):
    name = StringField('Company', [Required(message="Please add your Company's Name")])
    street = StringField('Company', [Required(message="Please add your Company's Name")])
    suburb = StringField('Company', [Required(message="Please add your Company's Name")])
    ext_number = IntegerField('Exterior Number',[
                               NumberRange(message="The number must be within 1 and 10 range",
                               min=1, max=10),
                               Required(message="Please supply the exterior number")])
    interior_number =IntegerField('Interior Number',[
                               NumberRange(message="The number must be within 1 and 10 range",
                               min=1, max=10),
                               Required(message="Please supply the interior number")])
    postal_code = IntegerField('Postal Code',[
                               NumberRange(message="The number must be within 1 and 10 range",
                               min=1, max=10),
                               Required(message="Please supply your postal code")])
    city = StringField('Company', [Required(message="Please add your Company's Name")])
    country = StringField('Company', [Required(message="Please add your Company's Name")])
    
    
class EditCompanyForm(Form):
    new_name = StringField('Email Address', [Required(message='Please add the new name of the company')])