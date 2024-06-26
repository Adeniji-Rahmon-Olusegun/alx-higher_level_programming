#!/usr/bin/python3

"""
Script that lists all cities from the database hbtn_0e_4_usa
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

    cursor.execute(
            "SELECT cities.id, cities.name, states.name\
            FROM cities\
            INNER JOIN states on cities.state_id = states.id\
            ORDER BY cities.id")

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    my_db.close()
