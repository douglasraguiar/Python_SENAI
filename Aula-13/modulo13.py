import random

# 1 - Crie um número aleatório de 5,10
def numero_aleatorio():
    return random.randint(5,10)

# 2 - Crie 3 números aleatórios
def numero_aleatorio_3():
    n1 = random.randint(0,999)
    n2 = random.randint(0,999)
    n3 = random.randint(0,999)
    return n1, n2, n3

# 3 - Crie um número aleatório entre 10 a 30 utilize o range()
def numero_aleatorio_10_30_range():
    return random.randrange(10,30)

# 4 - Contagem regressiva simples
# Escreva um programa que exiba uma contagem regressiva de 10 a 1, e depois imprima "Fogo!".(loop for)
def countdown_10_1():
    lista = []
    x = 10
    fogo = "Fogo!"
    while x > 0:
        lista.append(x)
        x = x -1
    return lista, fogo

# 5 - Soma de números pares
# Peça ao usuário que insira um número inteiro positivo e, em seguida, calcule a soma de todos os números pares de 2 até o número inserido.
# # Peça ao usuário que insira um número inteiro 
# # faça o loop com range e for ate´o numero
# # positivo e, em seguida, calcule a soma de 
# # todos os números pares de 2 até o número inserido.
# (use módulo, if, for)
def soma_pares():
    numero_digitado = int(input("Insira um número inteiro e positivo:    "))
    numero_range = list(range(2, numero_digitado, 2))
    soma = sum(numero_range)
    return f"A soma dos números de 2 a {numero_digitado} é {soma}."


# 6 - Tabuada de multiplicação
# ***Utilize print() na saída***
# Peça ao usuário para inserir um número inteiro e mostre a tabuada de multiplicação desse número de 1 a 10.
# (while ou for )
def tabuada():
    numero_digitado = int(input("Digite um número inteiro:  "))
    x = 1
    while x <= 10:
        print(f"{x} x {numero_digitado} = ", (numero_digitado * x))
        x = x+1
        

# 7 -  Números ímpares reversos
# Exiba uma contagem regressiva de números ímpares de 99 a 1.
# (for)

def num_impar_reverse():
    
    for numero in reversed(range(1, 101, 2)):
        print(numero)



