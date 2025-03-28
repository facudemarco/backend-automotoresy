from fastapi import APIRouter, HTTPException
from models.cars import Cars
from Database.dbGetConnection import getConnection
from Database.testConnection import get_connection
import uuid


router = APIRouter()

@router.get('/teste-database')

def testeDatabase():
    connection = get_connection()
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

    cursor.execute("INSERT INTO `Cars`(`ID`, `title`, `cash_price`, `year`, `km`, `engine`, `liters`, `abs_type_breaks`, `transmition`, `speed_number`, `front_air_bags`, `doors`, `parking_sensor`, `exchange_accept`, `traction`, `air_conditioning`, `advance`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                  (generated_id, Cars.title, Cars.cash_price, Cars.year, Cars.km, Cars.engine, Cars.liters, Cars.abs_type_breaks, Cars.transmition, Cars.speed_number, Cars.front_air_bags, Cars.doors, Cars.parking_sensor, Cars.exchange_accept, Cars.traction, Cars.air_conditioning, Cars.advance))
    connection.commit()

    cursor.close()

    connection.close()

    return {"message": "Car created successfully, ID: " + generated_id}

# Put car
@router.put('/cars/{id}')

def modProduct(id: str, car: Cars):
    connection = getConnection()

    if connection is None:
        raise HTTPException(status_code=500, detail="Connection to the database failed.")

    cursor = connection.cursor()

    cursor.execute("UPDATE `Cars` SET title = %s, cash_price = %s, year = %s, km = %s, engine = %s, liters = %s, abs_type_breaks = %s, transmition = %s, speed_number = %s, front_air_bags = %s, doors = %s, parking_sensor = %s, exchange_accept = %s, traction = %s, air_conditioning = %s, advance = %s, id WHERE id = %s", (Cars.title, Cars.cash_price, Cars.year, Cars.km, Cars.engine, Cars.liters, Cars.abs_type_breaks, Cars.transmition, Cars.speed_number, Cars.front_air_bags, Cars.doors, Cars.parking_sensor, Cars.exchange_accept, Cars.traction, Cars.air_conditioning, Cars.advance, id))
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