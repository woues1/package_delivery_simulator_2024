from data.sql_db_update import sql_db_lookup_log_in, sql_db_update_new_game
import sys
from utils.pelilauta import art_exit_game





def kirjaudu_sisaan():
    print("""
    Kirjaudu sisään: \n 
    Käyttäjänimi: \n
    """)
    screen_name = str(input(""))
    print("""
    Salasna:\n
    """)
    password_player = str(input(""))#password_player, alempaan hakuun
    game_id = sql_db_lookup_log_in(screen_name)# atm palauttaa game_id, en oo viel suunitellu miten se tarkistaa oikeuden
    print(game_id) #<<----- Poista
    if game_id != []:
        # db_tietojen haku
        print("Tervetuloa...")
        return game_id
    else:
        print("Wrong username or password...")
        return game_id


def uusi_peli():
    print("Uusi peli...")
    screen_name = str(input("Käyttäjätunnus: ?"))
    player_password = str(input("Salasana: ?"))
    # sql_db_update_new_game(screen_name, player_password) <--- On loutu, mutta puuttuu toimminnallisuus.
    return


def exit_game():
    art_exit_game()
    sys.exit()