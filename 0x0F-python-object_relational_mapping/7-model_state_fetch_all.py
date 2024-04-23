#!/usr/bin/python3
"""
This module provides a function get_states to list
 all State objects from the states table from a MySQL DB
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def get_states(mysql_username, mysql_password, database_name):
    """
    Returns a tuple containing the requested state Objects
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            mysql_username, mysql_password, database_name
        ),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id)
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
        for state in get_states(argv[1], argv[2], argv[3]):
            print('{}: {}'.format(state.id, state.name))
