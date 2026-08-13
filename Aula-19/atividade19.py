# # ATIVIDADE:
# CRIE UM BANCO DE DADOS PARA UMA AGENCIA DE MARKETING 
# PRECISA  CADASTRAR OS LEADS DA AGENCIA:

# DADOS: 
# NOME 
# IDADE
# EMAIL 
# ENDEREÇO
# TRABALHO
# GRADUÇÃO

import sqlite3


con = sqlite3.connect('cadastro.db')
cursor = con.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,            
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        email TEXT NOT NULL,
        endereco TEXT NOT NULL,
        trabalho TEXT NOT NULL,
        graduacao TEXT NOT NULL
   )
''')


con.commit()


nome = input('Nome:  ')
idade =  int(input('Idade:  '))
email = input('E-mail:  ')
endereco = input('Endereço:  ')
trabalho = input('Trabalho:  ')
graduacao = input('Graduação:  ')

cursor.execute('INSERT INTO clientes (nome, idade, email, endereco, trabalho, graduacao) values(?,?,?,?,?,?)', (nome, idade, email, endereco, trabalho, graduacao))

con.commit()

dados = cursor.execute('SELECT * FROM clientes')
# dados =  cursor.fetchall()

for x in dados:
    print('Dados inseridos com sucesso"\n''nome:', x[1], "|", 'idade:', x[2], "|", 'email: ', x[3], "|", 'endereco: ', x[4], "|", 'trabalho: ', x[5], "|", 'graduacao: ', x[6])