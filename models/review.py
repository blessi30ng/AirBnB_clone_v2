#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review classto store review information """
    __tablename__ = "reviews"
    if type_of_storage == 'db':
        text = Column(string(1024), nullable=False)
        place_id = Column(string(60), nullable=False, ForeignKey('places.id'))
        user_id = Column(string(60), nullable=False, ForeignKey('user.id'))
    else:
        place_id = ""
        user_id = ""
        text = ""
