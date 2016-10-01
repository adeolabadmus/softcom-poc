from flask import jsonify, request

from ..utils.errors import BadRequest
from .. import apiWrapper

api = apiWrapper.blueprint

@api.route('/')
def index():
    return jsonify({'message': 'This is the Night\'s Watch. Welcome to Castle Black!'}), 200

@api.route('/search')
def search():
    query = request.args.get('q')
    if not query:
        raise BadRequest('query parameter not set')
    return str(query), 200
