#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel


class City(BaseModel):
    """ The city class, contains state ID and name """
    ___tablename__ = "cities"
    name = Column(string(128), nullable=False)
    state_id = Column(string(60), ForeignKey('states.id'), nullable=False)

    state_id = ""
    name = ""
