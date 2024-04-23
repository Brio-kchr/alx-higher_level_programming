#!/usr/bin/python3
"""
This module provides a function get_cities to list
 all City objects from the cities table from a MySQL DB
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def get_cities(mysql_username, mysql_password, database_name):
    """
    Returns a tuple containing tuples of the requested City Objects
     bundled with their corresponding States
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            mysql_username, mysql_password, database_name
        ),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    cities_states = session.query(City, State).join(City).order_by(City.id)
    session.close()
    return tuple(cities_states)


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
        for (city, state) in get_cities(argv[1], argv[2], argv[3]):
            print("{}: ({}) {}".format(state.name, city.id, city.name))
