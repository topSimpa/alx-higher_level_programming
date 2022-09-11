#!/usr/bin/python3
""" This script runs a program that add the State object "Louisiana"
    to the database

    Usage: ./11-model_state_insert.py <username> <passwd> <database name>
"""

import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    arg = sys.argv
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                            arg[1], arg[2], arg[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    update = session.query(State).filter(State.id == 2).one()
    update.name = "New Mexico"
    session.commit()
