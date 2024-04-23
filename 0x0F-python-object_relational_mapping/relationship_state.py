#!/usr/bin/python3
"""
This module provides a class State which is an ORM model
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base


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
    cities = relationship(
        "City",
        backref="state",
        cascade="all, delete"
    )
