#!/usr/bin/python3
"""defines the class City"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column, ForeignKey

Base = declarative_base()


class City(Base):
    """This maps to the cities table"""
    __tablename__ = "cities"
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
