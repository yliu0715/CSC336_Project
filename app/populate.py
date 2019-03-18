#!/usr/bin/env python
"""
This is an example of creating and inserting test records into a database.
"""

import sys
import random
import datetime

# Run `pip install mysql-connector` or follow the instructions at
#`https://dev.mysql.com/doc/connector-python/en/connector-python-installation.html`
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": 'root',
    "password": 'changepassword',
    "host": '127.0.0.1',
    "database": 'DB1'
}

def create_random_date():
    year = random.randint(2000, 2017)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return datetime.date(year, month, day)

def create_random_name():
    last = ("Turing", "Church", "Curry", "Hopper", "Lovelace", "Allen", "Liskov")
    first = ("Allan", "Haskell", "Alonzo", "Grace", "Ada", "Frances", "Barbara")
    return " ".join((random.choice(first), random.choice(last)))

def create_random_record(num):
    for _ in range(num):
        name = create_random_name()
        date = create_random_date()
        yield (name, date)

def query(cursor):
    qry = ("SELECT Name, EmplId, HireDate FROM Test;")
    cursor.execute(qry)
    print("*" * 80)
    for (name, emplid, date) in cursor:
        print(f"{emplid} : {name}, {date}")
    print("*" * 80)

def init(cursor):
    cursor.execute("DROP TABLE IF EXISTS Test;")
    cursor.execute("CREATE TABLE Test(EmplId INTEGER PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(128), HireDate DATE);")

def create(cursor):
    for info in create_random_record(10):
        name, date, *_ = info
        qry = "INSERT INTO Test (Name, HireDate) VALUES (%s, %s);"
        cursor.execute(qry, (name, date))

def main():
    if len(sys.argv) != 2 or sys.argv[1] not in {"init", "create", "query"}:
        print(f"USAGE: {sys.argv[0]} (init|create|query)")
        sys.exit(-1)

    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        if sys.argv[1] == "init":
            init(cursor)
            # Make sure data is committed to the database
            cnx.commit()
        elif sys.argv[1] == "create":
            create(cursor)
            # Make sure data is committed to the database
            cnx.commit()
        else:
            query(cursor)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        raise err
    else:
        cnx.close()

if __name__ == '__main__':
    main()
