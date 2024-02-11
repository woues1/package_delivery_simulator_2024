import keyboard
from utils.pelaaja import olio_luonti
# import utils.pelilauta
from utils.ohjaus import kbdCallback
from data.Tehtävät import luo_tehtava, valitse_tehtava, tulosta_tehtava
from utils.pelilauta import art_kartta, art_title_screen


def main():
    pelaaja = olio_luonti()
    while True:

        if pelaaja.tehtava_aktiivinen:
            pass

        else:
            tehtavat = luo_tehtava()
            tulosta_tehtava(tehtavat)
            valitse_tehtava(tehtavat, pelaaja)


if __name__ == '__main__':
    main()
