import mysql.connector

def get_connection():
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
        print("Conexión exitosa a la base de datos.")
        return connection
    except mysql.connector.Error as err:
        print(f"Error al conectar: {err}")
        return None

if __name__ == "__main__":
    conn = get_connection()
    if conn:
        conn.close()