from tkinter import *
from components import op1
from components import op2
from components import op3
from components import functions


def opcao1():
    window.destroy()
    op1.function1()
    main()


def opcao2():
    window.destroy()
    op2.function2()
    main()


def opcao3():
    op3.mostrar_itens_tkinter()


def main():
    # cria planilha
    functions.criar_planilha()
    # Abrindo janela
    global window
    window = Tk()
    window.title("Exemplo de Interface")

    # Definir o tamanho da janela
    window.geometry("400x300")  # Defina a largura e altura desejadas

    # Centralizar verticalmente os botões
    frame = Frame(window)
    frame.pack(expand=True, fill='both')

    # Botões de opção
    button_opcao1 = Button(frame, text="Adicionar membro",
                           command=opcao1, width=20)
    button_opcao1.pack(pady=10)

    button_opcao2 = Button(frame, text="Pesquisar membro",
                           command=opcao2, width=20)
    button_opcao2.pack(pady=10)

    button_opcao3 = Button(frame, text="todos os membros",
                           command=opcao3, width=20)
    button_opcao3.pack(pady=10)

    window.mainloop()


# Inicie o programa
main()
