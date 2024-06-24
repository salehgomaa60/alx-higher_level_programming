#!/usr/bin/python3
""" listing model states from mysqldb"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def db_engine():
    if len(sys.argv) != 4:
        return
    
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')
    
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).all()
    
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()

if __name__ == "__main__":
    db_engine()
