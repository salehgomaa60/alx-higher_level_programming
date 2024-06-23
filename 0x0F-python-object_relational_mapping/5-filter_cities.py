#!/usr/bin/python3
""" a script listing cities by states"""

import MySQLdb
import sys


def main():
    db = MySQLdb.connect(
          user=sys.argv[1],
          host="localhost",
          port=3306,
          password=sys.argv[2],
          database=sys.argv[3]
    )
    cursor = db.cursor()
    query = """
    SELECT c.id, c.name
    FROM cities c
    JOIN states s ON c.state_id = s.id
    WHERE s.name = %s
    ORDER BY c.id ASC
    """
    cursor.execute(query, (sys.argv[4],))
    results = cursor.fetchall()
    print(", ".join([row[1] for row in results]))
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
