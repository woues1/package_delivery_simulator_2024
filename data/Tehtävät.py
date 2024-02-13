import keyboard
import numpy as np
from data.sql_db_connect import sql_search
from utils.pelaaja import olio_luonti


pelaaja = olio_luonti()


def luo_tehtava():
    tulos = sql_search(f"SELECT airport.ident, airport.name FROM airport WHERE iso_country = 'FI'")
    lentokenttien_maara = len(tulos)
    tehtavat = []
    for _ in range(3):
        sijainti = np.random.randint(0, lentokenttien_maara-1)
        tehtavat.append(tulos[sijainti])
    return tehtavat


# DEF PISTEENMÄÄRITYS()
# print(Pelaaja.pisteet)
# KERROIN = 0
# SIJAINTI TIEDO = DB HAKU
# TYPE, GOAL.NAAME, COUNRTY
# IF TYPE HELIPORT KERRROIN = +3
# IF  GOAAL.NAME CLOUDS 0.7 RAHAA
# IF ETÄISYYS YLI 300 KM 3
# ÅIVITA_PSITEET(KERROIN)

def tulosta_tehtava(tehtavat):
    tehtava_numero = 1
    for i in tehtavat:
        print(f"\nToimita paketti lentokentälle: {i[1]} (paina {tehtava_numero})")
        tehtava_numero += 1


def valitse_tehtava(tehtavat, pelaaja):
    while True:
        pressed_key = input("valitse (1) (2) (3)")
        if pressed_key in ['1', '2', '3']:
            pressed_key = int(pressed_key)
            pelaaja.paivita_tehtava_aktiivinen(True)
            return print(tehtavat[pressed_key])
        else:
            print("Invalid input. Please press 1, 2, or 3.")
