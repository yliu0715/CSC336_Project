from .user_dependencies import *
from flask import session

class Profile(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username')

        json_data = request.get_json(force=True)

        try:
            data = get_user_profile(json_data['username'])[0]
            data.pop('password', None)
            resp = jsonify({"msg": data})
            resp.status_code = 200
        except Exception as e:
            print(e)
            resp = jsonify({"msg": "Error somewhere. Just give up"})
            resp.status_code = 400
        return resp

    def patch(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', help="Please supply username", required=True)
        parser.add_argument('firstname', help="Please supply firstname", required=True)
        parser.add_argument('lastname', help="Please supply lastname", required=True)

        json_data = request.get_json(force=True)

        try:
            data = update_user_file(json_data)
            resp = jsonify({"msg": data})
            resp.status_code = 200
        except Exception as e:
            print(e)
            resp = jsonify({"msg": "Error somewhere. Just give up"})
            resp.status_code = 400
        return resp
