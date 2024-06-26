#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel


class City(BaseModel):
    """ The city class, contains state ID and name """
    ___tablename__ = 'cities'
    if type_of_storage == 'db':
        name = Column(string(128), nullable=False)
        state_id = Column(string(60), ForeignKey('states.id'), nullable=False)
    else:
        state_id = ""
        name = ""
