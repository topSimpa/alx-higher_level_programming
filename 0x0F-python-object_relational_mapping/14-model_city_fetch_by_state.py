#!/usr/bin/python3
"""connect to database AND
   list all State in the database
   that has the same name as the fourth argument to this script

   Usage: ./14-model_city_fetch_by_state <username> <passwd> <database name>
"""


import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    result = session.query(City, State).\
        filter(City.state_id == State.id).order_by(City.id).all()

    for city, state in result:
        print(f"{state.name}: ({city.id}) {city.name}")
