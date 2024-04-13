#!/usr/bin/python3

"""
Script that lists all State objects from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import decalarative_base
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    db_url = "mysql://argv[1]:argv[2]@localhost:3306/argv[3]"

    # running on the local host at port 3306 connect to mysql server
    engine = create_engine(db_url)

    Session = sessionmaker(bind=engine)

    session = Session()

    # creates the desired table
    Base.metadata.create_all(engine)

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{State.id}: {State.name}")

    session.close()
