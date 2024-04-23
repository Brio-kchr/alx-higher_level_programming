#!/usr/bin/python3
"""
This module provides a function delete_filter_states to delete
 all State objects (with a specified substring in their name)
 from the states table from a MySQL DB
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def delete_filter_states(
    mysql_username, mysql_password, database_name, substr
):
    """
    Deletes the matching state Objects
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
        .filter(State.name.contains(substr))
    for state in states:
        session.delete(state)
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
        delete_filter_states(argv[1], argv[2], argv[3], 'a')
