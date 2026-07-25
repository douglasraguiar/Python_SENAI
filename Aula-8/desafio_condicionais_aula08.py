# - ***Desafio 1:  Condicionais***

# ***Sistema de Reservas de Hotel:***

# ***Você foi contratado(a) para desenvolver uma parte do sistema de um hotel. O objetivo é criar um sistema que gerencie reservas de quartos e o pagamento das diárias***.

# - *Cadastro de Cliente:*

# *O sistema deve permitir que o usuário "cadastre" o nome e a idade de até 3 clientes.*

# - *Reservas de Quartos:*

# ***O sistema deve oferecer 3 tipos de quartos:*** 

# ***"Simples", "Duplo" e "Luxo".***

# ***Cada cliente deve escolher um quarto para sua estadia.
# O preço da diária varia conforme o tipo de quarto:
# Simples: R$ 100,00 por dia.
# Duplo: R$ 150,00 por dia.
# Luxo: R$ 250,00 por dia.***

# - ***Cálculo da Estadia:***

# ***O usuário deve informar quantos dias cada cliente ficará no hotel.
# O sistema deve calcular o valor total da estadia para cada cliente, considerando o tipo de quarto e a quantidade de dias.***

# Exemplo: 

#  ***valor_cliente3 = preco_duplo * cliente3_dias***

# *Pagamento:*

# *O sistema deve exibir o valor total a ser pago por cada cliente.*

# *Regras Adicionais:
# **Utilize apenas variáveis, condicionais (if, elif, else) e listas para resolver o desafio.***


print("Bem vindo ao Hotel X")


try:
    hospedes = int(input("Digite quantos hospedes ficarão no hotel( 1 a 3 )"))
    if hospedes == 1:
        nome1 = input("Digite o nome do hospede:")
        idade1 = int(input("Digite a idade do hospede:"))
        print(f"""
            Cadastro efetuado com sucesso!!
            Nome do hospede: {nome1}
            Idade do hospede: {idade1}
            
            
            
            """)
    elif hospedes == 2:
        nome1 = input("Digite o nome do hospede 1:")
        idade1 = int(input("Digite a idade do hospede 1:"))
        nome2 = input("Digite o nome do hospede 2:")
        idade2 = int(input("Digite a idade do hospede 2:"))
        print(f"""
            Cadastro efetuado com sucesso!!
            Nome do hospede 1: {nome1}
            Idade do hospede 1: {idade1}

            Nome do hospede 2: {nome2}
            Idade do hospede 2: {idade2}
            
            
            """)
    elif hospedes == 3:
        nome1 = input("Digite o nome do hospede 1:")
        idade1 = int(input("Digite a idade do hospede 1:"))
        nome2 = input("Digite o nome do hospede 2:")
        idade2 = int(input("Digite a idade do hospede 2:"))
        nome3 = input("Digite o nome do hospede 3:")
        idade3 = int(input("Digite a idade do hospede 3:"))
        print(f"""
            Cadastro efetuado com sucesso!!
            Nome do hospede 1: {nome1}
            Idade do hospede 1: {idade1}

            Nome do hospede 2: {nome2}
            Idade do hospede 2: {idade2}
            
            Nome do hospede 3: {nome3}
            Idade do hospede 3: {idade3}
            
            """)
    else:
        print("Quantidade de hospedes inválida!!")


    print("Agora vamos à reserva de quartos")

    quarto = {

        "simples":100.00,
        "duplo":150.00,
        "luxo":250.00   
    }

    print(f"Quartos dísponíveis:{quarto.keys()}")

    if hospedes == 1:
        quarto1 = input("informe o quarto pretendido:")
        quarto1_valor = quarto[quarto1]
    elif hospedes == 2:
        quarto1 = input("informe o quarto pretendido para o hospede 1:")
        quarto2 = input("informe o quarto pretendido para o hospede 2:")
        quarto1_valor = quarto[quarto1]
        quarto2_valor = quarto[quarto2]
    elif hospedes == 3:
        quarto1 = input("informe o quarto pretendido para o hospede 1:")
        quarto2 = input("informe o quarto pretendido para o hospede 2:")
        quarto3 = input("informe o quarto pretendido para o hospede 3:")
        quarto1_valor = quarto[quarto1]
        quarto2_valor = quarto[quarto2]
        quarto3_valor = quarto[quarto3]
        
    print("Tudo certo! Agora vamos às diárias.")

    if hospedes == 1:
        diaria1 = input("informe quantos dias ficará hospedado:")
    elif hospedes == 2:
        diaria1 = input("informe quantos dias o hospede 1 ficará hospedado:")
        diaria2 = input("informe quantos dias o hospede 2 ficará hospedado:")
    elif hospedes == 3:
        diaria1 = input("informe quantos dias o hospede 1 ficará hospedado:")
        diaria2 = input("informe quantos dias o hospede 2 ficará hospedado:")
        diaria3 = input("informe quantos dias o hospede 3 ficará hospedado:")

    if hospedes == 1:
        cliente1 = quarto1_valor * float(diaria1)
    elif hospedes == 2:
        cliente1 = quarto1_valor * float(diaria1)
        cliente2 = quarto2_valor * float(diaria2)
    elif hospedes == 3:
        cliente1 = quarto1_valor * float(diaria1)
        cliente2 = quarto2_valor * float(diaria2)
        cliente3 = quarto3_valor * float(diaria3)

    if hospedes == 1:
        print(f"""
        Hospede: {nome1}
        Quarto: {quarto1}
        Valor do Quarto: R${quarto1_valor}
        Diárias: {diaria1}
        Valor Total R${cliente1}


        """)
    elif hospedes == 2:
        print(f"""
        Hospede: {nome1}
        Quarto: {quarto1}
        Valor do Quarto: R${quarto1_valor}
        Diárias: {diaria1}
        Valor Total R${cliente1}

        Hospede: {nome2}
        Quarto: {quarto2}
        Valor do Quarto: R${quarto2_valor}
        Diárias: {diaria2}
        Valor Total R${cliente2}


        """)
    elif hospedes == 3:
        print(f"""
        Hospede: {nome1}
        Quarto: {quarto1}
        Valor do Quarto: R${quarto1_valor}
        Diárias: {diaria1}
        Valor Total R${cliente1}

        Hospede: {nome2}
        Quarto: {quarto2}
        Valor do Quarto: R${quarto2_valor}
        Diárias: {diaria2}
        Valor Total R${cliente2}

        Hospede: {nome3}
        Quarto: {quarto3}
        Valor do Quarto: R${quarto3_valor}
        Diárias: {diaria3}
        Valor Total R${cliente3}


        """)

except KeyError:
    print("Quarto inexistente")
except ValueError:
    print("Digite apenas números")
except NameError:
    print("Digite apenas números")
