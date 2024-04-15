#!/usr/bin/python3

"""
Python file that contains the class definition of a State
and an instance Base = declarative_base()
"""

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class State(Base):
    """class for states table"""

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_ref="state", cascade="all, delete")
