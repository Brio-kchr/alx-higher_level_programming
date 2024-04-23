#!/usr/bin/python3
"""
This module provides a function insert_state to add
 a state to the states table of a MySQL DB
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def insert_state(mysql_username, mysql_password, database_name, state_name):
    """
    Returns the id of the newly created state Object
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            mysql_username, mysql_password, database_name
        ),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    state = State(name=state_name)
    session.add(state)
    session.commit()
    state_id = state.id
    session.close()
    return state_id


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
        state_id = insert_state(argv[1], argv[2], argv[3], "Louisiana")
        print(state_id)
