from pydoc import describe
from pydantic import BaseModel
from typing import Optional
from datetime import date

class Cars(BaseModel):
    id: Optional[str] = None
    title: str
    cash_price: str
    year: str
    km: str
    engine: str
    liters: str
    abs_type_breaks: str
    transmition: str
    speed_number: str
    front_air_bags: str
    doors: str
    parking_sensor: str
    exchange_accept: str
    traction: str
    air_conditioning: str
    advance: str