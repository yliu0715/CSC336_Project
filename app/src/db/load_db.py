#### Load Database Engine:
from .DB_CONN import DB_CONN
import time, os

APP_MODE = os.getenv('DEBUG', False)

try:
    DB = DB_CONN()
except Exception as e:
    raise e

comms = {}

#### Loading the USER TABLE DB
comms['users'] = """
CREATE TABLE IF NOT EXISTS USERS (
    user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    firstname VARCHAR(255),
    lastname VARCHAR(255),
    password VARBINARY(255) NOT NULL
);
"""


#### Loading the Rooms TABLE DB
comms['room_info'] = """
CREATE TABLE IF NOT EXISTS ROOM (
    room_name VARCHAR(255) PRIMARY KEY,
    location VARCHAR(255),
    description TEXT
);
"""

comms['skills'] = """
CREATE TABLE IF NOT EXISTS SKILLS (
    skill_name VARCHAR(255) NOT NULL,
    room_name VARCHAR(255),
    FOREIGN KEY (room_name) REFERENCES ROOM (room_name)
);
"""

#### Loading the Rooms TABLE DB
comms['rooms'] = """
CREATE TABLE IF NOT EXISTS ROOMS (
    room_name VARCHAR(255),
    user_id INT,
    is_owner BOOLEAN DEFAULT 0,

    FOREIGN KEY (room_name) REFERENCES ROOM (room_name),
    FOREIGN KEY (user_id) 
        REFERENCES USERS (user_id)
);
"""

sample_insert = """
INSERT INTO USERS (username, password) VALUES ('test1', 'testpass')
"""

sample_query = """
SELECT *
FROM USERS
WHERE username = 'test1'
AND password = 'testpass'
"""

def drop_table():
    tables = ['SKILLS', 'ROOMS_TO_SKILLS', 'ROOMS', 'ROOM', 'USERS']
    for i in tables:
        DB.create("DROP TABLE IF EXISTS {};".format(i))
    print("Dropped all tables.")

def query_sample():
    DB.create(sample_insert)
    DB.create(sample_query)
    result = [x for x in DB.cursor.fetchall()]
    # Convert to string
    print("[DEBUG]: Inserting and querying test account... ", end="")
    if(result[0]['username'] == 'test1' and result[0]['password'].decode('utf-8') == 'testpass'):
        print(result[0])
        print("OK\n")

try:
    if (APP_MODE):
        print("\n[DEBUG]: Dropped a previous user tables system... ", end="")
        drop_table()
        print("OK ")
        DB.create(comms['users'])
        query_sample()
    print("[INFO]: Checking/creating user tables system... ")
    for key, val in comms.items():
        DB.create(val)
        print("\t{} done.".format(key))
    print("done.", end="\n")
    print("[INFO]: No issues found with database setup.\n")
except Exception as e:
    print("\n[WARN]: {}\n".format(str(e)))
