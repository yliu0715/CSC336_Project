#### Load Database Engine:
from .DB_CONN import DB_CONN
import time, os

APP_MODE = os.getenv('DEBUG', True)

try:
    DB = DB_CONN()
except Exception as e:
    raise e

#### Loading the USER TABLE DB
comms = """
CREATE TABLE IF NOT EXISTS USERS (
    username VARCHAR(255) NOT NULL,
    password VARBINARY(255) NOT NULL,
    PRIMARY KEY (username)
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
    result = [x for x in DB.cursor.fetchall()[0]]
    # Convert to string
    result[1] = result[1].decode('utf-8')
    print("[DEBUG]: Inserting and querying test account... ", end="")
    if(result[0] == 'test1' and result[1] == 'testpass'):
        print("OK\n")

try:
    if (APP_MODE):
        print("\n[DEBUG]: Dropped a previous user tables system... ", end="")
        drop_table()
        print("OK ")
        DB.create(comms)
        query_sample()
    print("[INFO]: Checking/creating user tables system... ", end="")
    DB.create(comms)
    print("done.", end="\n")
except Exception as e:
    raise e

print("[INFO]: No issues found with database setup.\n")