from data.sql_db_query import *

# tehtava1 = Tehtava(location="Location1", co2_consumed=5, multiplier=2) <-- näin luodaan tehtävä

# pelaaja.current_tehtava = tehtava1 <-- tällä annetaan pelaajalle tehtävä

# pelaaja.suorita_tehtava() <-- tällä komennolla pelaaja suorittaa tehtävän


# pelaajan tiedot
class Pelaaja:
    def __init__(self, nimi, salasana, pisteet, location, co2_consumed, co2_budget):
        self.nimi = nimi
        self.salasana = salasana
        self.pisteet = pisteet
        self.location = location
        self.co2_consumed = co2_consumed
        self.tehtava_aktiivinen = False
        self.current_tehtava = []
        self.Tehtavat = []
        self.Items = []
        self.co2_budget = co2_budget
        self.co2_kerroin = 1.0
        self.piste_kerroin = 1.0

    def paivita_tehtava_aktiivinen(self, is_active):
        self.tehtava_aktiivinen = is_active

    def paivita_pisteet(self, piste_maara, tehtava_kerroin):
        self.pisteet += piste_maara * (tehtava_kerroin * self.piste_kerroin)

    def paivita_co2_kulutettu(self, co2_consumed):
        self.co2_consumed += co2_consumed * self.co2_kerroin

    def paivita_sijainti(self, location):
        self.location = location

    def lisaa_tehtava(self, tehtava):
        self.Tehtavat.append(tehtava)

    def lisaa_item(self, items):
        self.Items.append(items)

    def add_item(self, item):
        self.Items.append(item)
        if item.name == "Hybridi mersu":
            self.co2_kerroin *= item.attribute_value
        elif item.name == "point_multiplier":
            self.piste_kerroin *= item.attribute_value

    def aseta_tehtava(self, tehtava):
        if not self.tehtava_aktiivinen:
            self.current_tehtava = tehtava
            self.paivita_tehtava_aktiivinen(True)
        if self.current_tehtava:
            self.current_tehtava = []
            self.current_tehtava = tehtava
            self.paivita_tehtava_aktiivinen(True)

    def suorita_tehtava(self):
        if self.tehtava_aktiivinen and self.current_tehtava:
            self.paivita_sijainti(self.current_tehtava.location)
            self.paivita_pisteet(self.current_tehtava.piste_maara, self.current_tehtava.multiplier) # Lisätty psite_maara VE
            self.paivita_co2_kulutettu(self.current_tehtava.co2_consumed)
            self.paivita_tehtava_aktiivinen(False)
            self.current_tehtava = None

    def hae_current_tehtava_tiedot(self):
        if self.current_tehtava:
            location = sql_db_lookup_location_name(self.current_tehtava.location)
            return f"Maa: {location[0][0]} | Co2 kulutus: {self.current_tehtava.co2_consumed}"
        else:
            return "Tehtävää ei ole valittu"

    def hae_pelaaja_Maa(self):
        player_country = sql_db_lookup_country_name(self.location)
        return f"Maa: {player_country[0][0]}"
    def hae_pelaaja_lentokentta(self):
        player_location_print = sql_db_lookup_location_name(self.location)
        return f"Lentokenttä: {player_location_print[0][0]}"

def kayttaja_haku(id):
    tulos = sql_db_lookup_kayttaja_tiedot(id)
    return tulos


def olio_luonti(id):
    res = kayttaja_haku(id)
    for i in res:
        pelaaja = Pelaaja(i[0], i[1], i[2], i[3], i[4], i[5])
        return pelaaja


class Item:
    def __init__(self, name, price, attribute):
        self.name = name    
        self.price = price
        self.attribute = attribute
        self.purchased = False

    def purchase(self):
        self.purchased = True

    def disply_info(self):
        purchased_status = "X" if self.purchased else ""
        return purchased_status


class Tehtava:
    def __init__(self, location, co2_consumed, multiplier, piste_maara):#Lisätty pisteet VE
        self.location = location
        self.co2_consumed = co2_consumed
        self.multiplier = multiplier
        self.piste_maara = piste_maara #lisätty VE

    def lookup_country(self):
        country = sql_db_lookup_country_name(self.location)
        return country[0][0]

    def lookup_airport(self):
        airport = sql_db_lookup_location_name(self.location)
        return airport[0][0]

    def lookup_pisteet(self):
        return self.piste_maara

    def lookup_co2_consumed(self):
        co2_info = self.co2_consumed
        return co2_info

    def lookup_kerroin(self):
        kerroin_info = self.multiplier
        return kerroin_info