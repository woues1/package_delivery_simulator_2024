import sys

from utils.kirjaudu import main_menu
from data.Tehtävät import *
from utils.pelaaja import *
from utils.valikko import valikko
from utils.kauppa_valikko import *

def main():
    jatka = True #Lisätty while loop että valikko toiminnallisuus toimii, en tiiä ootko samaaa mieltä tästä
    pelaaja = main_menu()
    while jatka:

#

    # toimiva tehtävän luonti
        #Easy vs hard mode, näkyy co2 consumed vs ei näy

        t1 = luo_tehtava(pelaaja)
        t2 = luo_tehtava(pelaaja)
        t3 = luo_tehtava(pelaaja)
        #lista = [t1,t2,t3] #näihin pitäs vaihtaa airport.name mielummin kun airport.id
        player_location_print = sql_db_lookup_location_name(pelaaja.location)
        player_country_print = sql_db_lookup_country_name(pelaaja.location)
        t1_location = sql_db_lookup_location_name(t1[0])
        t2_location = sql_db_lookup_location_name(t2[0])
        t3_location = sql_db_lookup_location_name(t3[0])
        t1_country = sql_db_lookup_country_name(t1[0])
        t2_country = sql_db_lookup_country_name(t2[0])
        t3_country = sql_db_lookup_country_name(t3[0])
        print(f"""
        +------------------------------------------+
        | Tehtävät(Airport, Co2 Consumed, kerroin) |
        +------------------------------------------+
        1.{t1} {t1_location[0][0]}, {t1_country[0][0]}
        2.{t2} {t2_location[0][0]}, {t2_country[0][0]}
        3.{t3} {t3_location[0][0]}, {t3_country[0][0]}
        +---------------------++---------------------++---------------------+ 
        |     Omat tiedot     |  Aktiivinen tehtava : {pelaaja.tehtava_aktiivinen}
        +---------------------++---------------------++---------------------+ 
        | {player_country_print[0][0]} 
        | {player_location_print[0][0]}                                             
        | {pelaaja.co2_consumed}/{pelaaja.co2_budget}                                      
        | {pelaaja.pisteet}         
        +---------------------++---------------------++---------------------+ 
        """)
        valinta = input("Valitse : 1.Valikko, 2.Valitse tehtävä , 3.Siirry , 4. Kauppa  ")#4.Kauppa? Vois käyttää raha saada permanent buffs, esim. Co2 consumed halved, pelaaja.pisteet doubler, Co2 Budget doubler.
        if valinta == "1":
            pelaaja = valikko(pelaaja)
            continue
        if valinta == "2":
            tehtava1 = Tehtava(t1[0], t1[1], t1[2], t1[3])
            tehtava2 = Tehtava(t2[0], t2[1], t2[2], t2[3])
            tehtava3 = Tehtava(t3[0], t3[1], t3[2], t3[3])
            tehtava = input("Valitse tehtävä (1, 2, 3): ")
            if tehtava == "1":
                pelaaja.aseta_tehtava(tehtava1)
            elif tehtava == "2":
                pelaaja.aseta_tehtava(tehtava2)
            elif tehtava == "3":
                pelaaja.aseta_tehtava(tehtava3)
            else:
                print(f"{tehtava} ei ole valinta.")
        if valinta == "3":
            pelaaja.suorita_tehtava()
        if valinta == "4":
            kauppa_valikko(pelaaja)
            continue

        if pelaaja.co2_consumed >= pelaaja.co2_budget:
            print(f"Game Over")
            sql_db_update_leaderboard(pelaaja.nimi, pelaaja.pisteet)
            sql_db_update_reset_game(pelaaja.nimi, pelaaja.salasana)
            sys.exit()



    #tehtava = Tehtava(t1[0],t1[1],t1[2])
    #pelaaja.aseta_tehtava(tehtava)
    #pelaaja.suorita_tehtava()


if __name__ == '__main__':
    main()
