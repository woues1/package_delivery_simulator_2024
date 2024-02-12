import random
from utils.pelaaja import olio_luonti, Pelaaja
pelaaja = olio_luonti()


def generate_delivery_location():
    print(pelaaja.location)

generate_delivery_location()