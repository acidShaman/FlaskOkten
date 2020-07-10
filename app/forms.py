from wtforms import Form, StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, length, NumberRange


class OwnerForm(Form):
    name = StringField('Name', [DataRequired(), length(2, 50, 'Name must be 2-50 characters long')])
    age = IntegerField('Age', [DataRequired(), NumberRange(10, 120, 'Age must be 10 - 120 years')])
    location = StringField('Location', [DataRequired(), length(2, 100, 'Address must be 2 - 100 characters long')])
    save = SubmitField('Save')


class PetForm(Form):
    name = StringField('Name', [DataRequired(), length(2, 50, 'Name must be 2-50 characters long')])
    age = IntegerField('Age', [DataRequired(), NumberRange(0, 120, 'Age must be 0 - 120 years')])
    type_pet = StringField('Type_pet', [DataRequired(), length(2, 100, 'Species name must be 2 - 100 characters long')])
    save = SubmitField('Save')

