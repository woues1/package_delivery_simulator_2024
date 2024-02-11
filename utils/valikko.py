
"""
def valikko():
    print("MAIN MENU PLACEHOLDER")
    print("PELAAJAN TIEDOT(pisteet, co2 budjetti jne.)")

    print("UUSI PELI (poistaa nykyisen pelitiedoston ja aloittaa uudestaan)")

    print("LOPETA PELI(nappi)")

"""

def valikko():
    from utils.pelaaja import olio_luonti
    pelaaja = olio_luonti()
    import keyboard
    import sys
    from utils.pelilauta import art_new_game,art_exit_game,art_gane_paused
    from utils.ohjaus import kbdCallback
    print(pelaaja.pisteet,pelaaja.nimi,pelaaja.location)
    art_gane_paused()
    art_new_game()       #1. Uusi peli
    art_exit_game()      #2. Lopeta peli""")
    while True:
        event = keyboard.read_event(suppress=True)
        if event.event_type == keyboard.KEY_DOWN:
            pressed_key = event.name
            if pressed_key == "1":
                print("uusi peli")#<----No clue mitetn tää pitäs tehä
            elif pressed_key == "2":
                print("Lopetetaan peli...")
                #update.db
                sys.exit()
            elif pressed_key == "esc":
                print("Main")
                break

