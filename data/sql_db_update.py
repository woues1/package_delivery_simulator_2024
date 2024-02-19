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
    tulos = sql_search(f"SELECT screen_name, co2_consumed, location, co2_consumed "
                       f"FROM game "
                       f"WHERE id='{id}'")
    return tulos
def sql_db_update_new_game(screen_name, player_password): #HUOM!!!!älä kutsu tätä, ei valmis
    from data.sql_db_update import sql_db_lookup_random_location
    starting_location = sql_db_lookup_random_location()
    update_query =  (f"INSERT INTO game (co2_consumed, co2_budget, location, screen_name, password) "
                     f"VALUES (0, 10000, '{starting_location}', '{screen_name}', '{player_password}');")             #<---- Default starting location EFHK(Helsinki Vantaa),
    sql_search(update_query) #Game ID poistaminen jää haahuilee uudet game id tulee isomalla numerolla vaikka vanhat olis poistettu
    tulos = sql_db_lookup_log_in(screen_name, player_password)
    return tulos

def sql_db_lookup_random_location():
    locations = sql_db_lookup_locations()
    delivery_location = random.choice(locations)[0]
    return delivery_location

def sql_db_lookup_screen_names_money():
    tulos = sql_search(f"SELECT screen_name,co2_consumed FROM game;")
    return tulos

def sql_db_lookup_location_name(pelaaja_location):
    tulos = sql_search(f"SELECT a.name FROM airport a WHERE a.ident = '{pelaaja_location}';")
    return tulos
def sql_db_lookup_country_name(pelaaja_location):
    tulos = sql_search(f"SELECT c.name FROM country AS c JOIN airport AS a ON c.iso_country = a.iso_country WHERE a.ident = '{pelaaja_location}';")
    return tulos