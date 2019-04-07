#### Load Database Engine:
from .DB_CONN import DB_CONN
import time, os

APP_MODE = os.getenv('DEBUG', True)

try:
    DB = DB_CONN()
except Exception as e:
    raise e

comms = {}

#### Loading the USER TABLE DB
comms['users'] = """
CREATE TABLE IF NOT EXISTS USERS (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARBINARY(255) NOT NULL
);
"""

#### Loading the Rooms TABLE DB
comms['room_info'] = """
CREATE TABLE IF NOT EXISTS ROOM (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255),
    location VARCHAR(255),
    description TEXT,
    required_skills VARCHAR(255),
    PRIMARY KEY(id)
);
"""

comms['skills'] = """
CREATE TABLE IF NOT EXISTS SKILLS (
    name VARCHAR(255) NOT NULL,
    programming_language BOOLEAN
);
"""

comms['rooms_to_skills'] = """
CREATE TABLE IF NOT EXISTS rooms_to_skills (
    language VARCHAR(255) NOT NULL,
    room_id INT NOT NULL,
    FOREIGN KEY (room_id) REFERENCES ROOM (id),
    PRIMARY KEY(language)
);
"""

#### Loading the Rooms TABLE DB
comms['rooms'] = """
CREATE TABLE IF NOT EXISTS ROOMS (
    room_id INT NOT NULL,
    member_id INT,
    is_owner BOOLEAN DEFAULT 0,

    FOREIGN KEY (member_id) 
        REFERENCES USERS (id)
        ON DELETE SET NULL
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
    DB.create("DROP TABLE IF EXISTS USERS;")

def query_sample():
    DB.custom_comms(sample_insert)
    DB.custom_comms(sample_query)
    result = [x for x in DB.cursor.fetchall()]
    # Convert to string
    print("[DEBUG]: Inserting and querying test account... ", end="")
    if(result[0]['username'] == 'test1' and result[0]['password'].decode('utf-8') == 'testpass'):
        print(result[0])
        print("OK\n")

try:
    if (not APP_MODE):
        print("\n[DEBUG]: Dropped a previous user tables system... ", end="")
        drop_table()
        print("OK ")
        DB.create(comms['users'])
        query_sample()
    print("\n[INFO]: Checking/creating user tables system... ")
    for key, val in comms.items():
        DB.create(val)
        print("\t{} done.".format(key))
    print("done.", end="\n")
except Exception as e:
    raise e

print("[INFO]: No issues found with database setup.\n")