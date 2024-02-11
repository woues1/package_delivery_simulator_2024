import keyboard
from utils.valikko import valikko


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
    "f",
    "esc"
]

def kbdCallback(e):
    for key in keys:
        if key == keyboard.normalize_name(e.name):
            if key == "esc":
                valikko()
                continue
            # work your magic

keyboard.on_press(kbdCallback)