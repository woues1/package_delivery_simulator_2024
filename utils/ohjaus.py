import keyboard
def tapahtuma_paina(on_key_press):
    def on_key_tapahtumaa(tapahtuma):
        nappi = tapahtuma.name
        if nappi =='esc':
            on_key_press('esc')#<----- Insert
        elif nappi in [str(i) for i in range(1, 10)]:
            on_key_press(nappi)#<----- Insert
        else:
            print("Invalid key")#<----- Insert
    
    keyboard.on_press(on_key_tapahtumaa)