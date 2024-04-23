#!/usr/bin/python3
"""
This module provides a function insert_city_state to add
 a city and its state to the appropriate tables of a MySQL DB
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


def insert_city_state(
    mysql_username, mysql_password, database_name, city_name, state_name
):
    """
    Returns the newly created city Object
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            mysql_username, mysql_password, database_name
        ),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    city = City(name=city_name, state=State(name=state_name))
    session.add(city)
    session.commit()
    session.close()
    return city


def create_tables(mysql_username, mysql_password, database_name):
    """
    Creates the tables in the database
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            mysql_username, mysql_password, database_name
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)


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
        create_tables(argv[1], argv[2], argv[3])
        insert_city_state(
            argv[1], argv[2], argv[3],
            "San Francisco", "California"
        )
