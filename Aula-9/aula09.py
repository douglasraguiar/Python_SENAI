# ***EXERCÍCIOS com match/ case:*** 

# # ***1: Verificando se o número é par ou ímpar***

numero = 2

match numero:
    case x if x % 2 == 0:
        print("Par")
    case _:
        print("Impar")

# # ***2: Verificando se um número é positivo, negativo ou zero***

numero = 5

match numero:
    case x if x > 0:
        print("Positivo")
    case x if x < 0:
        print("Negativo")
    case _:
        print("Zero")

# ***3: Verificando se uma string é vazia ou não***

variavel = input("Digite um texto aqui:")

match variavel:
    case "":
        print("Vazio")
    case _:
        print("Possui valor")

# ***4: Verificando se um número é maior, menor ou igual a 10***

numero = int(input("Digite um número:"))

match numero:
    case x if x > 10:
        print("Maior")
    case x if x == 10:
        print("Igual a 10")
    case x if x < 10:
        print("Menor")

# ***5: Classificando uma idade em faixas etárias -  criança(12), adolescente(17), jovem(35), adulto 35 ><64, idoso(65)***

idade = int(input("Digite sua idade:"))

match idade:
    case 12:
        print("Criança")   
    case 17:
        print("Adolescente")       
    case 35:
        print("Jovem")       
    case x if x > 35 and x <=64:
        print("Adulto")
    case 65:
        print("Idoso")
    case _:
        print("Idade fora dos parâmetros")