from flask import request
from flask_restful import Resource, reqparse, inputs
from app.models import UserModel, PostModel


class User(Resource):
    req = reqparse.RequestParser()
    req.add_argument('name', required=True, type=inputs.regex('[A-Za-z]{3,}'), help='only characters and len min 3')
    req.add_argument('email', required=True, type=inputs.regex(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"), help='please choose another email')

    def post(self):
        data = User.req.parse_args()
        if UserModel.get_user_by_email(data['email']):
            return {'message': 'user with this email already exists'}, 400
        user = UserModel(**data)
        user.save_to_db()
        return {'message': f'user with email {user.email} created successfully!'}, 201

    def get(self, user_id):
        user = UserModel.get_user_by_id(user_id)
        if not user:
            return {'message': 'user with this id doesn\'t exist'}, 404
        return user.json(), 200

    def put(self, user_id):
        data = User.req.parse_args()
        user = UserModel.get_user_by_id(user_id)
        if not user:
            user = UserModel(**data)
            user.save_to_db()
            return {'message': f'user with this id:{user_id} hadn\'t existed and was created'}, 201
        user.name = data['name']
        user.email = data['email']
        user.save_to_db()
        return {'message': f'user with this id:{user_id} was updated successfully'}, 200

    def delete(self, user_id):
        user = UserModel.get_user_by_id(user_id)
        if not user:
            return {'message': 'user with this id doesn\'t exist'}, 404
        user.delete_from_db()
        return {'message': f'user {user.name} was deleted successfully'}, 200


class User1(Resource):
    req = reqparse.RequestParser()
    req.add_argument('name', required=True, type=inputs.regex('[A-Za-z]{3,}'), help='only characters and len min 3')
    req.add_argument('email', required=True, type=inputs.regex(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"),
                     help='please choose another email')

    def get(self):
        users = UserModel.get_all_users()
        return {"data": [user.json() for user in users]}


class Post(Resource):
    req = reqparse.RequestParser()
    req.add_argument('title', required=True, type=inputs.regex('[A-Za-z]{1,}'), help='only letters')
    req.add_argument('text', required=True, type=inputs.regex('[A-Za-z]{3,}'), help='only letters')
    req.add_argument('user_id', required=True, type=int)

    def get(self, post_id):
        post = PostModel.get_post_by_id(post_id)
        if not post:
            return {'message': f'Post with id:{post_id} doesn\'t exist!'}, 404
        return post.json(), 200

    def get(self):
        posts = PostModel.get_all_posts()
        return {"data": [post.json() for post in posts]}


class Post1(Resource):
    req = reqparse.RequestParser()
    req.add_argument('title', required=True, type=inputs.regex('[A-Za-z]{1,}'), help='only letters')
    req.add_argument('text', required=True, type=inputs.regex('[A-Za-z]{3,}'), help='only letters')
    req.add_argument('user_id', required=True, type=int)

    def get(self):
        user_id = request.args.get('userId')
        posts = PostModel.get_posts_by_user_id(user_id)
        if not posts:
            return {'message': f'This user has no posts or doesn\'t exist'}, 404
        return {'data': [post.json() for post in posts]}

    def post(self, user_id):
        data = Post1.req.parse_args()
        if user_id == data['user_id']:
            post = PostModel(**data)
            post.save_to_db()
            return {'message': 'Post created successfully!'}, 201
        return {'message': 'User with this id doesn\'t exist'}
