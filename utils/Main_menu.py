from utils.kirjaudu_funktiot import *
from utils.pelilauta import art_title_screen
from utils.pelaaja import initialize_player


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
                pelaaja = initialize_player(tulos[0][0])
                return pelaaja

        elif valinta == "2":
            tulos = uusi_peli()
            if tulos != []:
                tutorial()
                input("Paina mitä tahansa näppäintä jatkaaksesi")
                pelaaja = initialize_player(tulos[0][0])
                return pelaaja

        elif valinta == "4":
            exit_game()

        elif valinta == "3":
            leaderboard_menu()
            art_title_screen()
            valinta = input("")
            continue
        else:
            print(f"Epäkelpo syöte: {valinta}")
            valinta = input("")
            continue
