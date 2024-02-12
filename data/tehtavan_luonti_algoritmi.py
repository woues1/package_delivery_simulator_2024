import random
from geopy import distance
from data.sql_db_update import sql_db_lookup_locations, sql_db_lookup_lat_long
from utils.pelaaja import olio_luonti
pelaaja = olio_luonti()


def generate_delivery_location():
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


location = generate_delivery_location()
print(location)

def kerroin_maaarittaj(location):
    kerroin = 0
    current_location = sql_db_lookup_lat_long(pelaaja.location)
    destintion = sql_db_lookup_lat_long(location)
    print(current_location, destintion)#poista
    distance_to_location = distance.distance(current_location, destintion).km
    print(distance_to_location)#poista
    co2_consumed = distance_to_location // 10
    print(co2_consumed)#poista
    return co2_consumed
    #co2_budget-co2_consumed=new co2 budget
    #1 co2 == 10km
    #if distance > 500
    #kerroin =+2
kerroin_maaarittaj(location)