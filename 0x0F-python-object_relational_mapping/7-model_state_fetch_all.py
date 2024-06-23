#!/usr/bin/python3
"""List all the  states from mysqldb in ascending order by id """


from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def db_engine():
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
        )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(asc(state.id)).all()
    for state in states:
        print(f"{state.id}: {state.name}")
        print("\n")

    session.close()


if __name__ == "__main__":
    db_engine()
