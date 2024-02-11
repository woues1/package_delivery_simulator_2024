import keyboard
from utils.pelaaja import Pelaaja, kayttaja_haku, olio_luonti
# import utils.pelilauta
from utils.ohjaus import kbdCallback
from data.Tehtävät import luo_tehtava, valitse_tehtava, tulosta_tehtava


max_pisteet = 10000
pisteet = 10000


def main():
    kayttaja_haku()
    pelaaja = olio_luonti()
    while True:

        if pelaaja.tehtava_aktiivinen:
            pass

        else:
            tehtavat = luo_tehtava()
            tulosta_tehtava(tehtavat)
            valitse_tehtava(tehtavat, pelaaja)

        if pisteet > max_pisteet:
            quit()


if __name__ == '__main__':
    main()
