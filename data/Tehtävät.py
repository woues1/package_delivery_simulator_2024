from data.sql_db_connect import sql_search
from data.tehtavan_luonti_algoritmi import *


def luo_tehtava():
    location = generate_delivery_location()
    co2_consumed = co2_consumed_distance(location)
    kerroin = kerroin_maarittaja(co2_consumed)
    lista = [location, co2_consumed, kerroin]
    return lista



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
            return
        else:
            print("Invalid input. Please press 1, 2, or 3.")
