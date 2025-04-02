import mysql.connector

def getConnection():
    config = {
        'user': 'u830440565_facundo2',
        'password': 'Iweb.2025!',
        'host': '193.203.175.121',
        'database': 'u830440565_automotores_yr',
        'raise_on_warnings': True,
        'port': '3306'
    }

    try:
        connection = mysql.connector.connect(**config)
        return connection
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        return None