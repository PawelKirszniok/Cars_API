from pydantic import BaseModel, Field
from pydantic.color import Color


class NewCarRequest(BaseModel):
    make: str
    color: Color
    production_year: int = Field(gt=1950, lt=2030)
    avg_fuel_consumption_per_100km: float
    max_passengers: int
