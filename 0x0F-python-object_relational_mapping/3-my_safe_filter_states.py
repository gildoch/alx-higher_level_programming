#!/usr/bin/python3
"""
script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Access to the database and get the states
    from the database.
    """
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8",
    )

    cur = conn.cursor()
    cur.execute(
        """SELECT * \
         FROM states \
         WHERE name LIKE BINARY %(name)s \
         ORDER BY states.id ASC""",
        {"name": argv[4]},
    )
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()
