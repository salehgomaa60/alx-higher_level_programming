#!/usr/bin/python3
""" Listing the model  states from mysqldb"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def db_engine():
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{user}:{password}@localhost:3306/{db}'
        )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).first()
    if states:
        print(f"{states.id}: {states.name}")
    else:
        print("Nothing")
    session.close()


if __name__ == "__main__":
    db_engine()
