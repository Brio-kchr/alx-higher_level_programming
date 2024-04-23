#!/usr/bin/python3
"""
This module provides a function update_state to change the name of
 a state (of known id) in the states table of a MySQL DB
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def update_state(
    mysql_username, mysql_password, database_name, state_id, state_name
):
    """
    Updates the name of a state whose id is provided
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            mysql_username, mysql_password, database_name
        ),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.id == state_id).first()
    state.name = state_name
    session.commit()
    session.close()


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
        update_state(argv[1], argv[2], argv[3], 2, "New Mexico")
