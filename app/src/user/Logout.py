from .user_dependencies import *
from flask import session


class Logout(Resource):
    def post(self):
        resp = jsonify({"msg": "Goodbye"})
        resp.status_code = 205
        return resp