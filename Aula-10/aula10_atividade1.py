# ## ***ATIVIDADE 1***

# 1 - Faça um programa, utilizando ***while***, que mostre na tela os números de 0 a 1000.

numero = 0

while numero <= 1000:
    print(numero)
    numero = numero +1


# 2 -  Faça um sistema, utilizando ***while e listas***, que permita o usuário escrever o nome de 10 pessoas e os mostre na tela.

nome = []

while len(nome) < 10:
    nome.append(input("digite um nome: "))
print(nome)
