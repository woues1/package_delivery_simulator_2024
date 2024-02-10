import keyboard




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

keyboard.on_press(kbdCallback)