# Exercício 1:
# Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro.


# try:
#     numero = int(input("Digite um número inteiro: "))
# except ValueError: 
#     print("Isso não é número inteiro")


# Exercício 2:
# Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule a exceção caso ocorra um erro na operação  -  ZeroDivisionError.

# try:
#     numero1 = int(input("Digite o número 1: "))
#     numero2 = int(input("Digite o número 2: "))
#     resultado = numero1 / numero2
#     print(f"Resultado: {resultado}")
# except ZeroDivisionError: 
#     print("Foi digitado zero, resultado é: zero.")

# Exercício 3:
# Crie uma lista e um índice como entrada e retorne o índice. Manipule a exceção caso o índice seja inválido(caso imprima um indice que não exista na lista).
# try:
#     lista = ["a","b"]
    
#     valor = input("Digite um indice de lista[a,b]:   ")
#     lista.index(valor)
# except ValueError:
#     print("Indice invalido")
