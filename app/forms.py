from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, length, NumberRange


class FormBP(Form):
    name = StringField('name', [DataRequired(), length(2, 50, 'Name must be 2-50 characters long')])
    age = IntegerField('age', [DataRequired(), NumberRange(10, 120, 'Age must be 10 - 120 characters long')])


class ClientForm(FormBP):
    location = StringField('location', [DataRequired(), length(2, 100, 'Address must be 2 - 100 characters long')])


class PetForm(FormBP):
    type_pet = StringField('type_pet', [DataRequired(), length(2, 100, 'Species name must be 2 - 100 characters long')])
    client_id = IntegerField('client_id', [DataRequired(), NumberRange(10, 120, 'Client ID must be 10 - 120 characters long')])
