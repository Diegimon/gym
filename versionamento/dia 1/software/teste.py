from tkinter import *

def salvar_dados():
    nome = entry_nome.get()
    sobrenome = entry_sobrenome.get()
    numero = entry_numero.get()
    endereco = entry_endereco.get()
    data_nascimento = entry_data_nascimento.get()
    

    if len(nome) < 2:
        label_erro_nome.config(text="Nome inválido", fg="red")
    elif len(sobrenome) < 2:
        label_erro_nome.config(text="Sobrenome inválido", fg="red")
    elif len(numero) < 8:
        print(len(numero))
        label_erro_nome.config(text="Numero inválido", fg="red")
    elif len(endereco) < 3:
        label_erro_nome.config(text="Endereço inválido", fg="red")
    elif len(data_nascimento) < 8:
        label_erro_nome.config(text="Data de nascimento invalida", fg="red")
    else:
        print("Deu certo")
        label_erro_nome.config(text="Registrado", fg="green")
      
       
      

window = Tk()
window.title("Formulário")

# Maximizar a janela
window.state('zoomed')

# Área do formulário
frame_formulario = Frame(window, padx=20, pady=20)
frame_formulario.pack()

# Campo de Nome
label_nome = Label(frame_formulario, text="Nome:")
label_nome.grid(row=0, column=0)
entry_nome = Entry(frame_formulario)
entry_nome.grid(row=0, column=1)

# Campo de Sobrenome
label_sobrenome = Label(frame_formulario, text="Sobrenome:")
label_sobrenome.grid(row=1, column=0)
entry_sobrenome = Entry(frame_formulario)
entry_sobrenome.grid(row=1, column=1)

# Campo de Número
label_numero = Label(frame_formulario, text="Número:")
label_numero.grid(row=2, column=0)
entry_numero = Entry(frame_formulario)
entry_numero.grid(row=2, column=1)

# Campo de Endereço
label_endereco = Label(frame_formulario, text="Endereço:")
label_endereco.grid(row=3, column=0)
entry_endereco = Entry(frame_formulario)
entry_endereco.grid(row=3, column=1)

# Campo de Data de Nascimento
label_data_nascimento = Label(frame_formulario, text="Data de Nascimento:")
label_data_nascimento.grid(row=4, column=0)
entry_data_nascimento = Entry(frame_formulario)
entry_data_nascimento.grid(row=4, column=1)

# Botão Salvar
button_salvar = Button(frame_formulario, text="Salvar", command=salvar_dados)
button_salvar.grid(row=5, columnspan=2)

# Label de Erro para o Nome
label_erro_nome = Label(frame_formulario, text="", fg="red")
label_erro_nome.grid(row=6, columnspan=2)

window.mainloop()
