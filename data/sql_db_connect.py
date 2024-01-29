import mysql.connector

# Replace the placeholders with your database credentials
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'flight_game',
}

# Establish a connection
conn = mysql.connector.connect(**db_config)

# Create a cursor to interact with the database
cursor = conn.cursor()

# Example: execute a simple query
cursor.execute("SELECT * FROM airport")
result = cursor.fetchall()
print(result)

# Close the cursor and connection when done
cursor.close()
conn.close()
