#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv
import sqlalchemy
import models


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    if type_of_storage == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, *kwargs):
        """Initializes state"""
        super().__init__(*args, **kwargs)

    if type_of_storage != 'db':
        @property
        def cities(self):
            """getter for list of city instances related to the state"""
            city_l = []
            all_cities = storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_l.append(city)
            return city_l
