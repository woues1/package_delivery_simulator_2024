import mysql.connector


def get_db_connection() -> mysql.connector.connect:

    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'root',
        'database': 'flight_game',
        'autocommit': True
    }

    # Establish a connection
    return mysql.connector.connect(**db_config)


def sql_search(sql):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    return result
