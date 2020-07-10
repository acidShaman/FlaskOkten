from wtforms import Form, StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, length, NumberRange


class FormBP(Form):
    name = StringField('Name', [DataRequired(), length(2, 50, 'Name must be 2-50 characters long')])
    age = IntegerField('Age', [DataRequired(), NumberRange(10, 120, 'Age must be 10 - 120 characters long')])


class OwnerForm(FormBP):
    location = StringField('Location', [DataRequired(), length(2, 100, 'Address must be 2 - 100 characters long')])
    save = SubmitField('Save')



class PetForm(FormBP):
    type_pet = StringField('Type_pet', [DataRequired(), length(2, 100, 'Species name must be 2 - 100 characters long')])
    save = SubmitField('Save')

