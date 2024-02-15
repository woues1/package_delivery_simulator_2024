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
        +------------------------------------------+
        |Tehtävät(Airport, Co2 Consumed, kerroin)  |
        +------------------------------------------+
        1.{t1}
        2.{t2} 
        3.{t3} 
        +---------------------+ 
        |     Omat tiedot     |  
        +---------------------+ 
        |       Country       |                                       
        |       airport       |                                      
        |      {pelaaja.co2_consumed}/10000     |                                 
        |        Money        | 
        +---------------------+ 
        """)


if __name__ == '__main__':
    main()
