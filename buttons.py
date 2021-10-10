import keyboard
words = {
    "space" : " ",
    "alt" : "",
    "shift": "",
    "enter" : "\n",
    "backspace" : " "
}

def translate(text):
    layout = dict(zip(map(ord, '''qwertyuiop[]asdfghjkl;'zxcvbnm,./`QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?~'''),
                               '''йцукенгшщзхъфывапролджэячсмитьбю.ёЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ё'''))

    return text.translate(layout)


def print_pressed_keys(e):
    #print(e)
    if e.event_type == "down":
        print(e.name)
    #print(e.event_type)


keyboard.hook(print_pressed_keys)
keyboard.wait()