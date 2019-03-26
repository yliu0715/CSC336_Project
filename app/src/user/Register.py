from .user_dependencies import *
from flask import session


class Register(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username')
        parser.add_argument('password')

        json_data = request.get_json(force=True)
        
        try:
            create = create_new_user(json_data)
        except Exception as e:
            response = jsonify({"msg": str(e)})
            response.status_code = 409
            return response

        response = jsonify({"msg": "Registration complete"})
        response.status_code = 201 
        return response