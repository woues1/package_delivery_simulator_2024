import random
from data.sql_db_connect import sql_Execute_Query


# <<LOOKUP QUERY's>>
def sql_db_lookup_items(player_id):
    items_search = (
        f"SELECT id, name, price, attribute, purchased "
        f"FROM Item "
        f"LEFT JOIN PlayerItem ON Item.id = PlayerItem.item_id "
        f"WHERE PlayerItem.player_id = {player_id};"
    )
    query_res = sql_Execute_Query(items_search)
    return query_res

print(sql_db_lookup_items("9"))

def sql_db_lookup_locations():  # etsii kaikki airport.ident arvot
    locations_search = f"SELECT a.ident FROM airport a;"
    tulos_locations = sql_Execute_Query(locations_search)
    return tulos_locations


def sql_db_lookup_airport_info(location):  # location on airport.ident
    locations_search = f"SELECT c.name, a.type, a.continent FROM country AS c JOIN airport AS a ON c.iso_country = a.iso_country WHERE a.ident = '{location}';"
    tulos_locations = sql_Execute_Query(locations_search)
    return tulos_locations


def sql_db_lookup_lat_long(location):  # location on airport.ident
    locations_search = f"SELECT a.latitude_deg, a.longitude_deg FROM airport a WHERE a.ident = '{location}';"
    tulos_locations = sql_Execute_Query(locations_search)
    return tulos_locations


def sql_db_lookup_log_in(screen_name, player_password):
    login_info = f"SELECT g.id FROM game g WHERE g.screen_name = '{screen_name}' AND g.password = '{player_password}';"
    user_id = sql_Execute_Query(login_info)
    return user_id


def sql_db_lookup_kayttaja_tiedot(id):
    tulos = sql_Execute_Query(f"SELECT screen_name, id, pisteet, location, co2_consumed, co2_budget "
                              f"FROM game "
                              f"WHERE id='{id}'")
    return tulos


def sql_db_lookup_random_location():
    locations = sql_db_lookup_locations()
    delivery_location = random.choice(locations)[0]
    return delivery_location


def sql_db_lookup_screen_names_pisteet():
    tulos = sql_Execute_Query(f"SELECT name, pisteet FROM leaderboard ORDER BY pisteet DESC LIMIT 5;")
    return tulos


def sql_db_lookup_location_name(pelaaja_location):
    tulos = sql_Execute_Query(f"SELECT a.name FROM airport a WHERE a.ident = '{pelaaja_location}';")
    return tulos


def sql_db_lookup_country_name(pelaaja_location):
    tulos = sql_Execute_Query(
        f"SELECT c.name FROM country AS c JOIN airport AS a ON c.iso_country = a.iso_country WHERE a.ident = '{pelaaja_location}';")
    return tulos


def sql_db_lookup_continent_in_location(location):
    tulos = sql_Execute_Query(f"SELECT a.continent FROM airport a WHERE a.ident = '{location}'; ")
    return tulos


# <<UPDATE QUERY's>>
def sql_db_update_exit_game(screen_name, player_co2_consumed, player_location, player_pisteet):
    update_query = (f"UPDATE game "
                    f"SET co2_consumed ='{player_co2_consumed}', location ='{player_location}', pisteet = '{player_pisteet}'"  # money
                    f"WHERE game.screen_name = '{screen_name}';")
    sql_Execute_Query(update_query)
    return None


def sql_db_update_new_game(screen_name, player_password):  # HUOM!!!!älä kutsu tätä, ei valmis
    starting_location = sql_db_lookup_random_location()
    update_query = (f"INSERT INTO game (co2_consumed, co2_budget, location, screen_name, password, pisteet) "
                    f"VALUES (0, 10000, '{starting_location}', '{screen_name}', '{player_password}', 0);")  # <---- Default starting location EFHK(Helsinki Vantaa),
    sql_Execute_Query(
        update_query)  # Game ID poistaminen jää haahuilee uudet game id tulee isomalla numerolla vaikka vanhat olis poistettu
    tulos = sql_db_lookup_log_in(screen_name, player_password)
    return tulos


def sql_db_update_leaderboard(nimi, pelaajan_pisteet):
    update_query = (f"INSERT INTO leaderboard (name, pisteet)"
                    f"VALUES ('{nimi}', {pelaajan_pisteet})")
    sql_Execute_Query(update_query)


def sql_db_update_purchased_items(item_id, player_id):
    query = (f"UPDATE PlayerItem SET purchased = TRUE "
             f"WHERE player_id = {player_id} "
             f"AND item_id = {item_id};"
             )
    sql_Execute_Query(query)


def sql_db_update_new_player_items(id):
    sql_Execute_Query(f"INSERT INTO PlayerItem(player_id, item_id, purchased) VALUES({id}, 1, FALSE);")
    sql_Execute_Query(f"INSERT INTO PlayerItem(player_id, item_id, purchased) VALUES({id}, 2, FALSE);")
    sql_Execute_Query(f"INSERT INTO PlayerItem(player_id, item_id, purchased) VALUES({id}, 3, FALSE);")
    sql_Execute_Query(f"INSERT INTO PlayerItem(player_id, item_id, purchased) VALUES({id}, 4, FALSE);")


# <<RESET GAME VALUE's>>
def sql_db_reset_game(pelaaja_id):
    starting_location = sql_db_lookup_random_location()
    reset_game = (f"UPDATE game "
                  f"SET co2_consumed = 0, co2_budget = 10000, pisteet = 0, location = '{starting_location}'"
                  f"WHERE id = {pelaaja_id};")
    sql_Execute_Query(reset_game)

    reset_items = (f"UPDATE PlayerItem "
                   f"SET purchased = 0 "
                   f"WHERE player_id = {pelaaja_id};")
    sql_Execute_Query(reset_items)
    return starting_location


def sql_db_lookup_screen_names(screen_name):
    tulos = (f"SELECT screen_name FROM game WHERE screen_name = '{screen_name}';")
    tulos1 = sql_Execute_Query(tulos)
    return tulos1

def sql_db_update_pisteet(pelaaja_id, pisteet):
    update_query = (f"UPDATE game "
                    f"SET pisteet = pisteet + {pisteet} "
                    f"WHERE id = '{pelaaja_id}';")
    sql_Execute_Query(update_query)

