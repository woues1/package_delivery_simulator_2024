def kauppa_valikko(pelaaja):
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
        if valinta == "1":# Pitäs olla tarkistukseet löytyykö tiettyä unlockaausta.
            print(f"""
            +---------------------++---------------------++---------------------+ 
              Tuote                     Hinta                  Ostettu
            +---------------------++---------------------++---------------------+ 
             1. Hybridi mersu             2000                 
             2. Päästö hujattu volkkari   4000                  
             3. Rahan tuplaus kone        8000                       
            """)
            valinta = input("")
            if valinta == "1":
                print("Haluatko ostaaa Hybridi mersun?: y/n")
                valinta = input("")
                if valinta == "y":
                    print("Ostit Hybridi mersun, Co2 päästösi on nytten tuplasti vähemmän")
                    #update.db
                    continue
                elif valinta == "n":
                    continue
        elif valinta == "2":
            return jatka == False