#!/usr/bin/python3
""" definition of a class State and an instance Base = declarative Base """

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """ Connects the ORM to the the states table"""

    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade="all, delete",
                          backref="state")
