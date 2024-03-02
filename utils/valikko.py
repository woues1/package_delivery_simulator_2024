from utils.pelaaja import olio_luonti
import sys
from data.sql_db_query import *
"""
def valikko():
    print("MAIN MENU PLACEHOLDER")
    print("PELAAJAN TIEDOT(pisteet, co2 budjetti jne.)")

    print("UUSI PELI (poistaa nykyisen pelitiedoston ja aloittaa uudestaan)")

    print("LOPETA PELI(nappi)")

"""


def valikko(pelaaja):
    while True:

        valinta = input("""
        +--------------------+
        Valitse
        +--------------------+
        1. Uusi peli...
        2. Tallenna ja poistu
        3. Takaisin...
        +--------------------+
        """)
        if valinta == "1":
            print("Aloitetaan uusi peli...")
            sql_db_reset_game(pelaaja.nimi, pelaaja.id)
            id = sql_db_lookup_log_in(pelaaja.nimi, pelaaja.id)
            pelaaja = olio_luonti(id[0][0])
            return pelaaja

        elif valinta== "2":
            print("Lopetetaan peli...")
            sql_db_update_exit_game(pelaaja.nimi, pelaaja.co2_consumed, pelaaja.location, pelaaja.pisteet)
            sys.exit()

        elif valinta == "3":
            return pelaaja

