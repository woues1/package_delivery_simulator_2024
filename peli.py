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
    print(f"""

        +---------------------+ +------------------------------------------+
        |     Omat tiedot     | | Tehtävät(Airport, Co2 Consumed, kerroin) |
        +---------------------+ +------------------------------------------+
        |       Country       | |   {t1}                                   |
        |       airport       | |   {t2}                                   |
        | Co2_consumed/budget | |   {t3}                                   |
        |        Money        | +------------------------------------------+
        +---------------------+ 
        """)


if __name__ == '__main__':
    main()
