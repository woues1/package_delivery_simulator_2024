from utils.kirjaudu import main_menu
from data.Tehtävät import *
from utils.pelaaja import *


def main():
    pelaaja = main_menu()
    print(pelaaja.nimi)

    # toimiva tehtävän luonti

    t1 = luo_tehtava(pelaaja)
    t2 = luo_tehtava(pelaaja)
    t3 = luo_tehtava(pelaaja)
    lista = [t1,t2,t3]
    print(*lista[0])
    print(f"""

        +---------------------+ +------------------------------------------+
        |     Omat tiedot     | | Tehtävät(Airport, Co2 Consumed, kerroin) |
        +---------------------+ +------------------------------------------+
        |       Country       |    1.{t1}                                   
        |       airport       |    2.{t2}                                   
        | Co2_consumed/10000  |    3.{t3}                                   
        |        Money        | 
        +---------------------+ 
        """)

    tehtava = Tehtava(t1[0],t1[1],t1[2])
    pelaaja.aseta_tehtava(tehtava)
    pelaaja.suorita_tehtava()



if __name__ == '__main__':
    main()
