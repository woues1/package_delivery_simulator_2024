from data.sql_db_connect import sql_search

# COPY PASTE PELAAJA
"""
from utils.pelaaja import olio_luonti
pelaaja = olio_luonti()
"""

# pelaajan tiedot
class Pelaaja:
    def __init__(self, nimi, pisteet, location):
        self.nimi = nimi
        self.pisteet = pisteet
        self.location = location
        self.tehtava_aktiivinen = False

    # Päivittää pelaajan tehtävä tilan
    def paivita_tehtava_aktiivinen(self, is_active):
        self.tehtava_aktiivinen = is_active

    def paivita_pisteet(self, pisteet, p_maara, kerroin):
        self.pisteet = pisteet + p_maara * kerroin


def kayttaja_haku():
    tulos = sql_search(f"SELECT screen_name, co2_budget, location "
                        f"FROM game "
                        f"where screen_name = 'ilkka'")
    return tulos


# luo olion, johon tallennetaan pelaajan tiedot
def olio_luonti():
    res = kayttaja_haku()
    for i in res:
        asd = Pelaaja(i[0], i[1], i[2])
        return asd
