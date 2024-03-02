from utils.pelaaja import Item
from data.sql_db_query import sql_db_lookup_items


def kauppa_valikko(pelaaja):

    items = sql_db_lookup_items(pelaaja.id)
    print(items)
    item1 = Item(items[0][0], items[0][1], items[0][2], items[0][3], items[0][4])
    item2 = Item(items[1][0], items[1][1], items[1][2], items[1][3], items[1][4])
    item3 = Item(items[2][0], items[2][1], items[2][2], items[2][3], items[2][4])

    jatka = True
    while jatka:
        print("""
        +---------------------++---------------------++---------------------+ 
            Tervetuloa kauppaan!
        +---------------------++---------------------++---------------------+ 
        1.Osta
        2.Poistu
        """)
        valinta = input("")
        if valinta == "1":  # Pitäs olla tarkistukseet löytyykö tiettyä unlockaausta.
            print(f"""
            +---------------------++---------------------++---------------------+ 
              Tuote                     Hinta                  Ostettu
            +---------------------++---------------------++---------------------+ 
             1. Hybridi mersu             2000                    {item1.disply_info()}
             2. Päästö hujattu volkkari   4000                    {item2.disply_info()}   
             3. Rahan tuplaus kone        8000                    {item3.disply_info()}         
            """)
            valinta = input("")
            if valinta == "1":
                print(f"Haluatko ostaaa {item1.name}?: y/n")
                valinta = input("")
                if valinta == "y":
                    print(f"Ostit {item1.name}, Co2 päästösi on nytten tuplasti vähemmän")
                    item1.purchase(pelaaja.id)
                    pelaaja.add_item(item1)
                    # return jotenki co2_päästö 0.5 kertaa
                    # update.db
                    continue
                elif valinta == "n":
                    continue


            elif valinta == "2":
                print(f"Haluatko ostaaa {item2.name}?: y/n")
                valinta = input("")
                if valinta == "y":
                    print(f"Ostit {item2.name}, Co2 budjettisi on tuplasti isompi")
                    item2.purchase(pelaaja.id)
                    pelaaja.add_item(item2)
                    # return jotenki co2_budget == 20000
                    # update.db
                    continue
                elif valinta == "n":
                    continue


            elif valinta == "3":
                print(f"Haluatko ostaaa {item3.name}?: y/n")
                valinta = input("")
                if valinta == "y":
                    print(f"Ostit {item3.name}, saat tuplsi ennemänn rahaa")
                    item3.purchase(pelaaja.id)
                    pelaaja.add_item(item3)
                    # return jotenki pelaaja.pisteet *2
                    # update.db
                    continue
                elif valinta == "n":
                    continue


        elif valinta == "2":
            return jatka == False
