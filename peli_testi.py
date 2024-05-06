from data.tehtavan_luonti_algoritmi import luo_tehtava
from utils.Main_menu import main_menu
from utils.easter_eggs import *
from utils.kauppa_valikko import *
from utils.pelaaja import *
from utils.valikko import valikko
from Assets.ASCII_art import game_over
from Assets.animaatio import *
import asyncio


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033c", end="")


async def main():
    jatka = True
    pelaaja = main_menu()
    items = initialize_items(pelaaja)

    while jatka:
        if pelaaja.tehtava_aktiivinen == False and Tehtava.instance_count < 3:
            tasks = [
                asyncio.create_task(luo_tehtava(pelaaja.location)) for _ in range(3)
            ]
            t1, t2, t3 = await asyncio.gather(*tasks)


        if pelaaja.hae_pelaaja_Maa() == "Columbia":
            operation_columbia(t1.lookup_airport())
            t1.multiplier = 20


        valinta = input("")
        if valinta == "1":
            clear_console()
            pelaaja = valikko(pelaaja, items)
            continue


        elif valinta == "2":
            tehtava = input("Valitse tehtävä (1, 2, 3): ")
            if tehtava == "1":
                pelaaja.aseta_tehtava(t1)
            elif tehtava == "2":
                pelaaja.aseta_tehtava(t2)
            elif tehtava == "3":
                pelaaja.aseta_tehtava(t3)
            else:
                print(f"{tehtava} ei ole valinta.")


        elif valinta == "3":
            if pelaaja.current_tehtava:
                animate()
                clear_console()
                Tehtava.instance_count -= 3
                pelaaja.suorita_tehtava()


        elif valinta == "4":
            clear_console()
            kauppa_valikko(pelaaja, *items)


        if int(pelaaja.co2_consumed) >= int(pelaaja.co2_budget):
            game_over()
            sql_db_update_leaderboard(pelaaja.nimi, pelaaja.pisteet)
            sql_db_reset_game(pelaaja.id)



if __name__ == '__main__':
    asyncio.run(main())
