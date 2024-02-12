import random
from data.sql_db_update import sql_db_lookup_locations, sql_db_lookup_airport_info
from utils.pelaaja import olio_luonti
pelaaja = olio_luonti()


def generate_delivery_location():
    from utils.pelaaja import olio_luonti
    pelaaja = olio_luonti()
    current_location = pelaaja.location
    locations = sql_db_lookup_locations()
    if locations:
        delivery_location = random.choice(locations)[0]
        if current_location == delivery_location:
            generate_delivery_location()
        return delivery_location
    else:
        return None


location = generate_delivery_location()
print(location)

def kerroin_maaarittaj(location):
    airport_location_info = sql_db_lookup_airport_info(location)
    a_continent = airport_location_info[0][0]
    a_type = airport_location_info[0][1]
    a_country = airport_location_info[0][2]

    print(a_continent, a_type, a_country)
    #if airport.type closed = generate_delivery_location()
    #values =
kerroin_maaarittaj(location)