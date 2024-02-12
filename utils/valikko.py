
"""
def valikko():
    print("MAIN MENU PLACEHOLDER")
    print("PELAAJAN TIEDOT(pisteet, co2 budjetti jne.)")

    print("UUSI PELI (poistaa nykyisen pelitiedoston ja aloittaa uudestaan)")

    print("LOPETA PELI(nappi)")

"""

def valikko(pelaaja):
    from utils.pelaaja import olio_luonti
    import keyboard
    import sys
    from utils.pelilauta import art_new_game,art_exit_game,art_gane_paused
    print(pelaaja.pisteet,pelaaja.nimi,pelaaja.location)
    art_gane_paused()
    art_new_game()       #1. Uusi peli
    art_exit_game()      #2. Lopeta peli""")
    while True:
        valinta = input("Valitse... ")
        if valinta == "1":
            #update.db
            print("uusi peli")#<----No clue mitetn tää pitäs tehä
        elif valinta== "2":
            print("Lopetetaan peli...")
            #update.db
            sys.exit()
        elif valinta == "esc":
            print("Main")
            break

