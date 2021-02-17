from flask_restplus import Api
from flask import Blueprint

from .rpc import api as ns1
from .user import api as ns2

blueprint = Blueprint('api', __name__, url_prefix='/api')

api = Api(
    blueprint,
    doc='/doc/',
    title='My Title',
    version='1.0',
    description='A description',
    # All API metadatas
)

api.add_namespace(ns1)
api.add_namespace(ns2)