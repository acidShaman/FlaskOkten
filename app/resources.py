from flask import request
from flask_restful import Resource
from flask_jwt import jwt_required
from app.models import UserModel, PostModel
from app.schemas import UserSchema, PostSchema


class User(Resource):

    @classmethod
    # @jwt_required()
    def post(cls):
        candidate = request.get_json()
        error = UserSchema().validate(candidate)
        if error:
            return {'message': error}, 400
        data = UserSchema().load(candidate)
        if UserModel.get_user_by_email(data['email']):
            return {'message': 'user with this email already exists'}, 400
        user = UserModel(**data)
        user.save_to_db()
        return {'message': f'user with email {user.email} created successfully!'}, 201

    @classmethod
    def get(cls, user_id):
        user = UserModel.get_user_by_id(user_id)
        if not user:
            return {'message': 'user with this id doesn\'t exist'}, 404
        return UserSchema().dump(user), 200

    @classmethod  # сделать так чтобы можо было изменять только одно или два поля
    @jwt_required
    def put(cls, user_id):
        candidate = request.get_json()
        error = UserSchema().validate(candidate)
        if error:
            return {'message': error}
        data = UserSchema().load(candidate)
        user = UserModel.get_user_by_id(user_id)
        if not user:
            user = UserModel(**data)
            user.save_to_db()
            return {'message': f'user with this id:{user_id} hadn\'t existed and was created'}, 201
        if data.get('name'):
            user.name = data['name']
        if data.get('email'):
            user.email = data['email']
        if data.get('password'):
            user.password = data['password']
        user.save_to_db()
        return {'message': f'user with this id:{user_id} was updated successfully'}, 200

    @classmethod
    @jwt_required()
    def delete(cls, user_id):
        user = UserModel.get_user_by_id(user_id)
        if not user:
            return {'message': 'user with this id doesn\'t exist'}, 404
        user.delete_from_db()
        return {'message': f'user {user.name} was deleted successfully'}, 200


class User1(Resource):
    @classmethod
    def get(cls):
        users = UserModel.get_all_users()
        return {"data": [UserSchema().dump(user) for user in users]}


class Post(Resource):
    @classmethod
    def get(cls, post_id):
        post = PostModel.get_post_by_id(post_id)
        if not post:
            return {'message': f'Post with id:{post_id} doesn\'t exist!'}, 404
        return PostSchema().dump(post), 200


class Post1(Resource):

    @classmethod
    def get(cls):
        user_id = request.args.get('userId')
        if user_id:
            posts = PostModel.get_posts_by_user_id(user_id)
            if not posts:
                return {'message': f'This user has no posts or doesn\'t exist'}, 404
            return {'data': [PostSchema().dump(post) for post in posts]}, 200
        posts = PostModel.get_all_posts()
        return {"data": [PostSchema().dump(post) for post in posts]}


    @classmethod
    @jwt_required
    def post(cls, user_id):
        data = Post1.req.parse_args()
        if UserModel.get_user_by_id(user_id):
            post = PostModel(**data)
            post.user_id = user_id
            post.save_to_db()
            return {'message': 'Post created successfully!'}, 201
        return {'message': 'User with this id doesn\'t exist'}
