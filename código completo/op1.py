from tkinter import *
import re
import string
import random
from openpyxl import Workbook, load_workbook
import pandas as pd
import os


def criar_planilha():
    if os.path.exists("planilha.xlsx"):
        print("Planilha already exists")
        return

    dados = {'name': [],
             'id': [],
             'age': [],
             'contacts': []}
    dados_history = {"id": [],
                     'name': [],
                     'duration': [],
                     'cost': []}
    df_main = pd.DataFrame(dados)

    df_history = pd.DataFrame(dados_history)
    with pd.ExcelWriter("planilha.xlsx") as writer:
        df_main.to_excel(writer, sheet_name='members', index=False)
        df_history.to_excel(writer, sheet_name='member_ship', index=False)

    print("Planilhas created successfully.")


def gerar_sequencia():
    # Gera uma sequência aleatória de duas letras
    letras = random.choices(string.ascii_uppercase, k=2)

    # Gera um número de 6 dígitos
    numero_6_digitos = random.randint(100000, 999999)

    # Gera um número aleatório de 1 a 9
    numero_1_a_9 = random.randint(1, 9)

    # Retorna a sequência gerada
    return ''.join(letras) + str(numero_6_digitos) + "RASTR0" + str(numero_1_a_9)


def create_account(name, age, number, duration, cost):
    df_main = pd.read_excel("planilha.xlsx", sheet_name='members')
    df_history = pd.read_excel("planilha.xlsx", sheet_name='member_ship')
    account = gerar_sequencia()
    nova_conta_main = pd.DataFrame({'name': [name],
                                    'id': [account],
                                    'age': [age],
                                    'contacts': [number]})

    nova_conta_history = pd.DataFrame({'id': [account],
                                       'name': [name],
                                       'duration': [duration],
                                      'cost': [cost]})

    # Adiciona a nova conta ao DataFrame 'main'
    df_main = pd.concat(
        [df_main, nova_conta_main], ignore_index=False)
    df_history = pd.concat(
        [df_history, nova_conta_history], ignore_index=False)

    # Salva os DataFrames atualizados no arquivo Excel
    with pd.ExcelWriter("planilha.xlsx") as writer:
        df_main.to_excel(
            writer, sheet_name='members', index=False)
        df_history.to_excel(
            writer, sheet_name='member_ship', index=False)

    print("Account created successfully")


def function1():
    def validar_numeros(entrada):
        if re.match(r'^[0-9]*$', entrada):
            return True
        else:
            return False

    def validar_sem_numeros(entrada):
        if re.search(r'\d', entrada):
            return False
        return True

    def salvar_dados():
        nome = entry_nome.get()
        sobrenome = entry_sobrenome.get()
        numero = entry_numero.get()
        endereco = entry_endereco.get()
        data_nascimento = entry_data_nascimento.get()
        duração = entry_duration.get()
        mensalidade = entry_cost.get()
        duração = int(duração)
        mensalidade = int(mensalidade)
        if nome == "" or sobrenome == '' or numero == "" or endereco == "" or data_nascimento == "" or duração == '' or mensalidade == "":
            label_erro_nome.config(
                text="Ainda há campos não preenchidos", fg="red")

        elif len(nome) < 2:
            label_erro_nome.config(text="Nome inválido", fg="red")
        elif len(sobrenome) < 2:
            label_erro_nome.config(text="Sobrenome inválido", fg="red")
        elif len(numero) < 8:
            print(len(numero))
            label_erro_nome.config(text="Numero inválido", fg="red")
        elif len(endereco) < 3:
            label_erro_nome.config(text="Endereço inválido", fg="red")
        elif len(data_nascimento) != 4:
            label_erro_nome.config(
                text="Ano de nascimento invalido", fg="red")

        elif duração < 0 or duração > 48:
            label_erro_nome.config(text="Duração invalida", fg="red")
        elif mensalidade < 0:
            label_erro_nome.config(text="Mensalidade inválida", fg="red")
        else:
            # -----------------------------------------------------tratamentp de tados
            # name, age, number, duration,
            name = nome + " " + sobrenome
            age = (2023 - int(data_nascimento))
            create_account(name, age, numero, duração, mensalidade)
            print("Salvando dados do usuário...")
            label_erro_nome.config(text="Registrado", fg="green")
            window.destroy()

    window = Tk()

    window.title("Formulário")

    # Maximizar a janela
    window.state('zoomed')

    # Área do formulário
    validar_numeros_cmd = window.register(validar_numeros)
    validar_sem_numeros_cmd = window.register(validar_sem_numeros)
    frame_formulario = Frame(window, padx=20, pady=20)
    frame_formulario.pack()

    # Campo de Nome
    label_nome = Label(frame_formulario, text="Nome:")
    label_nome.grid(row=0, column=0)
    entry_nome = Entry(frame_formulario, validate="key",
                       validatecommand=(validar_sem_numeros_cmd, '%P'))
    entry_nome.grid(row=0, column=1)

    # Campo de Sobrenome
    label_sobrenome = Label(frame_formulario, text="Sobrenome:")
    label_sobrenome.grid(row=1, column=0)
    entry_sobrenome = Entry(frame_formulario)
    entry_sobrenome.grid(row=1, column=1)

    # Campo de Número

    label_numero = Label(frame_formulario, text="Número:")
    label_numero.grid(row=2, column=0)
    entry_numero = Entry(frame_formulario, validate="key",
                         validatecommand=(validar_numeros_cmd, '%P'))
    entry_numero.grid(row=2, column=1)

    # Campo de Endereço
    label_endereco = Label(frame_formulario, text="Endereço:")
    label_endereco.grid(row=3, column=0)
    entry_endereco = Entry(frame_formulario)
    entry_endereco.grid(row=3, column=1)

    # Campo de Data de Nascimento
    label_data_nascimento = Label(frame_formulario, text="Ano de Nascimento:")
    label_data_nascimento.grid(row=4, column=0)
    entry_data_nascimento = Entry(frame_formulario, validate="key",
                                  validatecommand=(validar_numeros_cmd, '%P'))
    entry_data_nascimento.grid(row=4, column=1)

    # Campo de Data de duração
    label_duration = Label(frame_formulario, text="Duração:")
    label_duration.grid(row=5, column=0)
    entry_duration = Entry(frame_formulario, validate="key",
                           validatecommand=(validar_numeros_cmd, '%P'))
    entry_duration.grid(row=5, column=1)

    # Campo de Data de mensalidade
    label_cost = Label(frame_formulario, text="mensalidade:")
    label_cost.grid(row=6, column=0)
    entry_cost = Entry(frame_formulario, validate="key",
                       validatecommand=(validar_numeros_cmd, '%P'))
    entry_cost.grid(row=6, column=1)

    # Botão Salvar
    button_salvar = Button(
        frame_formulario, text="Salvar", command=salvar_dados)
    button_salvar.grid(row=7, columnspan=2)

    # Label de Erro para o Nome
    label_erro_nome = Label(frame_formulario, text="", fg="red")
    label_erro_nome.grid(row=8, columnspan=2)

    window.mainloop()
