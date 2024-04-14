#!/usr/bin/python3

"""
Script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    db_url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"

    # running on the local host at port 3306 connect to mysql server
    engine = create_engine(db_url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    new_state = State(name="Louisiana")

    session.add(new_state)

    session.commit()

    print(new_state.id)

    session.close()
