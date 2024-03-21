#!/usr/bin/python3
"""script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa"""

from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    """Add new state to the database"""

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:33061/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    data = State(name="Louisiana")
    session.add(data)
    session.commit()
    print("{0}".format(data.id))
    session.close()
