from .user_dependencies import *
from flask import session


class Login(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username')
        parser.add_argument('password')

        json_data = request.get_json(force=True)
        
        try:
            res = check_credentials(json_data)
        except Exception as e:
            print(str(e))
            response = jsonify({"msg": "Wrong user/pass"})
            response.status_code = 401
            return response

        if (res):
            response = jsonify({"msg": "Logged in."})
            response.status_code = 200
            return response
        else:
            response = jsonify({"msg": "Wrong user/pass"})
            response.status_code = 401
            return response