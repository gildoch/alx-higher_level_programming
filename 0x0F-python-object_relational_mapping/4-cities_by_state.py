#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    """Query for cities in the database"""
    conn = MySQLdb.connect(
        host="localhost", port=33061, user=argv[1], passwd=argv[2], db=argv[3]
    )
    cur = conn.cursor()
    cur.execute(
        """SELECT cities.id, cities.name, states.name
           FROM cities
           JOIN states
           ON cities.state_id = states.id
           ORDER BY cities.id ASC"""
    )

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()
