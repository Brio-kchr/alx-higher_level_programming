#!/usr/bin/python3
"""
This module provides a function safe_find_state to
 retrieve states from a MySQL DB that have a specific name
 and is safe from SQL injections
"""
from sys import argv
import MySQLdb


def safe_find_state(
    mysql_username, mysql_password, database_name, state_name
):
    """
    Returns a tuple of tuples containing the data of each state
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
        "SELECT * FROM states " +
        "WHERE name LIKE BINARY '{}' ".format(state_name) +
        "ORDER BY id ASC"
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
    if n != 5:
        print(
            "Usage: {} mysql_username ".format(argv[0]) +
            "mysql_password database_name state_name"
        )
    else:
        states = safe_find_state(argv[1], argv[2], argv[3], argv[4])
        for state in states:
            print(state)
