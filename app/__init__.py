from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_restful import Api
from flask_script import Manager
from flask_jwt import JWT

from app.resources import User, User1, Post, Post1
from security import authenticate, identity
from config import DevConfig
from db import db

app = Flask(__name__)
app.config.from_object(DevConfig)

jwt = JWT(app, authenticate, identity) #/auth
api = Api(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

api.add_resource(User, '/user', '/user/<int:user_id>')
api.add_resource(Post, '/posts/<int:post_id>')
api.add_resource(User1, '/users')
api.add_resource(Post1, '/user/<int:user_id>/post', '/posts')