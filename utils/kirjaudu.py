from utils.kirjaudu_funktiot import kirjaudu_sisaan, uusi_peli, exit_game
from utils.pelilauta import art_title_screen

def main_menu():
    art_title_screen()
    valinta = input("")
    while True:
        if valinta == "1":
            tulos = kirjaudu_sisaan()
            if tulos != []:
                #Tässä pelaaaja kirjautuu sisään ja break takas main scriptiin (pitääkö tää paluttaa mitään)? esim. g.id
                print(tulos)#game_id
                break
        elif valinta == "2":
            uusi_peli()
        elif valinta == "3":
            exit_game()
        else:
            print(f"Error: false input {valinta}")
            main_menu()


main_menu()#poista