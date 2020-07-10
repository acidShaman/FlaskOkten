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




class Pet:
    def __init__(self, name, age, type_pet):
        self.name = name
        self.age = age
        self.type_pet = type_pet

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        return str(self.__dict__)


class Owner:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location
        self.pets = []

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        return str(self.__dict__)

    def add_pet(self, name, age, type_pet):
        self.pets.append(Pet(name, age, type_pet))


