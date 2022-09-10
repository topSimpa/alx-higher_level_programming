#!/usr/bin/python3
""" This query a database for a table called states for all entry"""


import MySQLdb
import sys

if __name__ == "__main__":
    arg = sys.argv
    db = MySQLdb.connect(host="localhost", port=3306, user=arg[1],
                         password=arg[2], db=arg[3], charset="utf8")
    cur = db.cursor()
    cur.execute(f"SELECT *  FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        if row[1] == arg[4]:
            print(row)
