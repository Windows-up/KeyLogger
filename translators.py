_specal_words = {
    "space" : " ",
    "enter" : "\n",
    "decimal" : ".",

    "delete" : "",
    "insert" : "",
    "home" : "",
    "end": "",
    "page up": "",
    "page down" : "",
    "num lock" : "",
    "ctrl" : "",
    "shift" : ""
}


def translate(text):
    layout = dict(zip(map(ord, '''qwertyuiop[]asdfghjkl;'zxcvbnm,./`QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?~'''),
                               '''йцукенгшщзхъфывапролджэячсмитьбю.ёЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ё'''))

    return text.translate(layout)

def specal_buttons(btn):
    if btn in _specal_words:
        btn = _specal_words[btn]

    return btn