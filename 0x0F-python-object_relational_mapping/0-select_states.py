#!/usr/bin/python3

import sys
import MySQLdb

my_db = MYSQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
)

cursor = my_db.cursor()

cursor.execute("SHOW * FROM states")

states = cursor.fetchall()

for state in states:
    print(state)

cursor.close()
my_db.close()
