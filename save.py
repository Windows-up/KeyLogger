
def writeData(text):
    _file = open("users.txt", "r")
    _read = _file.read()
    _file.close()
    _file = open("users.txt", "w")
    _file.write(_read + text)
    _file.close()