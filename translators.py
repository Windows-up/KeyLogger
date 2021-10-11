_specal_words = {
    "space": " ",
    "enter": "\n",
    "decimal": ".",

    "delete": " [DEL]",
    "backspace": " [BACK]",
    "right": " {RIGHT}",
    "left": " {LEFT}",
    "up": " {UP}",
    "down": " {DOWN}",

    "insert": "",
    "home": "",
    "end": "",
    "page up": "",
    "page down": "",
    "num lock": "",
    "ctrl": "",
    "shift": "",
    "esc": "",
    "tab": "",
    "alt": "",
    "right alt": "",

    "f1": " (F1)",
    "f2": " (F2)",
    "f3": " (F3)",
    "f4": " (F4)",
    "f5": " (F5)",
    "f6": " (F6)",
    "f7": " (F7)",
    "f8": " (F8)",
    "f9": " (F9)",
    "f10": " (F10)",
    "f11": " (F11)",
    "f12": " (F12)",
}


def translate(text):
    layout = dict(zip(map(ord, '''qwertyuiop[]asdfghjkl;'zxcvbnm,./`QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?~'''),
                      '''йцукенгшщзхъфывапролджэячсмитьбю.ёЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ё'''))

    return text.translate(layout)


def specal_buttons(btn):
    if btn in _specal_words:
        btn = _specal_words[btn]

    return btn
