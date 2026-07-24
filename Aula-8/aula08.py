# 1 - Peça para o usuário digitar um número, verifique se um número é positivo, negativo ou zero.

# numero = int(input("Digite um número:"))

# if numero > 0:
#     print("Positivo")
# elif numero < 0:
#     print("Negativo")
# else:
#     print("Zero")

# 2 - Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com base na idade.

# idade = int(input("Digite sua idade:"))
# if idade > 18:
#     print("Pode votar.")
# else:
#     print("Não pode votar")

# 3 -  Declara uma variável com um número qualquer, determine se um número é par ou ímpar.

# numero = int(input("Digite um número:"))

# if numero % 2 == 0:
#     print("número par")
# else:
#     print("número impar")

# 4 - Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo é equilátero, isósceles ou escaleno
# Um triângulo é chamado de equilátero se todos os lados possuem a mesma medida. 
# Um triângulo é chamado de isósceles se dois lados possuem a mesma medida. 
# Um triângulo é chamado de escaleno se todos os lados possuem medidas diferentes.

# num1 = int(input("Digite o número 1:"))
# num2 = int(input("Digite o número 2:"))
# num3 = int(input("Digite o número 3:"))

# if num1 == num2 and num2 == num3:
#     print("Triangulo equilátero( 3 lados iguais )")
# elif num1 == num2 and num2 != num3 or num1 == num3 and num3 != num2 or num2 == num3 and num3 != num1:
#     print("Triangulo isósceles( 2 lados iguais )")
# else:
#     print("Triangulo escaleno( 3 lados diferentes )")

# 5 -  Determine se um número é múltiplo de 5 e 7.

# numero = int(input("Digite um número:"))

# if numero % 5 == 0 and numero % 7 == 0:
#     print("número digitado é multiplo de 5 e 7")
# else:
#     print(f"número digitado {numero} não é multiplo de 5 e 7.")

# 6 - Verifique se um número é positivo e maior que 10

# numero = int(input("Digite um número:"))

# if numero > 0 and numero > 10:
#     print("Positivo e maior que 10")
# elif numero > 0 and numero < 10 or numero == 10:
#     print("Positivo, mas não é maior que 10")
# elif numero < 0:
#     print("Negativo")
# else:
#     print("Zero")

# 7 - Verifique se um número é divisível por 3 ou 5.

# numero = int(input("Digite um número:"))

# if numero % 3 == 0 and numero % 5 == 0:
#     print("Número divisível por 3 e 5")
# elif numero % 3 == 0:
#     print("Número divisível por 3")
# elif numero % 5 == 0:
#     print("Número divisível por 5")
# else:
#     print("Número não é divisível por 3 e nem por 5")