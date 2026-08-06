import os
import shutil


# Exercício 1: Criar e ler um Arquivo

with os.scandir('C:/Users/Aluno/Downloads/Nova pasta/') as entrada:
    os.mkdir("nova1")

    for arquivo in entrada:
        print(f'Diretório encontrado: {arquivo.name}')
         

# Exemplo 2: Cria um Diretório

os.mkdir("nova2")


# # Exercício 3: Renomear um Diretório

os.rename('nova2', 'nova3')


# # Exercício 4:  Listar Arquivos em um Diretório

with os.scandir('C:/Users/Aluno/Downloads/Nova pasta/nova1') as entrada:
    for arquivo in entrada:
        if arquivo.is_file():
            print(f'Arquivo encontrado: {arquivo.name}')

# # Exercício 5:  Copiar Arquivos em um Diretório

shutil.copytree('nova1', 'nova5')

# # Exercício 6:  Remover

shutil.rmtree('C:/Users/Aluno/Downloads/Nova pasta/nova3')
shutil.rmtree('C:/Users/Aluno/Downloads/Nova pasta/nova1')
shutil.rmtree('C:/Users/Aluno/Downloads/Nova pasta/nova5')