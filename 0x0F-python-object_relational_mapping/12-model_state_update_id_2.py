#!/usr/bin/python3
"""script that changes the name of a State object
 from the database hbtn_0e_6_usa"""

from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    """Update a recorde on the database"""

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:33061/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(State).filter(State.id == 2).update({"name": "New Mexico"})
    session.commit()
    session.close()
