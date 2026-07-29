import random

add = [1, 2, 3]

meus_pontos = 0
pontos_pc = 0
    
for chance in add:
    opcao_pc  =  ['tesoura','pedra', 'papel']
    escolha_pc = random.choice(opcao_pc)
    minha_escolha = input('Escolha>>')
    

    if escolha_pc == minha_escolha:
        print('Sua escolha foi', minha_escolha)
        print('A maquina escolheu ',escolha_pc)
        print("=============== EMPATE ===============")
        add.append(1)
    elif escolha_pc == "pedra" and minha_escolha == "tesoura":
        print('Sua escolha foi', minha_escolha)
        print('A maquina escolheu ',escolha_pc)
        print("=============== PERDEU ===============")
        pontos_pc = pontos_pc +1
    elif escolha_pc == "papel" and minha_escolha == "pedra":
        print('Sua escolha foi', minha_escolha)
        print('A maquina escolheu ',escolha_pc)
        print("=============== PERDEU ===============")
        pontos_pc = pontos_pc +1
    elif escolha_pc == "tesoura" and minha_escolha == "papel":
        print('Sua escolha foi', minha_escolha)
        print('A maquina escolheu ',escolha_pc)
        print("=============== PERDEU ===============")
        pontos_pc = pontos_pc +1

    elif minha_escolha == "pedra" and escolha_pc == "tesoura":
        print('Sua escolha foi', minha_escolha)
        print('A maquina escolheu ',escolha_pc)
        print("=============== GANHOU ===============")
        meus_pontos = meus_pontos +1
    elif minha_escolha == "papel" and escolha_pc == "pedra":
        print('Sua escolha foi', minha_escolha)
        print('A maquina escolheu ',escolha_pc)
        print("=============== GANHOU ===============")
        meus_pontos = meus_pontos +1
    elif minha_escolha == "tesoura" and escolha_pc == "papel":
        print('Sua escolha foi', minha_escolha)
        print('A maquina escolheu ',escolha_pc)
        print("=============== GANHOU ===============")
        meus_pontos = meus_pontos +1
    
else:
    print('Resultado:')            
    print(f"Maquina = {pontos_pc} vitórias")
    print(f"Você = {meus_pontos} vitórias")
    if meus_pontos > pontos_pc:
        print("Você ganhou!!")
    else:
        print("Você perdeu, a maquina foi vitoriosa!!")

