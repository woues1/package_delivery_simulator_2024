from data.sql_db_connect import get_db_connection

connection = get_db_connection()
cursor = connection.cursor()

cursor.execute("SELECT * FROM airport")
result = cursor.fetchall()
print(result)

cursor.close()
connection.close()


