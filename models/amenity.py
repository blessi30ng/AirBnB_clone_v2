#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class Amenity(BaseModel):
    __tablename__ = "amenities"
    if type_of_storage == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Initializes amenity"""
        super().__init__(*args, **kwargs)
