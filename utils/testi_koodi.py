


def sql_haku_omat_tiedot(screen_name):
    from Modules.SQL_DEFAULT_SEARCH import hae
    def sql_haku_a_name(screen_name):
        airport_name = f"SELECT a.name FROM airport a JOIN game g ON a.ident = g.location WHERE g.screen_name = '{screen_name}'; "#<-----Käyttäjänimi haku to do list!!
        tulos_airport_name = hae(airport_name)
        return tulos_airport_name[0]
    def sql_haku_c_name(screen_name):
        country_name = f"SELECT c.name FROM country AS c JOIN airport AS a ON c.iso_country = a.iso_country JOIN game AS g ON a.ident = g.location WHERE g.screen_name = '{screen_name}';"#<-----Käyttäjänimi haku to do list!!
        tulos_country_name = hae(country_name)
        return tulos_country_name[0]
    def sql_haku_g_co2_budget(screen_name):
        co2_budget = f"SELECT g.co2_budget FROM game g WHERE g.screen_name = '{screen_name}';"#<-----Käyttäjänimi haku to do list!!
        tulos_co2_budget = hae(co2_budget)
        return tulos_co2_budget[0]
    def sql_haku_g_co2_consumed(screen_name):
        co2_consumed = f"SELECT g.co2_consumed FROM game g WHERE g.screen_name= '{screen_name}';"#<-----Käyttäjänimi haku to do list!!
        tulos_co2_consumed = hae(co2_consumed);
        return tulos_co2_consumed[0]

#def sql_haku_g_money(screen_name): #XD g_money

    airport_print = (sql_haku_a_name("Ilkka"))#<-----Käyttäjänimi haku to do list!!
    c_name_print = sql_haku_c_name("Ilkka")#<-----Käyttäjänimi haku to do list!!
    co2_budget_print=sql_haku_g_co2_budget("Ilkka")#<-----Käyttäjänimi haku to do list!!
    co2_consumed_print=sql_haku_g_co2_consumed("Ilkka")#<-----Käyttäjänimi haku to do list!!

    print("""
             ______
            _\ _~-\___
    =  = ==(____AA____D
                \_____\___________________,-~~~~~~~`-.._
                /     o O o o o o O O o o o o o o O o  |\_
                `~-.__        ___..----..                  )
                      `---~~\___________/------------`````
                      =  ===(_________D""")

    print(f"""
    Airport: {airport_print}"
    Country: {c_name_print}"
    Co2 budget: {co2_budget_print}"
    Co2 consumed: {co2_consumed_print}
    Money: 
    """)
