from utils.pelaaja import Item
from data.sql_db_query import sql_db_lookup_items
import os


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033c", end="")


def kauppa_valikko(pelaaja, item1, item2, item3):
    jatka = True
    while jatka:
        print("""
        +---------------------++---------------------++---------------------+ 
                                 Tervetuloa kauppaan!
        +---------------------++---------------------++---------------------+ 
        """)
        print(f"""
        +---------------------++---------------------++---------------------+ 
          Tuote                     Hinta                  Ostettu
        +---------------------++---------------------++---------------------+ 
        1. Hybridi mersu             2000                    {item1.disply_info()}
        2. Päästö hujattu volkkari   4000                    {item2.disply_info()}   
        3. Rahan tuplaus kone        8000                    {item3.disply_info()}    
             
        kirjoita 'back' jos haluat takaisin     
        """)

        valid_inputs = ['1', '2', '3']
        valinta = input("")

        if valinta.lower() == "back":
            return jatka == False
        elif valinta in valid_inputs:
            if valinta == "1":
                print(f"Haluatko ostaa {item1.name}?: y/n")
                valinta = input("")
                if valinta == "y":
                    if item1.purchase(pelaaja) == True:
                        print(f"Ostit {item1.name}, Co2 päästösi on nytten tuplasti vähemmän")
                        item1.purchase(pelaaja)
                        pelaaja.add_item(item1)
                    else:
                        print(item1.purchase(pelaaja))
                    continue
                elif valinta == "n":
                    continue


            elif valinta == "2":
                print(f"Haluatko ostaa {item2.name}?: y/n")
                valinta = input("")
                if valinta == "y":
                    if item2.purchase(pelaaja) == True:
                        print(f"Ostit {item2.name}, Co2 budjettisi on tuplasti isompi")
                        pelaaja.add_item(item2)
                    else:
                        print(item2.purchase(pelaaja))
                    continue
                elif valinta == "n":
                    continue


            elif valinta == "3":
                print(f"Haluatko ostaa {item3.name}?: y/n")
                valinta = input("")
                if valinta == "y":
                    if item3.purchase(pelaaja) == True:
                        print(f"Ostit {item3.name}, saat tuplasti ennemän rahaa")
                        pelaaja.add_item(item3)
                    else:
                        print(item3.purchase(pelaaja))
                    continue
                elif valinta == "n":
                    continue
        else:
            clear_console()
