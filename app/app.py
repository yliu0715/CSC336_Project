from src.common import *
from src.user.user_dependencies import *

from src.db.DB_CONN import DB_CONN
app = Flask(__name__)
CORS(app)
api = Api(app)

### The Routes

from src.user.Register import Register
# from src.user.Login import Login
# from src.user.Logout import Logout

##
## Actually setup the Api resource routing here
##
api.add_resource(Register, '/')

from src.settings import *

if __name__ == '__main__':
    app.run(debug=True)