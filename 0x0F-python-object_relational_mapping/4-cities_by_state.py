#!/usr/bin/python3
"""
This module provides a function cities_by_state to
 retrieve cities by their states from a MySQL DB
"""
from sys import argv
import MySQLdb


def cities_by_state(mysql_username, mysql_password, database_name):
    """
    Returns a tuple of tuples containing the data of each city
    """
    conn = MySQLdb.connect(
        host="localhost", port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name, charset="utf8"
    )
    cur = conn.cursor()
    cur.execute(
        "SELECT `cities`.`id`, `cities`.`name`, `states`.`name` FROM cities" +
        " LEFT JOIN states ON `cities`.`state_id` = `states`.`id`" +
        " ORDER BY `cities`.`id` ASC;"
    )
    query_rows = cur.fetchall()
    cur.close()
    conn.close()
    return query_rows


if __name__ == "__main__":
    """
    When running as a script, use command line arguments as
     function inputs and print output to screen
    """
    n = len(argv)
    if n != 4:
        print(
            "Usage: {} mysql_username ".format(argv[0]) +
            "mysql_password database_name"
        )
    else:
        cities = cities_by_state(argv[1], argv[2], argv[3])
        for city in cities:
            print(city)
