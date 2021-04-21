from configparser import ConfigParser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models.car import Car
from typing import List
import os


class DatabaseService:

    def __init__(self):
        config_object = ConfigParser()
        directory = os.path.dirname(__file__)
        filepath = os.path.join(directory, 'config.ini')
        config_object.read(filepath)

        db_config = config_object['DATABASECONFIG']
        login_string = f"{db_config['prefix']}://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['dbname']}"

        engine = create_engine(login_string, pool_pre_ping=True)

        self.session = sessionmaker(bind=engine)()

    def save_car(self, car: Car):

        self.session.add(car)
        self.session.commit()

    def get_all_cars(self) -> List[Car]:

        return self.session.query(Car).all()

    def get_car_by_id(self, car_id) -> Car:

        return self.session.query(Car).filter_by(id=car_id).all()



