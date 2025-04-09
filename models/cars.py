from pydoc import describe
from re import S
from xmlrpc.client import boolean
from pydantic import BaseModel
from typing import Optional
from datetime import date

class Cars(BaseModel):
    id: Optional[str] = None
    marca: str
    modelo: str
    km: str
    anio: int
    combustible: str
    precio: int
    motor: float
    carroceria: str
    aire_acondicionado: bool
    puertas: int
    transmision: str
    litros: float
    frenos: bool
    airbag: bool
    sensor: bool
    permuta: bool
    traccion: str
    anticipo: str
    imagen1: str
    imagen2: str
    imagen3: str
    imagen4: str
    hidraulica: bool