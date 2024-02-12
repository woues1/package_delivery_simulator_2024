#def sql_db_update_game_state():

#def sql_db_update_new_player():

#def sql_db_updaate_new_game():
from data.sql_db_connect import sql_search
def sql_db_lookup_locations():
    locations_serch= f"SELECT a.ident FROM airport a;"
    tulos_locations= sql_search(locations_serch)
    return tulos_locations