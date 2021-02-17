from flask_restplus import Namespace, Resource, fields
from core.rpc.RpcMethods import RpcMethods
from flask import request
import json
import inspect

api = Namespace('rpc', description='RPC related operations')

rpc_request = api.model('RpcRequest', {
    'id': fields.String(required=True, description='Unique Id request'),
    'method': fields.String(required=True, description='Call method'),
    'data': fields.String(description='JSON data for method'),
})

rpc_response = api.model('RpcResponse', {
    'id': fields.String(required=True, description='Unique Id request'),    
    'data': fields.String(description='JSON data for method'),
})


@api.route('/')
class PrcResource(Resource):
    @api.marshal_with(rpc_response)   
    @api.expect(rpc_request)
    def post(self):
        req_data = request.json
        method_to_call = getattr(RpcMethods, req_data['method'])
        param = json.loads(req_data['data'])
        result = method_to_call(**param)
        return {'id': req_data['id'], 'data': result}

    @api.doc(description='Get all available rpc method')
    @api.marshal_with(rpc_response)
    def get(self):
        methods = inspect.getmembers(RpcMethods, predicate=inspect.isfunction)
        data = [{method[0]: method[1].__doc__} for method in methods]
        return {'id': 0, 'data': data}
