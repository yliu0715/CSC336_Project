from src.common import *
from src.user.user_dependencies import *

from src.db.DB_CONN import DB_CONN
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
CORS(app)
api = Api(app)

### The Routes

from src.user.Register import Register
from src.user.Rooms import Rooms, RoomsGetInfo
from src.user.Login import Login
from src.user.Logout import Logout
from src.user.Profile import Profile

##
## Actually setup the Api resource routing here
##
api.add_resource(Rooms, '/rooms')
api.add_resource(Register, '/user/register')
api.add_resource(Login, '/user/login')
api.add_resource(Logout, '/user/logout')
api.add_resource(RoomsGetInfo, '/rooms/<string:roomname>')
api.add_resource(Profile, '/user/profile')

from src.settings import *

if __name__ == '__main__':
    app.run(debug=True)