from app import db

pet_tag = db.Table('pet_tag',
                   db.Column('pet_id', db.Integer, db.ForeignKey('pet_model.id')),
                   db.Column('tag_id', db.Integer, db.ForeignKey('tag_model.id')))


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

    tags = db.relationship('TagModel', secondary=pet_tag, backref=db.backref('pets', lazy='dynamic'))


class TagModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)




