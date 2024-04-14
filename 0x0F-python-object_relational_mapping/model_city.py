#!/usr/bin/python3

"""
Python file that contains the class definition of a City
and an instance Base = declarative_base()
"""

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class City(Base):
    """class for cities table"""

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    state = relationship("State", back_populates="cities")

