import time
import sys
from utils.pelaaja import initialize_player
from data.sql_db_query import *

"""
def valikko():
    print("MAIN MENU PLACEHOLDER")
    print("PELAAJAN TIEDOT(pisteet, co2 budjetti jne.)")

    print("UUSI PELI (poistaa nykyisen pelitiedoston ja aloittaa uudestaan)")

    print("LOPETA PELI(nappi)")

"""


def valikko(pelaaja, items):
    valinta = input("""
    +--------------------+
    Valitse
    +--------------------+
    1. Uusi peli...
    2. Tallenna ja poistu
    3. Takaisin...
    +--------------------+
    """)
    while True:

        if valinta == "1":
            valinta_v = input("Oletko varma ? y/n: ")
            if valinta_v == "y":
                print("Aloitetaan uusi peli...")
                sql_db_reset_game(pelaaja.id)
                pelaaja = initialize_player(pelaaja.id)
                for item in items:
                    item.purchased = 0
                time.sleep(1)
            return pelaaja

        elif valinta == "2":
            print("Lopetetaan peli...")
            time.sleep(1)
            sql_db_update_exit_game(pelaaja.nimi, pelaaja.co2_consumed, pelaaja.location, pelaaja.pisteet)
            print("Tallennetaan tietoja")
            time.sleep(1)
            sys.exit()

        elif valinta == "3":
            return pelaaja

        valinta = input("    ")
