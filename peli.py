import keyboard
from utils.ohjaus import kbdCallback

#alemmassa kommentissa esimerkki
#keyboard.on_press(kbdCallback(keyboard.wait()))

def main():
    while True:
        valinta = keyboard.on_press(kbdCallback(keyboard.wait()))
        if valinta == 1:
            print("valitsit tehtävän 1: (tehtävä 1 tiedot)")
        elif valinta == 2:
            print("valitsit tehtävän 2: (tehtävä 2 tiedot)")
        elif valinta == 3:
            print("valitsit tehtävän 2: (tehtävä 2 tiedot)")
        #päivitetään "pelaaja olioon"


    #Tässä katsotaan onko käyttäjä mennyt ESC > valikko > quit.
    #jos on valinnut quit suljetaan peli

    #ESC keypress löytyy ohjaus kansiosta ja valikko löytyy kansiosta "valikko"

        """
        if valinta == quit(): 
            print(f"kiitos pelaamisesta {pelaaja.nimi}")
            break 
        """
if __name__ == '__main__':
    main()
