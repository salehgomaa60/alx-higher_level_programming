#!/usr/bin/python3
""" listing  states from mysqldb"""


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
    states = session.query(State).\
        filter(State.name == sys.argv[4]).order_by(State.id).all()
    if states:
        print("{}".format(states[0].id))
    else:
        print("Not found")

    session.close()


if __name__ == "__main__":
    db_engine()
