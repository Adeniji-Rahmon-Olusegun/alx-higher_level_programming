#!/usr/bin/python3

"""Script that lists all states from the database hbtn_0e_0_usa"""

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

    cursor.execute("SELECT * FROM states ORDER BY states.id")

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    my_db.close()
