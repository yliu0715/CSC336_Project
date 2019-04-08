from flask_restful import reqparse, abort, Api, Resource
from flask import Flask, jsonify, request
from src.db.DB_CONN import DB_CONN
import bcrypt, random

def check_credentials(params):

    DB = DB_CONN()
    username = params['username'].lower()
    hashed = bcrypt.hashpw(params['password'].encode('utf8'), bcrypt.gensalt())
    
    query = """
    SELECT * FROM USERS WHERE username = %s;
    """

    try:
        DB.cursor.execute(query, (username,))
        DB.cnx.commit()
        if (DB.cursor.fetchall()[0]['password'] == hashed):
            return True
    except:
        pass

    return False
    

def create_new_user(params):

    DB = DB_CONN()
    hashed = bcrypt.hashpw(params['password'].encode('utf8'), bcrypt.gensalt())
    username = params['username'].lower()

    query = """
    INSERT INTO USERS (username, password) VALUES (%s, %s)
    """

    try:
        DB.cursor.execute(query, (username, hashed))
        DB.cnx.commit()
    except Exception as e:
        raise e

    return True

CREATED_DUMMY_DATA = False

def get_all_data():
    DB = DB_CONN()

    query = """
    SELECT USERS.user_id, USERS.username,
            ROOMS.user_id, ROOMS.is_owner,
            ROOMS.room, ROOM.name,
            ROOM.location, ROOM.description
            FROM ROOMS NATURAL JOIN USERS
            NATURAL JOIN ROOM;
    """

    try:
        DB.cursor.execute(query)
        DB.cnx.commit()
    except Exception as e:
        raise e

    return DB.cursor.fetchall()

def get_all_users():
    global CREATED_DUMMY_DATA
    if (CREATED_DUMMY_DATA == False):
        generate_dummy_info()
        CREATED_DUMMY_DATA = True
    DB = DB_CONN()
    query = """
    SELECT user_id FROM USERS;
    """
    try:
        DB.cursor.execute(query)
        DB.cnx.commit()
    except:
        print("Error on creating dummy info")

    return DB.cursor.fetchall()

def generate_dummy_skills():
    num = random.randint(1,10)
    skills = ['Python', 'JavaScript', 'C++', 'Fortran',
                'Go', 'Ruby on Rails', 'Rust', 'CSS',
                'HTML', 'Garbage', 'Assembly', 'Fortnite',
                'Minecraft']
    random.shuffle(skills)
    DB = DB_CONN()

    room_name, desc = generate_rooms()

    createRoom = """
    INSERT INTO ROOM (name, description) VALUES (%s, %s)
    """
    createRooms = """
    INSERT INTO ROOMS (room, user_id, is_owner) VALUES (%s, %s, %s)
    """
    createSkills = """
    INSERT INTO SKILLS (name, room_name) VALUES (%s, %s)
    """

    users = get_all_users()
    random.shuffle(users)
    owner = users[0]['user_id']
    members = [x['user_id'] for x in users[1:7]]

    # Create room with description
    try:
        DB.cursor.execute(createRoom, (room_name, desc))
        DB.cnx.commit()
    except:
        pass

    # Create owner of the room
    try:
        DB.cursor.execute(createRooms, (room_name, owner, True))
        DB.cnx.commit()
    except:
        pass

    # Populate members of the room
    try:
        for i in members:
            DB.cursor.execute(createRooms, (room_name, i, False))
            DB.cnx.commit()

        # Populate the skills required to join the room
        for i in skills[:num]:
            DB.cursor.execute(createSkills, (i, room_name))
            DB.cnx.commit()
    except:
        pass

    return True

def generate_dummy_info():
    returnVal = {}
    first = ["Latchy", "Commrade", "XXx_", "gAmmY"
                "Viceroy", "Carter", "f0ker",
                "Aussie", ]
    second = ['lassy', 'pope', 'Green', 'Faker',
                'idiot', 'blackers']
    third = ['cheese', 'rice', 'redditor', 'blue',
                'jelly', 'stain', '_xXX']

    for i in range(20):
        random.shuffle(first)
        random.shuffle(second)
        random.shuffle(third)
        username = "{}{}{}".format(first[0], second[0], third[0])
        params = {
            "username": username,
            "password": "password"
        }
        try:
            create_new_user(params)
        except Exception as e:
            print("Duplicate username '{}'. Ignoring...".format(username))

    return True


def generate_rooms():

    first = ['silly', 'dark', 'chubby', 'stinky',
                'great', 'lost']
    second = ['bart', 'gem', 'fart', 'creamer',
                'jimmy', 'NULL']

    desc = []
    for i in range(10):
        random.shuffle(first)
        random.shuffle(second)
        desc.append(first[0])
        desc.append(second[0])

    room_name = "{}-{}".format(first[0],second[0])
    desc = ''.join(desc)
    return room_name, desc