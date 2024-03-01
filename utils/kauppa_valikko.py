from utils.pelaaja import Item


def kauppa_valikko(pelaaja):
    item1 = Item("Hybridi mersu", 2000, 0.5)
    item2 = Item("Päästö hujattu volkkari", 4000, 20000)
    item3 = Item("Rahan tuplaus kone", 8000, 2)

    
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
                    pelaaja.lisaa_item(item1.attribute)
                    item1.purchase()
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
                    pelaaja.lisaa_item(item2.attribute)
                    item2.purchase()
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
                    item3.purchase()
                    pelaaja.lisaa_item(item3.attribute)
                    # return jotenki pelaaja.pisteet *2
                    # update.db
                    continue
                elif valinta == "n":
                    continue


        elif valinta == "2":
            return jatka == False
