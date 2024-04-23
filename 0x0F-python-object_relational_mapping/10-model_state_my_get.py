#!/usr/bin/python3
"""
This module provides a function find_state to search for
 a State object from the states table from a MySQL DB
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def find_state(mysql_username, mysql_password, database_name, state_name):
    """
    Returns the first matching state Object
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            mysql_username, mysql_password, database_name
        ),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State)\
        .filter(State.name == state_name)\
        .first()
    session.close()
    return state


if __name__ == "__main__":
    """
    When running as a script, use command line arguments as
     function inputs and print output to screen
    """
    from sys import argv

    n = len(argv)
    if n != 5:
        print(
            "Usage: {} mysql_username ".format(argv[0]) +
            "mysql_password database_name state_name"
        )
    else:
        state = find_state(argv[1], argv[2], argv[3], argv[4])
        if state is None:
            print('Not found')
        else:
            print(state.id)
