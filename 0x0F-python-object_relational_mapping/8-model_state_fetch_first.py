#!/usr/bin/python3
"""
Mod
"""
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    """Query for all states on database"""

    engine = create_engine(
        "mysql+pymysql://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.query(State).order_by(State.id).first()

    if data is None:
        print("Nothing")
    else:
        print("{0}: {1}".format(data.id, data.name))
