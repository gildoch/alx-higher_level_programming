#!/usr/bin/python3
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import Base, City
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    """Delete a record on the database"""

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    for city, state in session.query(City,  State).join(State).all():
        print("{}: ({:d}) {}".format(state.name, city.id, city.name))
    session.commit()
    session.close()
