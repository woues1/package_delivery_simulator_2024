import keyboard
from utils.pelaaja import olio_luonti
# import utils.pelilauta
from data.Tehtävät import luo_tehtava, valitse_tehtava, tulosta_tehtava
from utils.pelilauta import art_kartta, art_title_screen

def main():
    # kirjaudu()
    pelaaja = olio_luonti()
    # alku_menu()
    while True:

        if pelaaja.tehtava_aktiivinen:
            # Valitse_lentokohde()
            continue

        else:
            tehtavat = luo_tehtava()
            tulosta_tehtava(tehtavat)
            valitse_tehtava(tehtavat, pelaaja)


if __name__ == '__main__':
    main()
