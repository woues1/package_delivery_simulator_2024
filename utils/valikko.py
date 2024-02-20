
"""
def valikko():
    print("MAIN MENU PLACEHOLDER")
    print("PELAAJAN TIEDOT(pisteet, co2 budjetti jne.)")

    print("UUSI PELI (poistaa nykyisen pelitiedoston ja aloittaa uudestaan)")

    print("LOPETA PELI(nappi)")

"""
import sys
from data.sql_db_update import *
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
            print("Uusi peli...")
            screen_name = input("Käyttäjänimi: ")
            player_password = input("Salasana : ")
            pelaaja = sql_db_update_new_game(screen_name, player_password)
            return pelaaja
        elif valinta== "2":
            print("Lopetetaan peli...")
            sql_db_update_exit_game(pelaaja.nimi, pelaaja.co2_consumed, pelaaja.location)
            sys.exit()
        elif valinta == "3":
            return pelaaja

