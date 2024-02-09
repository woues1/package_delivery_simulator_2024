import keyboard
import time

def valinta_näppäimistö(valinta):
    nappi = valinta.name
    if nappi =='esc':
        print("Escape") #<----Insert
        exit()
    elif nappi in [str(i) for i in range(1, 10)]:
        print(f"Nappi{nappi}")#<----Insert
    else:
        print("Invalid")#<----Insert

keyboard.on_press(valinta_näppäimistö)

print("1-9, esc to end")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Exit")