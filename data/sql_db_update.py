#def sql_db_update_game_state():

#def sql_db_update_new_player():

#def sql_db_updaate_new_game():
from data.sql_db_connect import sql_search
def sql_db_lookup_locations():#etsii kaikki airport.ident arvot
    locations_search = f"SELECT a.ident FROM airport a;"
    tulos_locations = sql_search(locations_search)
    return tulos_locations
def sql_db_lookup_airport_info(location):#location on airport.ident
    locations_search = f"SELECT c.name, a.type, a.continent FROM country AS c JOIN airport AS a ON c.iso_country = a.iso_country WHERE a.ident = '{location}';"
    tulos_locations = sql_search(locations_search)
    return tulos_locations
def sql_db_lookup_lat_long(location):
    locations_search = f"SELECT a.latitude_deg, a.longitude_deg FROM airport a WHERE a.ident = '{location}';"
    tulos_locations = sql_search(locations_search)
    return tulos_locations
def sql_db_lookup_log_in(screen_name):#player_password
    locations_search = f"SELECT g.id FROM game g WHERE g.screen_name = '{screen_name}';" # AND g.password = '{password_player}'
    game_id = sql_search(locations_search)
    return game_id