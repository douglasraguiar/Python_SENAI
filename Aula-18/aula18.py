# **ATIVIDADE 2** 
# Crie um formulário em Tkinter
# Problema: Sistema de Cadastro de Clientes
# Você é um desenvolvedor de software e foi contratado por uma empresa de serviços para criar um sistema de cadastro de clientes.
# O sistema deve permitir que os clientes forneçam suas informações pessoais, como nome, idade, e-mail, endereço, celular...

# ***Atividade:***
# Crie um formulário em Tkinter que contenha os seguintes campos:
# Nome
# Idade
# E-mail
# Endereço
# Celular
# Cep
# Cidade
# Cursos
# O formulário deve ter um botão de "Enviar" que, quando clicado, imprima as informações do cliente na console.
# Tamanho  da tela  = '1700x750’

import tkinter as tk
from tkinter import ttk, messagebox


janela  =  tk.Tk()
janela.geometry('1700x750')
janela.title('FORMULÁRIO')



# TITULO DO FORM


titulo  =  tk.Label(janela, text='FORMULARIO DE CADASTRO')
titulo.pack()


# TÍTULO  DO NOME |  INPUT DO NOME
nome_texto = tk.Label(janela, text  =  'Nome')
nome_texto.pack()


nome_input =  tk.Entry(janela)
nome_input.pack()

# --------------------
idade_texto = tk.Label(janela, text  =  'Idade')
idade_texto.pack()


idade_input =  tk.Entry(janela)
idade_input.pack()
# -------------------
email_texto = tk.Label(janela, text  =  'E-mail')
email_texto.pack()


email_input =  tk.Entry(janela)
email_input.pack()
# -------------------
endereco_texto = tk.Label(janela, text  =  'Endereço')
endereco_texto.pack()


endereco_input =  tk.Entry(janela)
endereco_input.pack()
# -------------------
celular_texto = tk.Label(janela, text  =  'Celular')
celular_texto.pack()


celular_input =  tk.Entry(janela)
celular_input.pack()
# ------------------------
cep_texto = tk.Label(janela, text  =  'CEP')
cep_texto.pack()


cep_input =  tk.Entry(janela)
cep_input.pack()
# ------------------------
cidade_texto = tk.Label(janela, text  =  'Cidade')
cidade_texto.pack()

cidade_opcoes = ["Guarulhos", "São Paulo", "Itaquaquecetuba"]
combo_cidade = ttk.Combobox(janela, values=cidade_opcoes)
combo_cidade.set("Escolha sua cidade")
combo_cidade.pack()
# ------------------------
cursos_texto = tk.Label(janela, text  =  'Curso')
cursos_texto.pack()

cursos_opcoes = ["Administração", "Python", "SQL", "Excel"]
combo_cursos = ttk.Combobox(janela, values=cursos_opcoes)
combo_cursos.set("Escolha seu curso")
combo_cursos.pack()
# ------------------------



def display():

    nome_display = nome_input.get()
    idade_display = idade_input.get()
    email_display = email_input.get()
    endereco_display = endereco_input.get()
    celular_display = celular_input.get()
    cep_display = cep_input.get()
    combo_display = combo_cidade.get()
    cursos_display = combo_cursos.get()

    tk.Label(janela, text = "Nome: " + nome_display).pack()
    tk.Label(janela, text = "Idade: " + idade_display).pack()
    tk.Label(janela, text = "E-mail: " + email_display).pack()
    tk.Label(janela, text = "Edenraço: " + endereco_display).pack()
    tk.Label(janela, text = "Celular: " + celular_display).pack()
    tk.Label(janela, text = "CEP: " + cep_display).pack()
    tk.Label(janela, text = "Cidade: " + combo_display).pack()
    tk.Label(janela, text = "Curso: " + cursos_display).pack()
    tk.Label(janela, text = "").pack()
    tk.Label(janela, text = "Dados cadastrados com sucesso!").pack()
    messagebox.showinfo("", "Dados cadastrados com sucesso!")
    nome_input.delete(0, 'end')
    idade_input.delete(0, 'end')
    email_input.delete(0, 'end')
    endereco_input.delete(0, 'end')
    celular_input.delete(0, 'end')
    cep_input.delete(0, 'end')
    combo_cidade.delete(0, 'end')
    combo_cursos.delete(0, 'end')




btn  =  tk.Button(janela, text = 'Eviar', command=display, font=('Courier', 15), fg= 'Red')
btn.pack(pady=10, padx=20)




janela.mainloop()




# subir para o github 