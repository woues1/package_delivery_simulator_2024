import keyboard

def tapahtuma_paina(on_key_press):
    def on_key_tapahtumaa(tapahtuma):
        nappi = tapahtuma.name
        if nappi == 'esc':
            on_key_press('esc')  # <----- Insert
        elif nappi in [str(i) for i in range(1, 10)]:
            on_key_press(nappi)  # <----- Insert



    keyboard.on_press(on_key_tapahtumaa)


keys = [
    "down",
    "up",
    "left",
    "right",
    "w",
    "s",
    "a",
    "d",
    "1",
    "2",
    "3",
    "4",
    "q",
    "e",
    "f"
]

def kbdCallback(e):
    found = False
    for key in keys:
        if key == keyboard.normalize_name(e.name):
            print(f"{key} was pressed")
            found = True
            # work your magic

    if found == True:
        if e.name == "left":
            if keyboard.is_pressed("4"):
                print("4 & left arrow were pressed together!")
                # work your magic

keyboard.on_press(kbdCallback)