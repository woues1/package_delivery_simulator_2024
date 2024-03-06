from geopy import distance
from data.sql_db_query import *
from utils.pelaaja import Tehtava


def luo_tehtava(pelaaja):
    location = generate_delivery_location(pelaaja)
    co2_consumed = co2_consumed_distance(location, pelaaja)
    kerroin = kerroin_maarittaja(co2_consumed)
    pisteet = piste_maarittaja(location)
    tehtava = Tehtava(location, co2_consumed, kerroin, pisteet)
    return tehtava


def generate_delivery_location(pelaaja):
    while True:
        delivery_location = sql_db_lookup_random_location()
        if pelaaja.location == delivery_location:
            continue
        else:
            return delivery_location


def co2_consumed_distance(location, pelaaja):
    current_location = sql_db_lookup_lat_long(pelaaja.location)
    destintion = sql_db_lookup_lat_long(location)
    distance_to_location = distance.distance(current_location, destintion).km
    co2_consumed = distance_to_location // 10  # co2_budget-co2_consumed=new co2 budget , 1 co2 == 10km
    return co2_consumed


def kerroin_maarittaja(co2_consumed):
    kerroin = 0
    if co2_consumed < 50:  # if distance > 500
        kerroin += 1  # kerroin =+2
    elif co2_consumed > 100 and co2_consumed < 200:
        kerroin += 2
    elif co2_consumed > 200 and co2_consumed < 400:
        kerroin += 4
    elif co2_consumed > 400 and co2_consumed < 800:
        kerroin += 8
    elif co2_consumed > 800:
        kerroin += 16
    else:
        kerroin += 16
    return kerroin


def piste_maarittaja(location):
    continent = sql_db_lookup_continent_in_location(location)
    if continent[0][0] == "EU":
        return 10
    elif continent[0][0] == "AF":
        return 40
    elif continent[0][0] == "AS":
        return 30
    elif continent[0][0] == "NA":
        return 10
    elif continent[0][0] == "OC":
        return 50
    elif continent[0][0] == "SA":
        return 40
    else:
        return 60
