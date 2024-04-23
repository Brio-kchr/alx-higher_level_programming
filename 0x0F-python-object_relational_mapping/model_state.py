#!/usr/bin/python3
"""
This module provides a class State which is an ORM model
"""
from sqlalchemy import Column, Integer, String
from model_city import Base


class State(Base):
    """
    This model class links to the MySQL table "states"
    Attributes:
        id(int): identifier of state
        name(string): name of state
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    """
    When running as a script, use command line arguments as
     function inputs and print output to screen
    """
    from sys import argv
    from sqlalchemy import (create_engine)

    n = len(argv)
    if n != 4:
        print(
            "Usage: {} mysql_username ".format(argv[0]) +
            "mysql_password database_name"
        )
    else:
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                argv[1], argv[2], argv[3]
            ),
            pool_pre_ping=True
        )
        Base.metadata.create_all(engine)
