from operator import ge
from fastapi import APIRouter, HTTPException
from models.cars import Cars
from Database.dbGetConnection import getConnection
from Database.testConnection import get_connection
import uuid

router = APIRouter()

@router.get('/teste-database')

def testeDatabase():
    connection = get_connection()
    if(connection == True):
        return {"message": "Database connection successful"}
    
# Get all cars
@router.get('/cars')

def getCars():
    connection = getConnection()

    if connection is None:
        raise HTTPException(status_code=500, detail="Connection to the database failed.")

    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM `Cars`")

    cars = cursor.fetchall()
    cursor.close()

    connection.close()
    return cars
    
# Filter cars by id

@router.get('/cars/{id}')

def getCar(id: str):
    connection = getConnection()

    if connection is None:
        raise HTTPException(status_code=500, detail="Connection to the database failed.")

    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM `Cars` WHERE id = %s", (id,))
    
    car = cursor.fetchone()
    cursor.close()

    connection.close()

    if car is None:
        raise HTTPException(status_code=404, detail="Car not found.")
    return car

# Create car
@router.post('/products/create_car')

def createCar(cars: Cars):

    connection = getConnection()
    
    generated_id = str(uuid.uuid4())

    if connection is None:
        raise HTTPException(status_code=500, detail="Connection to the database failed.")
    cursor = connection.cursor()

    cursor.execute("INSERT INTO `Cars`(`ID`, `marca`, `modelo`, `km`, `anio`, `combustible`, `precio`, `motor`, `carroceria`, `aire_acondicionado`, `puertas`, `transmision`, `litros`, `frenos`, `airbag`, `sensor`, `permuta`, `traccion`, `anticipo`, `imagen1`, `imagen2`, `imagen3`, `imagen4`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                  (generated_id, cars.marca, cars.modelo, cars.km, cars.anio, cars.combustible, cars.precio, cars.motor, cars.carroceria, cars.aire_acondicionado, cars.puertas, cars.transmision, cars.litros, cars.frenos, cars.airbag, cars.sensor, cars.permuta, cars.traccion, cars.anticipo, cars.imagen1, cars.imagen2, cars.imagen3, cars.imagen4))
    connection.commit()

    cursor.close()

    connection.close()

    return {"message": "Car created successfully ID: " + generated_id}

# Put car
@router.put('/cars/{id}')

def modProduct(id: str, cars: Cars):
    connection = getConnection()

    if connection is None:
        raise HTTPException(status_code=500, detail="Connection to the database failed.")

    cursor = connection.cursor()

    cursor.execute("UPDATE `Cars` SET marca = %s, modelo = %s, km = %s, anio = %s, combustible = %s, precio = %s, motor = %s, carroceria = %s, aire_acondicionado = %s, puertas = %s, transmision = %s, litros = %s, frenos = %s, airbag = %s, sensor = %s, permuta = %s, traccion = %s, anticipo = %s, imagen1 = %s, imagen2 = %s, imagen3 = %s, imagen4 = %s  WHERE id = %s", (cars.marca, cars.modelo, cars.km, cars.anio, cars.combustible, cars.precio, cars.motor, cars.carroceria, cars.aire_acondicionado, cars.puertas, cars.transmision, cars.litros, cars.frenos, cars.airbag, cars.sensor, cars.permuta, cars.traccion, cars.anticipo, cars.imagen1, cars.imagen2, cars.imagen3, cars.imagen4, id))
    
    connection.commit()
    
    cursor.close()

    connection.close()

    return {"message": "Car updated successfully"}

# Delete car
@router.delete('/cars/{id}')

def delCars(id: str):
    connection = getConnection()

    if connection is None:
        raise HTTPException(status_code=500, detail="Connection to the database failed.")

    cursor = connection.cursor()

    cursor.execute("DELETE FROM `Cars` WHERE id = %s", (id,))

    connection.commit()

    cursor.close()

    connection.close()
    return {"message": "Car deleted successfully"}