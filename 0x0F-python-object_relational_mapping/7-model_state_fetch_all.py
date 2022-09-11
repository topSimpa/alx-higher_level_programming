#!/usr/bin/python3
"""connect to database AND
   list all State in the database

   Usage: ./7-model_state_fetch_all.py <username> <passwd> <database name>
"""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    for instance in session.query(State).order_by(State.id):
        print("{}: {}".format(instance.id, instance.name))
