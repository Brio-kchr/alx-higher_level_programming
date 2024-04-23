#!/usr/bin/python3
"""
This module provides a class City which is an ORM model
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    This model class links to the MySQL table "cities"
    Attributes:
        id(int): identifier of city
        name(string): name of city
        state_id(int): state the city belongs to
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
