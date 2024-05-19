#!/usr/bin/python3
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from os import getenv


STORAGE_TYPE = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """Represents a state class"""

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")

    if STORAGE_TYPE != 'db':
        name = ''
        cities = []

        @property
        def cities(self):
            """Gets a list of City instances with
               state_id equal to current state.id
            """
            city_list = []
            for city in models.storage.all(city):
                if city.state.id == self.id:
                    city_list.append(city)
            return city_list
