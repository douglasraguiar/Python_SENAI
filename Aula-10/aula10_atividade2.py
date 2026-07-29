# ## ***TIVIDADE 2***

# Crie um sistema de notas alunos, com as seguintes operações:
# ***Utilize While ou for***

#  **Sistema de notas de alunos**

# - ***Visão do professor***

# - Acesso a conta com condicionais

# - 3 chances de acessar o sistema

# - Após errar 3 x mensagem que diga que a conta bloqueada (senha incorreta)
# - Inserir notas (se Senha correta)
# - Fazer a média

# - Utilize ***loops for, while, condicionais, variáveis, listas, tuplas ou dicionários…***

# ***IMPORTANTE:***

# - Ao finalizar o código, insira na borda do script, no última linha:

# input(’Digite enter para sair’)


print("Bem vindo ao sistema de notas para professores.")
print("Digite seu login e senha. (Você possui 3 chances)")

login = "login"
senha = "senha"
nota1 = 0
nota2 = 0
nota3 = 0



for x in range(3):
    if input("Digite seu login: ") == "login" and input("Digite sua senha: ") == "senha":
        print("Login e senha validados!")
        nota1 = float(input("Digite a nota 1: "))
        print(f"Você incluiu a nota 1: {nota1}")
        nota2 = float(input("Digite a nota 2: "))
        print(f"Você incluiu a nota 2: {nota2}")
        nota3 = float(input("Digite a nota 3: "))
        print(f"Você incluiu a nota 3: {nota3}")

        media = (nota1 + nota2 + nota3) / 3

        print(" ")
        print(f"A média do aluno é: {media}")
        break
    else:
        print("Login ou senha incorreta!")


