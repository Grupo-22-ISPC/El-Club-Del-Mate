from errno import errorcode
import mysql.connector



def get_connection():
    try:
        return mysql.connector.connect(
            user= 'root',
            password='',
            host='localhost',
            database='club_del_mate',
            port='3309'
        )
    except mysql.connector.Error as err:
        print(f"Error al conectar: {err}")
        return None

