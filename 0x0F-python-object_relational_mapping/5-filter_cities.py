#!/usr/bin/python3
"""
This module provides a function cities_of_state to
 retrieve cities belonging to a given state from a MySQL DB
"""
from sys import argv
import MySQLdb


def cities_of_state(
    mysql_username, mysql_password, database_name, state_name
):
    """
    Returns a tuple containing the requested cities
    """
    if (state_name.find("'") != -1):
        return ()
    conn = MySQLdb.connect(
        host="localhost", port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name, charset="utf8"
    )
    cur = conn.cursor()
    cur.execute(
        "SELECT `cities`.`name` FROM cities" +
        " LEFT JOIN states ON `cities`.`state_id` = `states`.`id`" +
        " WHERE `states`.`name` = '{}'".format(state_name) +
        " ORDER BY `cities`.`id` ASC;"
    )
    query_rows = cur.fetchall()
    cur.close()
    conn.close()
    items_list = [it[0] for it in query_rows]
    return (*items_list,)


if __name__ == "__main__":
    """
    When running as a script, use command line arguments as
     function inputs and print output to screen
    """
    n = len(argv)
    if n != 5:
        print(
            "Usage: {} mysql_username ".format(argv[0]) +
            "mysql_password database_name state_name"
        )
    else:
        cities = cities_of_state(argv[1], argv[2], argv[3], argv[4])
        print(", ".join(cities))
