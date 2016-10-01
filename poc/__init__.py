from utils import factory
from utils.helpers import BlueprintWrapper


def create_app():
    app = factory.create_app(__name__)
    return app


apiWrapper = BlueprintWrapper('api', __name__, '/api')
