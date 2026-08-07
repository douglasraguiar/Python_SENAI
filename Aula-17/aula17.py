# MANIPULAÇÃO DOS EVENTOS
# JOGO LABIRINTO

import pygame

# Inicializa o Pygame
pygame.init()

# ATIVIDADE 1: 

# o que a estrutura(sintaticamente)? para que serve(contexto)? 
# COMENTE O CÓDIGO, EXPLIQUE COM SUAS PALAVRAS O QUE ESTA OCORRENDO EM CADA ESTRUTURA DO 
# CÓDIGO E VERIFIQUE O QUE OCORRE. 
# CONSULTE A BIBLIOTECA -> https://www.pygame.org/docs/

# 1 - cita a estrutura de código
# 2 - contextualiza 




#exemplo:
# 2 varáveis , uma defini a altura a outra a largura 
largura, altura = 400, 400

# variável recebendo a função do pygameque dá os tamanhos para a tela do jogo.
tela = pygame.display.set_mode((largura, altura))

# função do pygame que dá o nome do jogo, aparece na barra de cima da janela.
pygame.display.set_caption("Labirinto")

# variável recebendo a cor preta.
preto = (0, 0, 0)

# variável recebendo a cor branco.
branco = (255, 255, 255)

# variável recebendo a cor vermelho.
vermelho = (255, 0, 0)

# variável recebendo o valor int 40.
tamanho_celula = 40

# variável recebendo uma tupla bi-dimensional contendo valores int 0 e 1.
labirinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# duas variáveis recebendo valor int 1 e multiplicando por variável que dá tamnaho à celula.
x, y = 1 * tamanho_celula, 1 * tamanho_celula

# variável referent a velocidade recebendo o valor int 40.
velocidade = 40

# função que define as cores do labirinto alternando entre preto e branco.
def desenhar_labirinto():
    # Estrutura de loop que cria a linha do labirinto
    for linha in range(len(labirinto)):
        # estrutura de loop que cria a coluna do labirinto pelo tamanho da linha.
        for coluna in range(len(labirinto[linha])):
            # variável que recebe a cor preto, com um condicional que transforma em braco.
            cor = preto if labirinto[linha][coluna] == 1 else branco
            # função do pygame que desenha um retangulo.
            pygame.draw.rect(tela, cor, (coluna * tamanho_celula, linha * tamanho_celula, tamanho_celula, tamanho_celula))

# variáel responsável por fazer o jogo "rodar" em loop igualando seu valor a Verdadeiro.
executando = True

# Mantém o loop enquanto a variável é Verdadeira.
while executando:
    # loop usando a variavel evento e chamando a função de evento get.
    for evento in pygame.event.get():
        # condicional se o tipo do evento for o atributo do pygame que fecha a execução do jogo.
        if evento.type == pygame.QUIT:
            # Transforma a variável que faz o jogo "rodar" em Falso.
            executando = False

    # variavel recebendo a variavel de botao pressionado do pygame.
    teclas = pygame.key.get_pressed()
    
    # condicional da variavel tlecas recebendo o apertar da tecla ESQUERDA do teclado.
    if teclas[pygame.K_LEFT]:
        # variavel nova recebe valor de variavel já citada antes do loop referente ao tamanho da celula menos a velocidade fazendo o quadrado se mover.
        novo_x = x - velocidade
        # condicional se as variaveis x e y divididas(resulado int) forem zero significando que o quadrado nao se moveu:
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            # variavel x recebe novo x caso a condicao do if seja atendida.
            x = novo_x
    # condicional da variavel tlecas recebendo o apertar da tecla DIREITA do teclado.
    if teclas[pygame.K_RIGHT]:
        # variavel nova recebe valor de variavel já citada antes do loop referente ao tamanho da celula menos a velocidade fazendo o quadrado se mover.
        novo_x = x + velocidade
        # condicional se as variaveis x e y divididas(resulado int) forem zero significando que o quadrado nao se moveu:
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            # variavel x recebe novo x caso a condicao do if seja atendida.
            x = novo_x
    # condicional da variavel tlecas recebendo o apertar da tecla CIMA do teclado.
    if teclas[pygame.K_UP]:
        # variavel nova recebe valor de variavel já citada antes do loop referente ao tamanho da celula menos a velocidade fazendo o quadrado se mover.
        novo_y = y - velocidade
        # condicional se as variaveis x e y divididas(resulado int) forem zero significando que o quadrado nao se moveu:
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            # variavel y recebe novo y caso a condicao do if seja atendida.
            y = novo_y
    # condicional da variavel tlecas recebendo o apertar da tecla BAIXO do teclado.
    if teclas[pygame.K_DOWN]:
        # variavel nova recebe valor de variavel já citada antes do loop referente ao tamanho da celula menos a velocidade fazendo o quadrado se mover.
        novo_y = y + velocidade
        # condicional se as variaveis x e y divididas(resulado int) forem zero significando que o quadrado nao se moveu:
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            # variavel y recebe novo y caso a condicao do if seja atendida fazemdo quadrado mudar de valor e se mover.
            y = novo_y

    # usa a variavel de janela do jogo e chama a funçao para preencher com a cor branco.
    tela.fill(branco)

    # chama a função que define as cores do labirinto alternando entre preto e branco.
    desenhar_labirinto()

    # função do pygame que desenha um retangulo.
    pygame.draw.rect(tela, vermelho, (x, y, tamanho_celula, tamanho_celula))

    # função que atualiza a exibição da tela.
    pygame.display.flip()

    # Função introduz um relógio no jogo controlando frame ranting.
    pygame.time.Clock().tick(10)

# função de encerrar do pygame.
pygame.quit()