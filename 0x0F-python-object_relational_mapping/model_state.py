#!/usr/bin/python3
""" definition of a class State and an instance Base = declarative Base """


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """ Connects the ORM to the the states table"""

    __tablename__ = "states"

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
