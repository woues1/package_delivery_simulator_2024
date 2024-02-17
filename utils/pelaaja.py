from data.sql_db_update import *
# COPY PASTE PELAAJA
"""
from utils.pelaaja import olio_luonti
pelaaja = olio_luonti()
print(pelaaja.pisteet) = print(self."")
"""

# tehtava1 = Tehtava(location="Location1", co2_consumed=5, multiplier=2) <-- näin luodaan tehtävä

# pelaaja.current_tehtava = tehtava1 <-- tällä annetaan pelaajalle tehtävä

# pelaaja.suorita_tehtava() <-- tällä komennolla pelaaja suorittaa tehtävän

class Tehtava:
    def __init__(self, location, co2_consumed, multiplier):
        self.location = location
        self.co2_consumed = co2_consumed
        self.multiplier = multiplier


# pelaajan tiedot
class Pelaaja:
    def __init__(self, nimi, pisteet, location, co2_consumed):
        self.nimi = nimi
        self.pisteet = pisteet
        self.location = location
        self.co2_consumed = co2_consumed
        self.tehtava_aktiivinen = False
        self.current_tehtava = None

    def paivita_tehtava_aktiivinen(self, is_active):
        self.tehtava_aktiivinen = is_active

    def paivita_pisteet(self, piste_maara, kerroin):
        self.pisteet += piste_maara * kerroin

    def paivita_co2_kulutettu(self, co2_consumed):
        self.co2_consumed += co2_consumed

    def paivita_sijainti(self, location):
        self.location = location

    def aseta_tehtava(self, tehtava):
        if not self.tehtava_aktiivinen:
            self.current_tehtava = tehtava
            self.paivita_tehtava_aktiivinen(True)

    def suorita_tehtava(self):
        if self.tehtava_aktiivinen and self.current_tehtava:
            self.paivita_sijainti(self.current_tehtava.location)
            self.paivita_pisteet(10, self.current_tehtava.multiplier)
            self.paivita_co2_kulutettu(self.current_tehtava.co2_consumed)
            self.paivita_tehtava_aktiivinen(False)
            self.current_tehtava = None


def kayttaja_haku(id):
    tulos = sql_db_lookup_kayttaja_tiedot(id)
    return tulos


def olio_luonti(id):
    res = kayttaja_haku(id)
    for i in res:
        pelaaja = Pelaaja(i[0], i[1], i[2], i[3])
        return pelaaja
