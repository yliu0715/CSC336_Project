from flask import Flask, jsonify, request
from flask_cors import CORS
import os, sys

#### Structuring the path to access all python files

absFilePath = os.path.abspath(__file__)
fileDir = os.path.dirname(os.path.abspath(__file__))
parentDir = os.path.dirname(fileDir)

user_dir = os.path.join(parentDir, 'user')
db_dir = os.path.join(parentDir, 'db')

sys.path.append(user_dir) 
sys.path.append(db_dir) 

#### Loading database test

import src.db.load_db