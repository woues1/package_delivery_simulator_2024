import random
from data.sql_db_update import sql_db_lookup_locations
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


locaation=generate_delivery_location()
print(locaation)