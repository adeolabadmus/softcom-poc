from flask import jsonify

class BadRequest(Exception):
    def __init__(self, message=None):
        Exception.__init__(self)
        self.status = 400
        self.error = 'Bad Request'
        if message:
            self.message = message

    def to_json(self):
        return jsonify(self.__dict__), self.status
