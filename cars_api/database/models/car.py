from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, Float, DateTime
from sqlalchemy.sql import func
from cars_api.request_model import NewCarRequest
import uuid as uid

Base = declarative_base()


class Car(Base):
    """database model for cars"""

    __tablename__ = "car"
    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(String(40), unique=True, nullable=False)
    make = Column(String(50))
    color = Column(String(7))
    production_year = Column(Integer)
    average_consumption = Column(Float)  # expressed in liters per 100 km
    max_passengers = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __init__(self, new_car:NewCarRequest):

        self.uuid = uid.uuid4()
        self.make = new_car.make
        self.color = new_car.color.as_hex()
        self.production_year = new_car.production_year
        self.average_consumption = new_car.avg_fuel_consumption_per_100km
        self.max_passengers = new_car.max_passengers



