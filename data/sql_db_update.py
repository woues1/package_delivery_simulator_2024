#def sql_db_update_game_state():


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
def sql_db_update_new_game(screen_name, player_password):
    update_query =  (f"INSERT INTO game (co2_consumed, co2_budget, screen_name, location, password)" #<--Password ei vielä lisätty DB
                     f"VALUES (0, 10000, '{screen_name}','EFHK', '{player_password}');")             #<---- Default starting location EFHK(Helsinki Vantaa)
    tulos = sql_search(update_query)
    return tulos