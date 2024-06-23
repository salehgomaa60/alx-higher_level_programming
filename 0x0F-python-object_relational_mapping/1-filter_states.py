#!/usr/bin/python3
""" listing states in ascending order dependent on id"""

import MySQLdb
import sys


def main():
    db = MySQLdb.connect(
          user=sys.argv[1],
          host="localhost",
          port=3306,
          password=sys.argv[2],
          db=sys.argv[3]
          )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    results = cursor.fetchall()
    for row in results:
        if row[1].startswith("N"):
            print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
