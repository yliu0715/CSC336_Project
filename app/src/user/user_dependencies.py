from flask_restful import reqparse, abort, Api, Resource
from flask import Flask, jsonify, request
from src.db.DB_CONN import DB_CONN
import bcrypt

def check_credentials(params):

    DB = DB_CONN()

    query = """
    SELECT *
    FROM USERS
    WHERE username = '{}'
    AND password = '{}' 
    """.format(params['username'], params['password'])

    DB.custom_comms(query)
    result = DB.cursor.fetchall()
    print(result)

    return result
    

def create_new_user(params):

    DB = DB_CONN()

    hashed = params['password']
    # hashed = bcrypt.hashpw(params['password'].encode('utf8'), bcrypt.gensalt())

    table = "USERS"
    columns = "username, password"
    values = f"'{params['username']}', '{str(hashed)}'"

    try:
        DB.insert(table, columns, values)
    except Exception as e:
        raise e

    return "OK"
