from utils.kirjaudu_funktiot import kirjaudu_sisaan, uusi_peli, exit_game


def main_menu():
    valinta = input("")
    while True:
        if valinta == "1":
            tulos = kirjaudu_sisaan()
            if tulos != []:
                #Tässä pelaaaja kirjautuu sisään ja break takas main scriptiin (pitääkö tää paluttaa mitään)? esim. g.id
                print(tulos)#game_id
                break
            else:
                main_menu() # tää ehkä pitää muuttaa paulautuvaan komenttoon niinku kirjaudu_sisaan
        elif valinta == "2":
            uusi_peli()
        elif valinta == "3":
            exit_game()
        else:
            print(f"Error: false input {valinta}")
            main_menu()


main_menu()