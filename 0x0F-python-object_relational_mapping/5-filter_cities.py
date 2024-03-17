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
        """SELECT cities.name
           FROM cities
           JOIN states
           ON cities.state_id = states.id
           WHERE states.name = %(state)s
           ORDER BY cities.id ASC""",
        {"state": argv[4]},
    )

    rows = cur.fetchall()
    if rows is not None:
        print(", ".join([row[0] for row in rows]))

    cur.close()
    conn.close()
