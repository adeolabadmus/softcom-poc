from flask import jsonify, request

from ..utils.errors import BadRequest
from .. import apiWrapper
from services import get_results

api = apiWrapper.blueprint


@api.route('/')
def index():
    return jsonify({'message': 'This is the Night\'s Watch. Welcome to Castle Black!'}), 200


@api.route('/search')
@api.route('/search/')
def search():
    query = request.args.get('query')
    if not query:
        raise BadRequest('query parameter not set')
    results = get_results(query)
    return jsonify(results), 200
