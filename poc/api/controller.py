from flask import jsonify, request

from .. import apiWrapper

api = apiWrapper.blueprint.route


@api('/')
def index():
    return jsonify({'message': 'This is the Night\'s Watch. Welcome to Castle Black!'}), 200
