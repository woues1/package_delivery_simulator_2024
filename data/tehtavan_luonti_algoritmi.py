import random
from geopy import distance
from data.sql_db_update import sql_db_lookup_locations, sql_db_lookup_lat_long
from utils.pelaaja import olio_luonti


def generate_delivery_location(pelaaja):
    current_location = pelaaja.location
    locations = sql_db_lookup_locations()
    if locations:
        delivery_location = random.choice(locations)[0]
        if current_location == delivery_location:
            generate_delivery_location()
        else:
            return delivery_location
    else:
        return None


def co2_consumed_distance(location, pelaaja):
    current_location = sql_db_lookup_lat_long(pelaaja.location)
    destintion = sql_db_lookup_lat_long(location)
    distance_to_location = distance.distance(current_location, destintion).km
    co2_consumed = distance_to_location // 10 #co2_budget-co2_consumed=new co2 budget , 1 co2 == 10km
    return co2_consumed


def kerroin_maarittaja(co2_consumed):
    kerroin = 0
    if co2_consumed < 50: #if distance > 500
        kerroin += 1 #kerroin =+2
    elif co2_consumed >100 and co2_consumed <200:
        kerroin += 2
    elif co2_consumed > 200 and co2_consumed<400:
        kerroin += 4
    elif co2_consumed > 400 and co2_consumed <800:
        kerroin += 8
    elif co2_consumed > 800:
        kerroin += 16
    else:
        kerroin += 16
    return kerroin
