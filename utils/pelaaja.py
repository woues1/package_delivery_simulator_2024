from data.sql_db_connect import sql_search


class Pelaaja:
    def __init__(self, nimi, pisteet, location):
        self.nimi = nimi
        self.pisteet = pisteet
        self.location = location


# Päivittää käyttäjän pistemäärän.
    def suoritus_piste_lisays(self, pisteet, piste_kerroin):
        self.pisteet = self.pisteet + pisteet * piste_kerroin


def kayttaja_haku():
    result = sql_search(f"SELECT screen_name, co2_budget, location "
                        f"FROM game "
                        f"where screen_name = 'ilkka'")
    return result


def olio_luonti():
    res = kayttaja_haku()
    for i in res:
        return Pelaaja(i[0], i[1], i[2])


pelaaja_instanssi = olio_luonti()


# pelaaja_instanssin tietojen haku
print(f"\n{pelaaja_instanssi.nimi} {pelaaja_instanssi.location} {pelaaja_instanssi.pisteet}")

# Käyttää olioa pisteiden lisäämiseen pelaaja_instanssille
pelaaja_instanssi.suoritus_piste_lisays(1000, 1.2)

print(f"\npäivitettyjen pisteiden määrä: {pelaaja_instanssi.pisteet}")