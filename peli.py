from utils.kirjaudu import main_menu
from data.Tehtävät import *
from utils.pelaaja import *
from utils.valikko import valikko


def main():
    jatka = True#Lisätty while loop että valikko toiminnallisuus toimii, en tiiä ootko samaaa mieltä tästä
    pelaaja = main_menu()
    while jatka:

        print(pelaaja.nimi)

    # toimiva tehtävän luonti

        t1 = luo_tehtava(pelaaja)
        t2 = luo_tehtava(pelaaja)
        t3 = luo_tehtava(pelaaja)
        lista = [t1,t2,t3]#näihin pitäs vaihtaa airport.name mielummin kun airport.id
        player_location_print = sql_db_lookup_location_name(pelaaja.location)
        player_country_print = sql_db_lookup_country_name(pelaaja.location)
        print(*lista[0])
        print(f"""
        +------------------------------------------+
        | Tehtävät(Airport, Co2 Consumed, kerroin) |
        +------------------------------------------+
        1.{t1}
        2.{t2} 
        3.{t3} 
        +---------------------++---------------------++---------------------+ 
        |     Omat tiedot     |  Aktiivinen tehtava : {pelaaja.current_tehtava}
        +---------------------++---------------------++---------------------+ 
        | {player_country_print[0][0]} 
        | {player_location_print[0][0]}                                             
        | {pelaaja.co2_consumed}/10000                                      
        | {pelaaja.pisteet}         
        +---------------------++---------------------++---------------------+ 
        """)
        valinta = input("Valitse : 1.Valikko, 2.Valitse tehtävä , 3.Siirry  ")#4.Kauppa? Vois käyttää raha saada permanent buffs, esim. Co2 consumed halved, pelaaja.pisteet doubler, Co2 Budget doubler.
        if valinta == "1":
            valikko(pelaaja)
            continue
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
        if valinta == "3":
            pelaaja.suorita_tehtava()
        else:
            print(f"{valinta} ei ole valinta")

    #tehtava = Tehtava(t1[0],t1[1],t1[2])
    #pelaaja.aseta_tehtava(tehtava)
    #pelaaja.suorita_tehtava()



if __name__ == '__main__':
    main()
