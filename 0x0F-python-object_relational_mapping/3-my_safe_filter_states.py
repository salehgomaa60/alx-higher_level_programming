#!/usr/bin/python3
""" how to protect the script  against sql injection"""

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
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (sys.argv[4],))
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
