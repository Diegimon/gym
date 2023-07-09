from tkinter import *
from components import op1


def opcao1():
    limpar_interface()
    window.destroy()
    op1.function()


def opcao2():
    limpar_interface()
    label_resultado.config(text="search member")


def opcao3():
    limpar_interface()
    label_resultado.config(text="show all members")


def opcao4():
    limpar_interface()
    label_resultado.config(text="delete member")


def limpar_interface():
    # Remove os botões da interface
    button_opcao1.pack_forget()
    button_opcao2.pack_forget()
    button_opcao3.pack_forget()
    button_opcao4.pack_forget()
    # Remove o texto anterior da interface
    label_resultado.config(text="")


# Abrindo janela
window = Tk()
window.title("Exemplo de Interface")

# Botões de opção
button_opcao1 = Button(window, text="Opção 1", command=opcao1)
button_opcao1.pack()

button_opcao2 = Button(window, text="Opção 2", command=opcao2)
button_opcao2.pack()

button_opcao3 = Button(window, text="Opção 3", command=opcao3)
button_opcao3.pack()

button_opcao4 = Button(window, text="Opção 4", command=opcao3)
button_opcao4.pack()

# Rótulo para exibir o resultado
label_resultado = Label(window)
label_resultado.pack()

window.mainloop()
