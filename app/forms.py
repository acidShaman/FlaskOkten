import wt as wt
from wtforms import Form, StringField, IntegerField, SubmitField, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, length, NumberRange
from .owners.models import TagModel

tags = [(tag.id, tag.name) for tag in TagModel.query.all()]


class OwnerForm(Form):
    name = StringField('Name', [DataRequired(), length(2, 50, 'Name must be 2-50 characters long')])
    age = IntegerField('Age', [DataRequired(), NumberRange(10, 120, 'Age must be 10 - 120 years')])
    location = StringField('Location', [DataRequired(), length(2, 100, 'Address must be 2 - 100 characters long')])
    gender = StringField('Gender', [DataRequired(), length(4, 20, 'Please choose your gender')])
    save = SubmitField('Save')


class PetForm(Form):
    name = StringField('Name', [DataRequired(), length(2, 50, 'Name must be 2-50 characters long')])
    age = IntegerField('Age', [DataRequired(), NumberRange(0, 120, 'Age must be 0 - 120 years')])
    type_pet = StringField('Type_pet', [DataRequired(), length(2, 100, 'Species name must be 2 - 100 characters long')])
    # tags = QuerySelectField(query_factory=TagModel.objects.all(),
    #                         get_pk=lambda a: a.id,
    #                         get_label=lambda a: a.name)
    tag = SelectField('Tags', choices=tags, coerce=int)
    save = SubmitField('Save')


class TagForm(Form):
    name = StringField('Name', [DataRequired(), length(2, 50, 'Tag must be 2-50 characters long')])
    save = SubmitField('Save')

