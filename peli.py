from data.tehtavan_luonti_algoritmi import luo_tehtava
from utils.Main_menu import main_menu
from utils.easter_eggs import *
from utils.kauppa_valikko import *
from utils.pelaaja import *
from utils.valikko import valikko
from Assets.ASCII_art import game_over
from Assets.animaatio import *
import asyncio


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033c", end="")


async def main():
    jatka = True
    pelaaja = main_menu()
    items = initialize_items(pelaaja)

    while jatka:
        if pelaaja.tehtava_aktiivinen == False and Tehtava.instance_count < 3:
            tasks = [
                asyncio.create_task(luo_tehtava(pelaaja.location)) for _ in range(3)
            ]
            t1, t2, t3 = await asyncio.gather(*tasks)

        if pelaaja.hae_pelaaja_Maa() == "Columbia":
            operation_columbia(t1.lookup_airport())
            t1.multiplier = 20

        clear_console()
        print(f"""
        +------------------------------------------+
        | Tehtävät(Co2 Consumed, Kerroin, Pisteet) |
        +------------------------------------------+
        1. co2: {t1.lookup_co2_consumed()}  K: {t1.lookup_kerroin()}  P: {t1.lookup_pisteet()} | {t1.lookup_airport()}, {t1.lookup_country()}
        2. co2: {t2.lookup_co2_consumed()}  K: {t2.lookup_kerroin()}  P: {t2.lookup_pisteet()} | {t2.lookup_airport()}, {t2.lookup_country()}
        3. co2: {t3.lookup_co2_consumed()}  K: {t3.lookup_kerroin()}  P: {t3.lookup_pisteet()} | {t3.lookup_airport()}, {t3.lookup_country()}
        +---------------------++---------------------++---------------------+ 
        |     Omat tiedot     |  Aktiivinen tehtava: {pelaaja.hae_current_tehtava_tiedot()}
        +---------------------++---------------------++---------------------+ 
        | Maa: {pelaaja.hae_pelaaja_Maa()}
        | Lentokenttä: {pelaaja.hae_pelaaja_lentokentta()}                                          
        | {pelaaja.co2_consumed}/{pelaaja.co2_budget}                                      
        | {pelaaja.pisteet}         
        +---------------------++---------------------++---------------------+ 
        """)

        print("Valitse : 1.Valikko, 2.Valitse tehtävä, 3.Siirry, 4. Kauppa  ")  # 4.Kauppa? Vois käyttää raha saada permanent buffs, esim. Co2 consumed halved, pelaaja.pisteet doubler, Co2 Budget doubler.
        valinta = input("")
        # Pelaajan valinta logiikka
        if valinta == "1":
            clear_console()
            pelaaja = valikko(pelaaja, items)
            continue

        # Tehtävän valinta
        elif valinta == "2":
            tehtava = input("Valitse tehtävä (1, 2, 3): ")
            if tehtava == "1":
                pelaaja.aseta_tehtava(t1)
            elif tehtava == "2":
                pelaaja.aseta_tehtava(t2)
            elif tehtava == "3":
                pelaaja.aseta_tehtava(t3)
            else:
                print(f"{tehtava} ei ole valinta.")

        elif valinta == "3":
            if pelaaja.current_tehtava:
                animate()
                clear_console()
                Tehtava.instance_count -= 3
                pelaaja.suorita_tehtava()

        elif valinta == "4":
            clear_console()
            kauppa_valikko(pelaaja, *items)


        if int(pelaaja.co2_consumed) >= int(pelaaja.co2_budget):
            game_over()
            sql_db_update_leaderboard(pelaaja.nimi, pelaaja.pisteet)
            sql_db_reset_game(pelaaja.id)
            print(f"\nLOPPU PISTEET: {pelaaja.pisteet}\n")
            input("Paina mitä tahansa nappia lopettaaksesi")
            sys.exit()


if __name__ == '__main__':
    asyncio.run(main())
