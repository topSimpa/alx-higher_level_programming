#!/usr/bin/python3
"""connect to database AND
   delete all state
   that has 'a' in it name

   Usage: ./13-model_state_delete_a.py <username> <passwd> <database name>
"""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State):
        if 'a' in instance.name:
            session.delete(instance)
    session.commit()
