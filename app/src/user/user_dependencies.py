from flask_restful import reqparse, abort, Api, Resource
from flask import Flask, jsonify, request
from src.db.DB_CONN import DB_CONN
import bcrypt

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
