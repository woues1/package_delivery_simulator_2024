from data.sql_db_query import sql_db_lookup_log_in, sql_db_update_new_game, sql_db_lookup_screen_names_pisteet, sql_db_lookup_items
import sys
from utils.pelilauta import art_exit_game
from utils.pelaaja import Item




def kirjaudu_sisaan():# pitää päästä ulos jotenkin jos ei ole kayttjaa
    print("""
    Kirjaudu sisään (kirjoita 'back' jos haluat takaisin)
    Käyttäjänimi: 
    """)
    screen_name = str(input(""))
    if screen_name == "back":
        return "back"
    print("""
    Salasna:
    """)
    player_password = str(input(""))# how to make input star?
    user_id = sql_db_lookup_log_in(screen_name, player_password)
    if user_id != []:
        print("Tervetuloa...")
        return user_id
    else:
        print("Wrong username or password...")
        return user_id


def uusi_peli():
    print("Uusi peli...")
    screen_name = str(input("Käyttäjätunnus: ?"))
    player_password = str(input("Salasana: ?"))
    user_id = sql_db_update_new_game(screen_name, player_password) #<--- On loutu, mutta puuttuu toimminnallisuus.
    return user_id


def exit_game():
    art_exit_game()
    sys.exit()

#game.ids
#game.money
def leaderboard_menu():
    while True:
        results = sql_db_lookup_screen_names_pisteet()
        sorted_results = sorted(results, key=lambda x: x[1], reverse=True)
        print(f"""
+------------------------------------------+
|               Leaderboard               |
+------------------------------------------+
   Name:        Pisteet
    """)
        for index, (name, money) in enumerate(sorted_results, start=1):
            print(f"| {index}. {name:10} | {money:10} |")
        print("Input back to get back...")
        valinta = str(input(""))
        if valinta == "back":
            return "back"
        else:
            continue

