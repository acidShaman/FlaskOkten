from db import db
from crypt import bcrypt


class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    posts = db.relationship('PostModel', backref='user', lazy=True)

    def __repr__(self):
        return f'{self.id}. {self.name} - {self.email}'

    def __init__(self, name, email, password):
        self.password = bcrypt.generate_password_hash(password, 10)
        self.name = name
        self.email = email

    def json(self):
        return {'name': self.name, 'email': self.email, 'password': self.password}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_user_by_id(cls, user_id):
        return cls.query.filter_by(id=user_id).first()

    @classmethod
    def get_user_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def get_all_users(cls):
        return cls.query.all()


class PostModel(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    text = db.Column(db.String(300), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, ondelete='CASCADE')

    def __init__(self, title, text, user_id):
        self.title = title
        self.text = text
        self.user_id = user_id

    def __repr__(self):
        return {'title': self.title, 'text': self.text, 'user_id': self.user_id}

    # def json(self):
    #     return {'title': self.title, 'text': self.text, 'user_id': self.user_id}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_post_by_id(cls, post_id):
        return cls.query.filter_by(id=post_id).first()

    @classmethod
    def get_posts_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id).all()

    @classmethod
    def get_all_posts(cls):
        return cls.query.all()