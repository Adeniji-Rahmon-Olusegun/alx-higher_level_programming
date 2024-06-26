#!/usr/bin/python3

"""
Script that creates the State “California” with
the City “San Francisco” from the database hbtn_0e_100_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":

    db_url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"

    # running on the local host at port 3306 connect to mysql server
    engine = create_engine(db_url, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)

    session.add_all([new_state, new_city])

    session.commit()

    session.close()
