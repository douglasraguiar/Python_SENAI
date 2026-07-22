### 1 - Crie um programa para efetuar a leitura de um número inteiro e apresentar o resultado do quadrado deste número.

x= int(input("Digite um número inteiro:"))
print("O número ao quadrado é:",x ** 2)

### 2 - Crie duas variáveis para armazenar seu primeiro nome e sobrenome. Em seguida, concatene-as para formar seu nome completo e exiba o resultado.

nome = "Douglas"
sobrenome = "Aguiar"
print("Meu nome é", nome, sobrenome)

# ### 3 - Peça ao usuário para digitar dois números inteiros e armazene-os em variáveis. Realize a concatenação desses números como strings e exiba o resultado.

num1 = int(input("Digite o primeiro número inteiro:"))
num2 = int(input("Digite o segundo número inteiro:"))
print(str(num1), str(num2))

# ### 4 - Crie uma variável para armazenar a palavra "Python". Em seguida, adicione um número inteiro ao final da palavra usando a concatenação e exiba o resultado.

y = "Python"
print(y,5)

# # ### 5 - Declare uma variável contendo uma frase. Em seguida, peça ao usuário para digitar uma palavra e concatene essa palavra no final da frase. Exiba o resultado.

frase = "meu nome é"
continuacao = input("Qual é o seu nome?")
print(frase,continuacao)