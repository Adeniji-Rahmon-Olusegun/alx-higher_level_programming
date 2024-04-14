#!/usr/bin/python3

"""
Script that lists all City objects from the database hbtn_0e_14_usa
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    db_url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"

    # running on the local host at port 3306 connect to mysql server
    engine = create_engine(db_url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    # creates the desired table
    Base.metadata.create_all(engine)

    cities = session.query(City, State).join(State).order_by(City.id).all()

    for city, state in cities:
        print(f"{state.name}: (city.id) {city.name}")

    session.close()
