from errno import errorcode
import mysql.connector



def get_connection():
    try:
        return mysql.connector.connect(
            user= 'your-username',
            password='your-password',
            host='your-host',
            database='your-data-base-name',
            port='your-port'
        )
    except mysql.connector.Error as err:
        print(f"Error al conectar: {err}")
        return None

