import datetime

FILE_NAME = F"log_{datetime.datetime.now().date()}.txt"


def writeData(text):
    try:
        _file = open(FILE_NAME, "r")
        _read = _file.read()
        _file.close()
    except:
        _read = ""
    _file = open(FILE_NAME, "w")
    _file.write(_read + text)
    _file.close()