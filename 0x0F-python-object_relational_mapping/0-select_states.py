#!/usr/bin/python3
import MySQLdb
import sys

arg = sys.argv
db = MySQLdb.connect(host="localhost", port=3306, user=arg[1],
                     password=arg[2], db=arg[3], charset="utf8")
cur = db.cursor()
cur.execute("SELECT *  FROM states ORDER BY id ASC")
rows = cur.fetchall()
for row in rows:
    print(row)
