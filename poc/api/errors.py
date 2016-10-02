from .. import apiWrapper
from ..utils.errors import BadRequest

api = apiWrapper.blueprint


@api.errorhandler(BadRequest)
def handle_bad_request(error):
    return error.to_json()
