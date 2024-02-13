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
def sql_db_lookup_lat_long(location):#location on airport.ident
    locations_search = f"SELECT a.latitude_deg, a.longitude_deg FROM airport a WHERE a.ident = '{location}';"
    tulos_locations = sql_search(locations_search)
    return tulos_locations
def sql_db_lookup_log_in(screen_name):#(player_password) ei ole vielä
    locations_search = f"SELECT g.id FROM game g WHERE g.screen_name = '{screen_name}';" # AND g.password = '{password_player}'
    user_id = sql_search(locations_search)
    return user_id
def sql_db_lookup_kayttaja_tiedot(screen_name, salasana):
    tulos = sql_search(f"SELECT screen_name, co2_consumed, location, co2_budget "
                       f"FROM game "
                       f"WHERE screen_name = 'ilkka'")
    return tulos
def sql_db_update_new_game(screen_name, player_password): #HUOM!!!!älä kutsu tätä, ei valmis
    update_query =  (f"INSERT INTO game (co2_consumed, co2_budget, screen_name, location, password)" #<--Password ei vielä lisätty DB
                     f"VALUES (0, 10000, '{screen_name}','EFHK', '{player_password}');")             #<---- Default starting location EFHK(Helsinki Vantaa),
    tulos = sql_search(update_query)                                                                 #Voi käyttää samaaa tehtavan generointii ett saais RNG starting location.
    return tulos