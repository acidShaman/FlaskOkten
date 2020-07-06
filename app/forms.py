from wtforms import Form, StringField


class FormBP(Form):
    name = StringField('name')
    age = StringField('age')


class ClientForm(FormBP):
    location = StringField('location')


class PetForm(FormBP):
    species = StringField('species')
