from data.sql_db_connect import sql_search


class Pelaaja:
    def __init__(self, nimi, pisteet, location):
        self.nimi = nimi
        self.pisteet = pisteet
        self.location = location


def kayttaja_haku():
    result = sql_search(f"SELECT screen_name, co2_budget, location "
                        f"FROM game "
                        f"where screen_name = 'ilkka'")
    return result


def olio_luonti():
    res = kayttaja_haku()
    for i in res:
        pelaaja = Pelaaja(i[0], i[1], i[2])
        print(pelaaja.nimi, pelaaja.pisteet, pelaaja.location)
    return pelaaja

asd = olio_luonti()