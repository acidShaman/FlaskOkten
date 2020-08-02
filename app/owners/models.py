from app import db
from flask_login import UserMixin

pet_tag = db.Table('pet_tag',
                   db.Column('pet_id', db.Integer, db.ForeignKey('pet_model.id')),
                   db.Column('tag_id', db.Integer, db.ForeignKey('tag_model.id')))


class UserModel(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False, unique=True)
    is_admin = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f'{self.id}) {self.email}'


class OwnerModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(120), nullable=False)
    pets = db.relationship('PetModel', backref='owner', lazy='dynamic')

    def __repr__(self):
        return f'{self.id}) {self.name}'


class PetModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    type_pet = db.Column(db.String(50), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner_model.id', ondelete='CASCADE'))

    tags = db.relationship('TagModel', secondary=pet_tag, backref=db.backref('pets', lazy='dynamic'))

    def __repr__(self):
        return f'{self.id}) {self.name} - {self.type_pet}'


class TagModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    def __repr__(self):
        return f'{self.name}'




