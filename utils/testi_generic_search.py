
import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='makkarakoira123',
         autocommit=True
         )



def hae(sql):
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

#from Modules.SQL_DEFAULT_SEARCH import hae