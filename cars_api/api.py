from fastapi import FastAPI
from cars_api.request_model import NewCarRequest
from cars_api import database_service
from cars_api.database.models.car import Car

app = FastAPI()


@app.post('/api/car')
def add_new_car(request: NewCarRequest):
    database_service.save_car(Car(request))


@app.get('/api/car')
def get_all_cars():
    return database_service.get_all_cars()


@app.get('/api/car/{car_id}')
def get_car_by_id(car_id: int):
    return database_service.get_car_by_id(car_id)

