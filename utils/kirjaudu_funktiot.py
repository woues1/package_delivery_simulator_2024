from data.sql_db_update import sql_db_lookup_log_in, sql_db_update_new_game
import sys
from utils.pelilauta import art_exit_game





def kirjaudu_sisaan():#pitää päästä ulos jotenkin jos ei ole kayttjaa
    print("""
    Kirjaudu sisään
    Käyttäjänimi: 
    """)
    screen_name = str(input(""))#not case sensitive
    print("""
    Salasna:
    """)
    player_password = str(input(""))#password_player, alempaan hakuun
    user_id = sql_db_lookup_log_in(screen_name,player_password)# atm palauttaa game_id, en oo viel suunitellu miten se tarkistaa oikeuden
    if user_id != []:
        # db_tietojen haku
        print("Tervetuloa...")
        return user_id
    else:
        print("Wrong username or password...")
        return user_id


def uusi_peli():
    print("Uusi peli...")
    screen_name = str(input("Käyttäjätunnus: ?"))
    player_password = str(input("Salasana: ?"))
    # sql_db_update_new_game(screen_name, player_password) <--- On loutu, mutta puuttuu toimminnallisuus.
    return #game.id


def exit_game():
    art_exit_game()
    sys.exit()