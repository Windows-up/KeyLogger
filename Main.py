from translators import *
from save import *

import datetime
import keyboard

last_press = datetime.datetime.now().second
ENTER_TIME = 3

def print_pressed_keys(e):
    global last_press

    # print(e)
    if e.event_type == "down":
        time = datetime.datetime.now().second
        if abs(last_press - time) >= ENTER_TIME:

            writeData(" {AUTOENTER}\n")
        last_press = time
        print(e.name)
        writeData(specal_buttons(e.name))
    # print(e.event_type)


keyboard.hook(print_pressed_keys)
keyboard.wait()
