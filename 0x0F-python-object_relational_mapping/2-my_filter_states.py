#!/usr/bin/python3
""" listing the  states depending on user input"""

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
    myquery = """
SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC"""
    myquery = myquery.format(sys.argv[4])
    cursor.execute(myquery)
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
