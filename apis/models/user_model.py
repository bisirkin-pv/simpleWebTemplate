from flask_restplus import fields
from flask_restplus import Api, Resource, fields, reqparse, inputs

user = {
    'id': fields.String(required=True, description='The user identifier'),
    'name': fields.String(description='The name', required=True),    
    'email': fields.String(description='The email', required=True),
    'age': fields.Integer(description='The user age', min=0),
}

user_action = {    
    'name': fields.String(description='The name', required=True),    
    'email': fields.String(description='The email', required=True),
    'age': fields.Integer(description='The user age', min=0),
}


parser_user = reqparse.RequestParser()
parser_user.add_argument('name', type=str, required=True)
parser_user.add_argument('email', type=str, required=True)
parser_user.add_argument('age', type=int, required=False)