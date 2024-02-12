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

def co2_consumed_distance(location):
    current_location = sql_db_lookup_lat_long(pelaaja.location)
    destintion = sql_db_lookup_lat_long(location)
    print(current_location, destintion)#poista
    distance_to_location = distance.distance(current_location, destintion).km
    print(distance_to_location)#poista
    co2_consumed = distance_to_location // 10 #co2_budget-co2_consumed=new co2 budget , 1 co2 == 10km
    print(co2_consumed)#poista
    return co2_consumed

co2_consumed_distance(location)
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
    print(kerroin)#poista
    return kerroin

kerroin_maarittaja(co2_consumed_distance(location))



