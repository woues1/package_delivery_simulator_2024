import sys
from utils.Main_menu import main_menu
from data.tehtavan_luonti_algoritmi import luo_tehtava
from utils.pelaaja import *
from utils.valikko import valikko
from utils.kauppa_valikko import *


def main():
    jatka = True #Lisätty while loop että valikko toiminnallisuus toimii, en tiiä ootko samaaa mieltä tästä
    pelaaja = main_menu()
    items = [Item(*item) for item in sql_db_lookup_items(pelaaja.id)]
    for item in items:
        if item.purchased:
            pelaaja.add_item(item)

    # If you still need references to item1, item2, and item3
    item1, item2, item3 = items[:3]

    while jatka:
        # toimiva tehtävän luonti
        # Easy vs hard mode, näkyy co2 consumed vs ei näy
        # Tehtävän luonti/ylikirjoitus
        # Tarkistaa onko tehtävä aktiivista tehtävää
        # ja onko yksi tehtävä suoritettu ennen uusien tehtävien luomista

        if pelaaja.tehtava_aktiivinen == False and Tehtava.instance_count < 3:
            t1 = luo_tehtava(pelaaja)
            t2 = luo_tehtava(pelaaja)
            t3 = luo_tehtava(pelaaja)


        print(f"""
        +------------------------------------------+
        | Tehtävät(Co2 Consumed, Kerroin, Pisteet) |
        +------------------------------------------+
        1. co2: {t1.lookup_co2_consumed()}  K: {t1.lookup_kerroin()}  P: {t1.lookup_pisteet()} | {t1.lookup_airport()}, {t1.lookup_country()}
        2. co2: {t2.lookup_co2_consumed()}  K: {t3.lookup_kerroin()}  P: {t2.lookup_pisteet()} | {t2.lookup_airport()}, {t2.lookup_country()}
        3. co2: {t3.lookup_co2_consumed()}  K: {t3.lookup_kerroin()}  P: {t3.lookup_pisteet()} | {t3.lookup_airport()}, {t3.lookup_country()}
        +---------------------++---------------------++---------------------+ 
        |     Omat tiedot     |  Aktiivinen tehtava: {pelaaja.hae_current_tehtava_tiedot()}
        +---------------------++---------------------++---------------------+ 
        | {pelaaja.hae_pelaaja_Maa()} 
        | {pelaaja.hae_pelaaja_lentokentta()}                                          
        | {pelaaja.co2_consumed}/{pelaaja.co2_budget}                                      
        | {pelaaja.pisteet}         
        +---------------------++---------------------++---------------------+ 
        """)

        valinta = input("Valitse : 1.Valikko, 2.Valitse tehtävä , 3.Siirry , 4. Kauppa  ")#4.Kauppa? Vois käyttää raha saada permanent buffs, esim. Co2 consumed halved, pelaaja.pisteet doubler, Co2 Budget doubler.

        # Pelaajan valinta logiikka
        if valinta == "1":
            pelaaja = valikko(pelaaja)
            continue

        # Tehtävän valinta
        if valinta == "2":

            tehtava = input("Valitse tehtävä (1, 2, 3): ")

            if tehtava == "1":
                pelaaja.aseta_tehtava(t1)
            elif tehtava == "2":
                pelaaja.aseta_tehtava(t2)
            elif tehtava == "3":
                pelaaja.aseta_tehtava(t3)
            else:
                print(f"{tehtava} ei ole valinta.")

        # aktiivisen tehtävän suoritus
        if valinta == "3":
            if pelaaja.current_tehtava:

                # asettaa tehtävä countin 0, jotta voidaan aloittaa uusi kierros
                # ilman "Tehtava.instance_count -= 3" count menee ylöspäin loputtomasti
                Tehtava.instance_count -= 3
                pelaaja.suorita_tehtava()

        # Tuo esiin kauppa näkymän
        if valinta == "4":
            kauppa_valikko(pelaaja, item1, item2, item3)


        # Tarkistaa onko pelaaja ylittänyt budjetin
        if pelaaja.co2_consumed >= pelaaja.co2_budget:
            print(f"Game Over")
            sql_db_update_leaderboard(pelaaja.nimi, pelaaja.pisteet)
            sql_db_reset_game(pelaaja.id)
            sys.exit()


if __name__ == '__main__':
    main()
