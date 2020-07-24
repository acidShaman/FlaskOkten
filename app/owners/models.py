from app import db


class OwnerModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    location = db.Column(db.String(120))
    pets = db.relationship('PetModel', backref='owner', lazy='dynamic')


class PetModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    type_pet = db.Column(db.String(50))
    owner_id = db.Column(db.Integer, db.ForeignKey('owner_model.id'))


class TagModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)


