import mysql.connector

def getConnection():
    config = {
        'user': 'admin',
        'password': 'Iweb.2025!',
        'host': 'automotores-yrigoyen-db.cx6mgus88zkq.sa-east-1.rds.amazonaws.com',
        'database': 'automotores-yrigoyen-db',
        'raise_on_warnings': True,
        'port': '3306'
    }

    try:
        connection = mysql.connector.connect(**config)
        return connection
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        return None