#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import sqlalchemy
import models


class City(BaseModel):
    """ The city class, contains state ID and name """
    ___tablename__ = 'cities'
    if type_of_storage == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    else:
        state_id = ""
        name = ""


    def __init__(self, *args, **kwargs):
        """Initializes city """
        super().__init__(*args, **kwargs)
