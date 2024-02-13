from utils.pelilauta import art_title_screen, art_exit_game
from utils.kirjaudu_funktiot import kirjaudu_sisaan, uusi_peli, exit_game

art_title_screen()
valinta = input("")

while valinta != "":
    if valinta == "1":
        tulos = kirjaudu_sisaan()
        if tulos == True:
            break
        elif tulos == False:
            continue
        else:
            continue # tää ehkä pitää muuttaa paulautuvaan komenttoon niinku kirjaudu_sisaan
    elif valinta == "2":
        uusi_peli()
    elif valinta == "3":
        exit_game()
    else:
        print(f"Error: false input{valinta}")


