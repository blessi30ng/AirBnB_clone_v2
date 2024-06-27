#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


if type_of_storage == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
            Column('place_id'), String(60),
                ForeignKey('places.id', onupdate='CASCADE',
                    ondelete='CASCADE')
            Column('amenity_id', String(60),
                ForeignKey('amenities_id', onupdate='CASCADE',
                    ondelete='CASCADE'),
                primary_key=True))


class Place(BaseModel):
    """ A place to stay """
    __tablename__ = 'places'
    if type_of_storage == 'db':
        city_id = Column(string(60), nullable=False, ForeignKey('cities.id'))
        user_id = Column(string(60), nullable=False, ForeignKey('user.id'))
        name = Column(string(128), nullable=False)
        description = Column(string(1024), nullable=False)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=False)
        longitude = Column(Float, nullable=False)
        reviews = relationship("Review", backref="place")
        amenities = relationship("Amenity", secondary="place_amenity",
                backref="place_amenities",
                viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Initializes place"""
        super().__init__(*args, **kwargs)

    if type_of_storage != 'db':
        @property
        def reviews(self):
            """ getter returns the list of Review instances"""
            from models.review import Amenity
            review_l = []
            all_reviews = storage.all(Review)
            for review in all_reviews.values():
                if review.place_id == self.id:
                    review_l.append(review)
            return review_l

        @property
        def amenities(self):
            """getter returns the listof amenity instances"""
            from models.amenity import Amenity
            amenity_l = []
            all_amenities = storage.all(Amenity)
            for amenity in all_amenities.values():
                if amenity.place_id == self.id:
                    amenity_l.append(amenity)
            return amenity_l
