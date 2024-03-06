import re
import sys
from Assets.ASCII_art import art_exit_game
from data.sql_db_query import *


def kirjaudu_sisaan():
    print("""
    Kirjaudu sisään (kirjoita 'back' jos haluat takaisin)
    Käyttäjänimi: 
    """)
    screen_name = input("")
    if re.search(r'[\'\"]', screen_name):
        print("\nEpäkelpo merkki käyttäjänimessä. Yritä uudelleen käyttämättä ' tai \".\n")
        return []
    elif screen_name.lower() == "back":
        return "back"

    print("""
    Salasana:
    """)
    player_password = input("")
    if re.search(r'[\'\"]', player_password):
        print("\nEpäkelpo merkki salasanassa. Yritä uudelleen käyttämättä ' tai \".\n")
        return []

    user_id = sql_db_lookup_log_in(screen_name, player_password)
    if user_id:
        print("Tervetuloa...")
        return user_id
    else:
        print("Väärä käyttäjänimi tai salasana")
        return []


def uusi_peli():  # jos sama screen_name , antaa error
    print(f"luo käyttäjä...\n")
    screen_name = input("Käyttäjätunnus: ?")
    screen_names = sql_db_lookup_screen_names(screen_name)
    if screen_names != []:
        print("Käyttäjänimi on jo käytössä!")
        return []

    if re.search(r'[\'\"]', screen_name):
        print("\nEpäkelpo merkki käyttäjänimessä. Yritä uudelleen käyttämättä ' tai \".\n")
        return []

    player_password = input("Salasana: ?")
    if re.search(r'[\'\"]', player_password):
        print("\nEpäkelpo merkki salasanassa. Yritä uudelleen käyttämättä ' tai \".\n")
        return []

    user_id = sql_db_update_new_game(screen_name,
                                     player_password)  # <--- On loutu, mutta puuttuu toiminnallisuus.
    if user_id:
        sql_db_update_new_player_items(user_id[0][0])
        return user_id
    else:
        print("Virhe uuden pelin luonnissa. Yritä uudelleen")


def exit_game():
    art_exit_game()
    sys.exit()


# game.ids
# game.pisteet
def leaderboard_menu():
    while True:
        results = sql_db_lookup_screen_names_pisteet()
        print("""
+------------------------------------------+
|               Leaderboard               |
+------------------------------------------+
   Nimi:        Pisteet:
    """)
        for index, (name, money) in enumerate(results, start=1):
            print(f"| {index}. {name:10} | {money:10} |")
        print("kirjoita back päästäksesi takaisin...")
        valinta = str(input(""))
        if valinta == "back":
            return "back"
        else:
            continue


def tutorial():
    print(f"""
    Tervetualoa Package Delivery Simulator 2024! Aloitat pelin satunnaisesta lentokentästä maailmalla.\n
    Jokaisesta lentokenttästä löytyy kolme eri tehtävää kolmeen eri lentokenttään.\n
    Sinun tehtävä on toimittaa paketteja ympäri maailmaa, ja kerätä niin paljon pisteitä kun mahdollista!\n
    Mutta muista, sinulla on Co2 budjetti mitä pitää noudattaa. Kun olet käyttäny budjettisi kokonaisuudesaan.\n
    Peli päättyy ja sinun pisteet kirjataan tulostaulukkoon.!\n
    Kilpaile kavereittesi kanssa ja katso kuka saa eniten pisteitä!\n
    Onnea matkaan!\n
    """)
