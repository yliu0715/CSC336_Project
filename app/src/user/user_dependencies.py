from flask_restful import reqparse, abort, Api, Resource
from flask import Flask, jsonify, request
from src.db.DB_CONN import DB_CONN
import bcrypt, random

def update_user_file(param):
    username = param['username']
    firstname = param['firstname']
    lastname = param['lastname']

    DB = DB_CONN()

    query = """
    UPDATE USERS
       SET firstname = %s, lastname = %s
       WHERE username = %s;
    """

    stored_procedure = """
    CREATE PROCEDURE update_user(
        IN new_firstname VARCHAR(255),
        IN new_lastname VARCHAR(255),
        IN user VARCHAR(255)
    )
    UPDATE USERS
        SET firstname = new_firstname, lastname = new_lastname
        WHERE username = user;
    """

    try:
        DB.cursor.execute(query, (firstname, lastname, username))
        DB.cnx.commit()
        return DB.cursor.fetchall()
    except Exception as e:
        raise e

    return None

def get_rooms_info_verbose(roomname):

    DB = DB_CONN()
    # ROOMS >> ROOM >> USERS >> SKILLS
    query = """
    SELECT USERS.username, USERS.user_id,
            ROOMS.is_owner, ROOMS.room_name,
            ROOMS.user_id, ROOM.room_name,
            ROOM.location, ROOM.description,
            SKILLS.skill_name, SKILLS.room_name
        FROM ROOMS
        INNER JOIN ROOM
            ON ROOMS.room_name = ROOM.room_name
        INNER JOIN USERS
            ON ROOMS.user_id = USERS.user_id
        INNER JOIN SKILLS
            ON ROOMS.room_name = SKILLS.room_name
        WHERE ROOM.room_name = %s;
    """
    try:
        DB.cursor.execute(query, (roomname,))
        DB.cnx.commit()
        return DB.cursor.fetchall()
    except Exception as e:
        raise e

    return None

def get_user_profile(username):
    DB = DB_CONN()
    query = """
    SELECT * FROM USERS WHERE username = %s;
    """
    try:
        DB.cursor.execute(query, (username,))
        DB.cnx.commit()
        return DB.cursor.fetchall()
    except Exception as e:
        raise e

    return None

def check_credentials(params):

    DB = DB_CONN()
    username = params['username'].lower()
    password = params['password'].encode('utf8')

    query = """
    SELECT * FROM USERS WHERE username = %s;
    """

    try:
        DB.cursor.execute(query, (username,))
        DB.cnx.commit()
        hashed = DB.cursor.fetchall()[0]['password']
        if (bytearray(bcrypt.hashpw(password, hashed)) == hashed):
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

    stored_procedure = """
    CREATE PROCEDURE create_user(
        IN new_firstname VARCHAR(255),
        IN new_password VARCHAR(255)
    )
    INSERT INTO USERS (username, password) VALUES (new_firstname, new_password);
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
            ROOMS.room_name, ROOM.room_name,
            ROOM.location, ROOM.description
            FROM ROOMS INNER JOIN USERS
                ON ROOMS.user_id = USERS.user_id
            INNER JOIN ROOM
                ON ROOMS.room_name = ROOM.room_name;
    """

    try:
        DB.cursor.execute(query)
        DB.cnx.commit()
    except Exception as e:
        print("Error on get_all_data: ", end="")
        raise e

    return DB.cursor.fetchall()

def get_all_users():
    # global CREATED_DUMMY_DATA
    # if (CREATED_DUMMY_DATA == False):
    #     generate_dummy_info()
    #     CREATED_DUMMY_DATA = True
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
    INSERT INTO ROOM (room_name, description) VALUES (%s, %s)
    """

    createRoom_procedure = """
    CREATE PROCEDURE create_room(
        IN new_room_name VARCHAR(255),
        IN new_description VARCHAR(255)
    )
    INSERT INTO USERS (room_name, description) VALUES (new_room_name, new_description);
    """


    
    createRooms = """
    INSERT INTO ROOMS (room_name, user_id, is_owner) VALUES (%s, %s, %s)
    """

    createRooms_procedure = """
    CREATE PROCEDURE create_rooms(
        IN new_room_name VARCHAR(255),
        IN new_user_id INT,
        IN owner BOOLEAN
    )
    INSERT INTO USERS (room_name, user_id, is_owner) VALUES (new_room_name, new_user_id, owner);
    """



    createSkills = """
    INSERT INTO SKILLS (skill_name, room_name) VALUES (%s, %s)
    """

    createSkills_procedure = """
    CREATE PROCEDURE create_skills(
        IN new_skill_name VARCHAR(255),
        IN new_room_name VARCHAR(255)
    )
    INSERT INTO SKILLS (skill_name, room_name) VALUES (new_skill_name, new_room_name);
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
