#!/usr/bin/python3
"""
This module provides a function filter_states to list
 all State objects (with a specified substring in their name)
 from the states table from a MySQL DB
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def filter_states(mysql_username, mysql_password, database_name, substr):
    """
    Returns a tuple containing the matching state Objects
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            mysql_username, mysql_password, database_name
        ),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State)\
        .filter(State.name.contains(substr))\
        .order_by(State.id)
    session.close()
    return tuple(states)


if __name__ == "__main__":
    """
    When running as a script, use command line arguments as
     function inputs and print output to screen
    """
    from sys import argv

    n = len(argv)
    if n != 4:
        print(
            "Usage: {} mysql_username ".format(argv[0]) +
            "mysql_password database_name"
        )
    else:
        for states in filter_states(argv[1], argv[2], argv[3], 'a'):
            print('{}: {}'.format(states.id, states.name))
