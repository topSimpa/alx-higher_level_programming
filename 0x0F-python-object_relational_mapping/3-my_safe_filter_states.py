#!/usr/bin/python3
""" This query a database for all entry in table called states
    whose name column matches the fourt argument to this script

    Usage: ./2-filtetr_states.py <username> <passwd> <database>
            <state name>
"""


import MySQLdb
import sys

if __name__ == "__main__":
    arg = sys.argv
    db = MySQLdb.connect(host="localhost", port=3306, user=arg[1],
                         password=arg[2], db=arg[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * \
                 FROM states \
                 WHERE name = %s \
                 ORDER BY id ASC", (arg[4],))
    rows = cur.fetchall()
    for row in rows:
        if row[1] == arg[4]:
            print(row)
    cur.close()
    db.close()
