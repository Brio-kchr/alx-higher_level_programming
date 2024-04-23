#!/usr/bin/python3
"""
This module provides a function find_state to
 retrieve states from a MySQL DB that have a specific name
"""
from sys import argv
import MySQLdb


def find_state(
    mysql_username, mysql_password, database_name, state_name
):
    """
    Returns a tuple of tuples containing the data of each state
    """
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
