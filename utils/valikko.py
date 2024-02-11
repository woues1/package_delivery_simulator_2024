
"""
def valikko():
    print("MAIN MENU PLACEHOLDER")
    print("PELAAJAN TIEDOT(pisteet, co2 budjetti jne.)")

    print("UUSI PELI (poistaa nykyisen pelitiedoston ja aloittaa uudestaan)")

    print("LOPETA PELI(nappi)")

"""

def valikko():
    from utils.pelaaja import kayttaja_haku
    import keyboard
    import sys
    from utils.ohjaus import kbdCallback
    printtaus = kayttaja_haku()#<----plaayer class
    print(printtaus)
    print("""
    1. Uusi peli
    2. Lopeta peli""")
    while True:
        event = keyboard.read_event(suppress=True)
        if event.event_type == keyboard.KEY_DOWN:
            pressed_key = event.name
            if pressed_key("1"):
                print("uusi peli")#<----No clue mitetn tää pitäs tehä
            elif pressed_key("2"):
                print("Lopetetaan peli...")
                #update.db
                sys.exit()
            elif pressed_key("esc"):
                break
