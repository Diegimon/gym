from tkinter import *
from components import op1
from components import op2
from components import functions


def opcao1():
    window.destroy()
    op1.function1()


def opcao2():
    window.destroy()
    op2.function2()


# cria planilha
functions.criar_planilha()
# Abrindo janela
window = Tk()
window.title("Exemplo de Interface")

# Botões de opção
button_opcao1 = Button(window, text="Adicionar mebro", command=opcao1)
button_opcao1.pack()

button_opcao2 = Button(window, text="Pesquisar membro", command=opcao2)
button_opcao2.pack()


window.mainloop()
