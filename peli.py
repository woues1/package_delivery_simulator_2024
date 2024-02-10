import keyboard
# import utils.pelaaja
# import utils.pelilauta
from utils.ohjaus import kbdCallback

# alemmassa kommentissa esimerkki
# keyboard.on_press(kbdCallback(keyboard.wait()))

def main():
    while True:
        for i in range(3):
            print(f"Tehtävä {i}: {luo_tehtävä()}\n")
        keyboard.on_press(kbdCallback(keyboard.wait()))

    # tähän kohtaan voi laittaa if target location == player location
    # Suoritetaan tehtävän palautus

    # päivitetään "pelaaja olioon"

    # ESC keypress löytyy ohjaus kansiosta ja valikko löytyy kansiosta "valikko"

if __name__ == '__main__':
    main()
