import re
from tkinter import *


def validar_sem_numeros(entrada):
    if re.search(r'\d', entrada):
        return False
    return True


root = Tk()

validar_sem_numeros_cmd = root.register(validar_sem_numeros)
entry = Entry(root, validate="key", validatecommand=(
    validar_sem_numeros_cmd, '%P'))
entry.pack()

root.mainloop()
