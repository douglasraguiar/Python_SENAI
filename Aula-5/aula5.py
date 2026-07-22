# # +
# print('isso é um texto ' + ' ' + '10')
# # print(10 + 10)

# # ,
# print('isso é um texto ',  '10')

# # % 
# print('isso é um texto  %d'%(10))

# # .format()
# print('isso é um texto  {}'.format(10))

# # f-string
# print(f'isso é um texto  {10} ')


# UTILIZE VARIÁVEIS!!!!!! 
# Utilize as 5 concatenações, teste todas 

# 1 Imprima uma mensagem de boas-vindas na tela.
print("Boas vindas!!")
# 2 Declare uma variável booleana verdadeiro
# com o valor True e imprima seu tipo
VarBool = True
print(type(VarBool))
# 3 Imprima o resultado da multiplicação de dois números decimais de sua escolha
print(10.5 * 15.6)
# 4 Imprima o resultado da divisão (/)de dois números inteiros 
# de sua escolha.
print(10 / 5)
# 5 Imprima o resultado da subtração de dois números inteiros de sua escolha
print(10 - 3)
# 6 Imprima o resultado da divisão (//)inteira de dois números inteiros 
# de sua escolha.
print(10 // 5)
# 7 Imprima o resultado da multiplicação de 4 números 
# decimais de sua escolha
print(1 * 2 * 3 * 4)
# 8 Declare uma variável numero e atribua um número inteiro. Em seguida, 
# imprima o dobro desse número
numero = 5
print(numero * 2)
# 9 Crie um sistema de cadastro com as estruturas que vc já 
# conhece(Use apenas input, print e variavel)
# # nome, email, idade, cidade, gradução, estado civil 
print("Bem vindo o cadastramento.")
nome = str(input("Digite seu nome:"))
email = str(input("Digite seu e-mail:"))
idade = int(input("Digite seu idade:"))
cidade = str(input("Digite sua cidade de nascimento:"))
graduacao = str(input("Digite seu nível de graduação:"))
EstadoCivil = str(input("Digite seu estado civil:"))
print("Nome:",nome)
print("E-mail:",email)
print("Idade:",idade, "anos")
print("Cidade:",cidade)
print("Graduação:",graduacao)
print("Estado Civil:",EstadoCivil)
