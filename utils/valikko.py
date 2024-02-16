
"""
def valikko():
    print("MAIN MENU PLACEHOLDER")
    print("PELAAJAN TIEDOT(pisteet, co2 budjetti jne.)")

    print("UUSI PELI (poistaa nykyisen pelitiedoston ja aloittaa uudestaan)")

    print("LOPETA PELI(nappi)")

"""
from utils.pelaaja import olio_luonti
def valikko(pelaaja):
    import sys
    print(pelaaja.pisteet,pelaaja.nimi,pelaaja.location)
    while True:
        valinta = input("""
        +--------------------+
        Valitse
        +--------------------+
        1. Uusi peli...
        2. Tallenna ja poistu
        3. Takaisin...
        +--------------------+
        """)
        if valinta == "1":
            #update.db
            print("uusi peli")#<----No clue mitetn tää pitäs tehä
        elif valinta== "2":
            print("Lopetetaan peli...")
            #update.db
            sys.exit()
        elif valinta == "3":
            print("Main")
            return valikko(pelaaja)

