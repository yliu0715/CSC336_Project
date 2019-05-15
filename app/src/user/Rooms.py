from .user_dependencies import *
from flask import session


class Rooms(Resource):
    def get(self):
        user_data = [x['user_id'] for x in get_all_users()]
        try:
            # generate_dummy_skills() 
            resp = jsonify({ "msg": get_all_data() })
            resp.status_code = 200
        except Exception as e:
            print(str(e))
            resp = jsonify({ "msg": "Error in the get req. Something something" })
            resp.status_code = 400
        return resp

class RoomsGetOne(Resource):
    def get(self, roomname):
        try:
            data = get_rooms_info_verbose(roomname)
            resp = jsonify({"msg": data})
            resp.status_code = 200
        except Exception as e:
            print("RoomsGetOne:" + e)
            data = "Error in the query. Check your POST request."
            resp = jsonify({"msg": data})
            resp.status_code = 400
        return resp

class RoomsGetInfo(Resource):
    def get(self, roomname):
        try:
            data = get_rooms_info_verbose(roomname)
            resp = jsonify({"msg": data})
            resp.status_code = 200
        except Exception as e:
            print(e)
            data = "Error in the query. Check you GET request."
            resp = jsonify({"msg": data})
            resp.status_code = 400

        return resp
