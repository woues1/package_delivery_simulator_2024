from utils.kirjaudu_funktiot import kirjaudu_sisaan, uusi_peli, exit_game, leaderboard_menu
from utils.pelilauta import art_title_screen
from utils.pelaaja import olio_luonti


def main_menu():
    art_title_screen()
    valinta = input("")


    while True:

        if valinta == "1":
            tulos = kirjaudu_sisaan()
            if tulos == "back":
                art_title_screen()
                valinta = input("")
                continue
            if tulos != []:
                pelaaja = olio_luonti(tulos[0][0])
                return pelaaja


        elif valinta == "2":
            tulos = uusi_peli()
            pelaaja = olio_luonti(tulos[0][0])
            return pelaaja


        elif valinta == "4":
            exit_game()


        elif valinta == "3":
            leaderboard_menu()
            art_title_screen()
            valinta = input("")
            continue
        else:
            print(f"Error: false input {valinta}")
            valinta = input("")
            continue
