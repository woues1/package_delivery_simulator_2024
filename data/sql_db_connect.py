import mysql.connector


def get_db_connection() -> mysql.connector.connect:

    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'root',
        'database': 'flight_game',
    }

    # Establish a connection
    return mysql.connector.connect(**db_config)
