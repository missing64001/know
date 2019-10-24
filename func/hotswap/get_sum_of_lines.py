import pyperclip


def getSumOfLines():
    data = pyperclip.paste()
    data = data.split('\n')
    data = [da for da in data if da.strip()]
    pyperclip.copy(len(data))