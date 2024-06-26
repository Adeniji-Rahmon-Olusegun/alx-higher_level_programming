#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument
"""

import sys
import MySQLdb

if __name__ == "__main__":

    my_db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
    )

    cursor = my_db.cursor()

    qu = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(sys.argv[4])

    cursor.execute(qu)

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    my_db.close()
