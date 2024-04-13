#!/usr/bin/python3

"""
script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
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

    query = "SELECT * FROM states WHERE BINARY name = %s"

    cursor.execute(query, [sys.argv[4]])

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    my_db.close()
