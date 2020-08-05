from flask import Flask
from flask_restful import Api

from config import DevConfig
from app.resources import User, Post, User1, Post1


app = Flask(__name__)
app.config.from_object(DevConfig)

api = Api(app)

api.add_resource(User, '/user', '/user/<int:user_id>')
api.add_resource(Post, '/posts', '/posts/<int:post_id>', '/user/<int:user_id>/post')
api.add_resource(User1, '/users')
api.add_resource(Post1, '/user/<int:user_id>/post')