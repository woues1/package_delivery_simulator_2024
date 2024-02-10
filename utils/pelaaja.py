from data.sql_db_connect import get_db_connection

connection = get_db_connection()
cursor = connection.cursor()

cursor.execute("SELECT screen_name, co2_budget, location FROM game where screen_name = 'ilkka'")
result = cursor.fetchall()
cursor.close()
connection.close()

class pelaaja:
    def __init__(self, nimi, pisteet, location):
        self.nimi = nimi
        self.pisteet = pisteet
        self.location = location


for i in result:
    pelaaja = pelaaja(i[0],i[1],i[2])

print(pelaaja.nimi, pelaaja.pisteet, pelaaja.location)
