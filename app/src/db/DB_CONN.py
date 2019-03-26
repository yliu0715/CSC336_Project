"""
    This class queries items from the database
"""

import mysql.connector, json, os
from mysql.connector import errorcode
import bcrypt

# from app import __location__

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'config.json')) as json_file:  
    config = json.load(json_file)


class Error(Exception):
   """Base class for other exceptions"""
   pass


class TableDoesNotExistError(Error):
   """Raised when the table doesn't exist"""
   pass


class DB_CONN:
    def __init__(self):
        self.cnx = mysql.connector.connect(**config)
        self.cursor = self.cnx.cursor(buffered=True, dictionary=True)

    def query(self, table, columns):
        try:
            cursor = self.cursor
            self.validate_input(table, columns)
            qry = ("SELECT {} FROM {};".format(columns, table))
            cursor.execute(qry)
        except Exception as e:
            comms = [table, columns]
            self.raise_error("QUERY", comms, str(e))

    def create(self, comms):
        """
            @param: 
                table: name of the table created
                columns: the columns of the table to be created
                    with the appropriate datatypes
        """
        try:
            cursor = self.cursor
            cursor.execute("{};".format(comms))
            self.cnx.commit()
        except Exception as e:
            comms = [comms]
            self.raise_error("CREATE", comms, str(e))

    def custom_comms(self, comms):
        """
            Pass custom sql commands. No validation here.
            @WARNING. DO NOT ALLOW ANYONE ELSE TO HAVE DIRECT ACCESS HERE.
        """
        try:
            cursor = self.cursor
            cursor.execute(comms)
            self.cnx.commit()
        except Exception as e:
            self.raise_error("CUSTOM_COMMS", comms, str(e))

    def insert(self, table, columns, values):
        try:
            cursor = self.cursor
            # self.validate_input({table, columns, values})
            qry = "INSERT INTO %s (%s) VALUES (%s);"
            data = (table, columns, values)
            cursor.execute(qry, data)
            self.cnx.commit()
            return True      
        except Exception as e:
            # comms = [table, columns, values]
            self.raise_error("INSERT", qry, str(e))

    def validate_input(self, **data):
        ILLEGAL_CHARS = [';-\\']
        for i in data:
            for illegal in ILLEGAL_CHARS:
                if illegal in i:
                    raise Exception("No '{}' in the input please.".format(illegal))

    def raise_error(self, area, comms, msg):
        raise Exception("Something went wrong in {}. Last command: '{}'. More about this: '{}'"
            .format(area, comms, msg))

    def check_table(self, table):
        self.validate_input(table)
        command = "SELECT 1 FROM {} LIMIT 1;".format(table)
        try:
            self.cursor.execute(command)
            self.cnx.commit()
        except:
            raise TableDoesNotExistError