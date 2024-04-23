#!/usr/bin/python3
"""
This module provides a function get_first_state to retrieve
 the first State object from the states table of a MySQL DB
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def get_first_state(mysql_username, mysql_password, database_name):
    """
    Returns the requested state Object
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            mysql_username, mysql_password, database_name
        ),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).first()
    session.close()
    return state


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
        state = get_first_state(argv[1], argv[2], argv[3])
        if state is None:
            print('Nothing')
        else:
            print('{}: {}'.format(state.id, state.name))
