#!/usr/bin/python3

"""
Script that takes in the name of a state as an argument
and lists all cities of that state,
using the database hbtn_0e_4_usa
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
            WHERE states.name = %s\
            ORDER BY cities.id", [sys.argv[4]])

    states = cursor.fetchall()

    corr_cities = []

    for state in states:
        corr_cities.append(state)
    print(", ".join(corr_cities))

    cursor.close()
    my_db.close()
