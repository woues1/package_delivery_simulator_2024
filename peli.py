from utils.kirjaudu import main_menu
from data.Tehtävät import *


def main():
    pelaaja = main_menu()
    print(pelaaja.nimi)

    # toimiva tehtävän luonti

    t1 = luo_tehtava(pelaaja)
    t2 = luo_tehtava(pelaaja)
    t3 = luo_tehtava(pelaaja)
    lista = [t1,t2,t3]
    print(lista)


if __name__ == '__main__':
    main()
