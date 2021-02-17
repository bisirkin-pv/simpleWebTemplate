from flask_restplus import Namespace, Resource
from flask import request
from .models.user_model import user, user_action
from apis.utilites import validator
from core.model.UserInstance import UserInstance

user_instance = UserInstance()
api = Namespace('users', description='Users related operations')
user_model = api.model('User', user)
user_action = api.model('UserAction', user_action)


@api.route('/')
class UserRootResource(Resource):
    @api.doc(description='Get user list')
    @api.marshal_list_with(user_model)
    def get(self):
        return user_instance.get_list()

    @api.doc(description='Create new user')
    @api.expect(user_action)
    @api.response(400, 'Validation error')
    @api.marshal_with(user_model, code=201, description='Object created')
    def post(self):
        data = request.json or request.args
        if validator(user_action, data):
            return {}, 400
        return user_instance.create(data)


@api.route('/<id>')
@api.doc(params={'id': 'User Id'})
class UserResource(Resource):
    @api.doc(description='Get user', model=user_model)
    def get(self, id):
        return user_instance.get(id)

    @api.doc(description='Update user',
             model=user_model,
             body=user_action)
    @api.response(400, 'Validation error')
    def put(self, id):
        data = request.json or request.args
        if user_instance.update(id, data):
            return {}
        return {}, 400

    @api.doc(description='Delete user',
             responses={
                 200: 'Success',
                 404: 'User not found'
             })
    def delete(self, id):
        if user_instance.delete(id):
            return {}
        return {}, 404

