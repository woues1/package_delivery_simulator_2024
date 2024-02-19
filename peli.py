from utils.kirjaudu import main_menu
from data.Tehtävät import *
from utils.pelaaja import *
from utils.valikko import valikko


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
        +------------------------------------------+
        |Tehtävät(Airport, Co2 Consumed, kerroin)  |
        +------------------------------------------+
        1.{t1}
        2.{t2} 
        3.{t3} 
        +---------------------+ 
        |     Omat tiedot     |  
        +---------------------+ 
               Country                                              
                {pelaaja.location}                                  
            {pelaaja.co2_consumed}/10000                                      
                {pelaaja.pisteet}         
        +---------------------+ 
        """)
    valintaa = input("Valitse : 1.Vallikko, 2.Valitse tehtävä , 3.Siirry  ")#4.Kauppa? Vois käyttää raha saada permanent buffs, esim. Co2 consumed halved, pelaaja.pisteet doubler, Co2 Budget doubler.
    if valintaa == "1":
        valikko(pelaaja)
    #tehtava = Tehtava(t1[0],t1[1],t1[2])
    #pelaaja.aseta_tehtava(tehtava)
    #pelaaja.suorita_tehtava()



if __name__ == '__main__':
    main()
