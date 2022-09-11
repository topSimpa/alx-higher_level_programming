#!/usr/bin/python3
""" Lists all cities and their states in a database"""


import MySQLdb
import sys

if __name__ == "__main__":
    arg = sys.argv
    db = MySQLdb.connect(host="localhost", port=3306, user=arg[1],
                         password=arg[2], db=arg[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
                FROM cities \
                INNER JOIN states \
                ON cities.state_id = states.id \
                ORDER BY cities.id ASC"
                )
    rows = cur.fetchall()
    for row in rows:
        print(row)
