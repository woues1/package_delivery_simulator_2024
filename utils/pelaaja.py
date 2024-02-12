from data.sql_db_connect import sql_search

# COPY PASTE PELAAJA
"""
from utils.pelaaja import olio_luonti
pelaaja = olio_luonti()
print(pelaaja.pisteet) = print(self."")
"""


# pelaajan tiedot
class Pelaaja:
    _instance = None

    def __new__(cls, nimi, pisteet, location):
        if cls._instance is None:
            cls._instance = super(Pelaaja, cls).__new__(cls)
            cls._instance.nimi = nimi
            cls._instance.pisteet = pisteet
            cls._instance.location = location
            cls._instance.tehtava_aktiivinen = False
        return cls._instance

    def paivita_tehtava_aktiivinen(self, is_active):
        self.tehtava_aktiivinen = is_active

    def paivita_pisteet(self, piste_maara, kerroin):
        self.pisteet += piste_maara * kerroin

def kayttaja_haku():
    tulos = sql_search(f"SELECT screen_name, co2_budget, location "
                       f"FROM game "
                       f"WHERE screen_name = 'ilkka'")
    return tulos

def olio_luonti():
    res = kayttaja_haku()
    for i in res:
        pelaaja = Pelaaja(i[0], i[1], i[2])
        return pelaaja
