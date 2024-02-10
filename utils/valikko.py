
"""
def valikko():
    print("MAIN MENU PLACEHOLDER")
    print("PELAAJAN TIEDOT(pisteet, co2 budjetti jne.)")

    print("UUSI PELI (poistaa nykyisen pelitiedoston ja aloittaa uudestaan)")

    print("LOPETA PELI(nappi)")

"""

def valikko():
    from utils.testi_koodi import sql_haku_omat_tiedot
    import keyboard
    import sys
    from utils.ohjaus import kbdCallback
    sql_haku_omat_tiedot("Ilkka")#<----plaayer class
    print("""
    1. Uusi peli
    2. Lopeta peli""")
    while True:
        if keyboard.is_pressed("1"):
            print("uusi peli")#<----No clue mitetn tää pitäs tehä
        elif keyboard.is_pressed("2"):
            print("Lopetetaan peli...")
            sys.exit()
