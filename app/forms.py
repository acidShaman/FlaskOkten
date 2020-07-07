from wtforms import Form, StringField


class FormBP(Form):
    name = StringField('name')
    age = StringField('age')


class ClientForm(FormBP):
    location = StringField('location')


class PetForm(FormBP):
    type_pet = StringField('type_pet')
    client_id = StringField('client_id')
