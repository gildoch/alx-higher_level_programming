#!/usr/bin/python3
"""
This script defines a City class and
a Base class to work with MySQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """City class

    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The City id of the class
        name (str): The City name of the class
        states_id (str): The ID of the state

    """

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
