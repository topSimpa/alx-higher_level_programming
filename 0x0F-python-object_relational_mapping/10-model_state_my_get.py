#!/usr/bin/python3
"""connect to database AND
   list all State in the database
   that has the same name as the fourth argument to this script

   Usage: ./10-model_state_my_get.py <username> <passwd> <database name>
          <state name>
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
    name = sys.argv[4]

    result = session.query(State).filter_by(name=name).first()
    if result:
        print(result.id)
    else:
        print("Not found")
