#!/usr/bin/python3
# Defines a State model
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a state for a MySQL database.
    __tablename__ (str): The name of the MySQL table"""
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)