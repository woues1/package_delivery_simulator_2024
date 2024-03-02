#def sql_db_update_game_state():
import random
from data.sql_db_connect import sql_search
def sql_db_lookup_locations():#etsii kaikki airport.ident arvot
    locations_search = f"SELECT a.ident FROM airport a;"
    tulos_locations = sql_search(locations_search)
    return tulos_locations


def sql_db_lookup_airport_info(location):#location on airport.ident
    locations_search = f"SELECT c.name, a.type, a.continent FROM country AS c JOIN airport AS a ON c.iso_country = a.iso_country WHERE a.ident = '{location}';"
    tulos_locations = sql_search(locations_search)
    return tulos_locations


def sql_db_lookup_lat_long(location):#location on airport.ident
    locations_search = f"SELECT a.latitude_deg, a.longitude_deg FROM airport a WHERE a.ident = '{location}';"
    tulos_locations = sql_search(locations_search)
    return tulos_locations


def sql_db_lookup_log_in(screen_name, player_password):
    locations_search = f"SELECT g.id FROM game g WHERE g.screen_name = '{screen_name}' AND g.password = '{player_password}';"
    user_id = sql_search(locations_search)
    return user_id


def sql_db_lookup_kayttaja_tiedot(id):
    tulos = sql_search(f"SELECT screen_name, password, pisteet, location, co2_consumed, co2_budget "
                       f"FROM game "
                       f"WHERE id='{id}'")
    return tulos


def sql_db_lookup_random_location():
    locations = sql_db_lookup_locations()
    delivery_location = random.choice(locations)[0]
    return delivery_location


def sql_db_lookup_screen_names_money():
    tulos = sql_search(f"SELECT name, pisteet FROM leaderboard;")
    return tulos


def sql_db_lookup_location_name(pelaaja_location):
    tulos = sql_search(f"SELECT a.name FROM airport a WHERE a.ident = '{pelaaja_location}';")
    return tulos


def sql_db_lookup_country_name(pelaaja_location):
    tulos = sql_search(f"SELECT c.name FROM country AS c JOIN airport AS a ON c.iso_country = a.iso_country WHERE a.ident = '{pelaaja_location}';")
    return tulos


def sql_db_lookup_continent_in_location(location):
    tulos = sql_search(f"SELECT a.continent FROM airport a WHERE a.ident = '{location}'; ")
    return tulos


def sql_db_update_exit_game(screen_name, player_co2_consumed,player_location, player_pisteet):
    update_query = (f"UPDATE game "
                    f"SET co2_consumed ='{player_co2_consumed}', location ='{player_location}', pisteet = '{player_pisteet}'"#money
                    f"WHERE game.screen_name = '{screen_name}';")
    sql_search(update_query)
    return None


def sql_db_update_new_game(screen_name, player_password): #HUOM!!!!älä kutsu tätä, ei valmis
    from data.sql_db_query import sql_db_lookup_random_location
    starting_location = sql_db_lookup_random_location()
    update_query =  (f"INSERT INTO game (co2_consumed, co2_budget, location, screen_name, password, pisteet) "
                     f"VALUES (0, 10000, '{starting_location}', '{screen_name}', '{player_password}', 0);")             #<---- Default starting location EFHK(Helsinki Vantaa),
    sql_search(update_query) #Game ID poistaminen jää haahuilee uudet game id tulee isomalla numerolla vaikka vanhat olis poistettu
    tulos = sql_db_lookup_log_in(screen_name, player_password)
    return tulos


def sql_db_update_reset_game(pelaaja_nimi, pelaaja_salasana):
    starting_location = sql_db_lookup_random_location()
    update_query = (f"UPDATE game "
                    f"SET co2_consumed = 0, co2_budget = 10000, pisteet = 0, location = '{starting_location}'"
                    f"WHERE screen_name = '{pelaaja_nimi}' AND password = '{pelaaja_salasana}';")
    sql_search(update_query)


def sql_db_update_leaderboard(nimi, pelaajan_pisteet):
    update_query = (f"INSERT INTO leaderboard (name, pisteet)"
                    f"VALUES ('{nimi}', {pelaajan_pisteet})")
    sql_search(update_query)
