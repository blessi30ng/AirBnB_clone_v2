#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    if type_of_storage == 'db':
        name = Column(string(128), nullable=False)
    else:
        name = ""
