from .user_dependencies import *
from flask import session


class Rooms(Resource):
    def get(self):
        user_data = [x['user_id'] for x in get_all_users()]
        try:
            generate_dummy_skills()
        except Exception as e:
            print(str(e))
        ret = get_all_data()
        
        resp = jsonify({
            "data": ret
        })
        resp.status_code = 200
        return resp

    def post(self):
        resp = jsonify({"msg": "Goodbye"})
        resp.status_code = 205
        return resp