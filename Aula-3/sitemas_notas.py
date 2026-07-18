


nota1 = float(input("insira sua nota 1:"))
nota2 = float(input("insira sua nota 2:"))
nota3 = float(input("insira sua nota 2:"))
media = (nota1 + nota2 + nota3) /3


if media >=7:
    print("Média:", round(media, 2) , "-" , "Você está aprovado")
else:
    if media <5:
        print("Média:" , round(media, 2) , "-" , "Você está reprovado")
    else:
        print("Média:" , round(media, 2) , "-" , "Você está de recuperação")
