#!/usr/bin/python3
"""
This module provides a function select_states to
 retrieve states from a MySQL DB
"""
from sys import argv
import MySQLdb


def select_states(mysql_username, mysql_password, database_name):
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
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    cur.close()
    conn.close()
    return query_rows
