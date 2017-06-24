#Equipe de IPC
#Antonio Diego Furtado da Silva 1715310004
#Gabriel de Queiroz Sousa 1715310044
#Lucas Gabriel Silveira Duarte 1715310053
#Matheus de Oliveira Matos 1515310514
#Reinaldo Vargas 1715310054
#Rodrigo Duarte de Souza 1115140049
import pygame
import time
import random

pygame.init()

#define cores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)


largura = 600
altura = 600

tela_jogo = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake v.10.1')

#clock time para criar um tempo para o frame
clock = pygame.time.Clock()

#tamanho do bloco
tamanho_objeto = 10
tempo_objeto = 20

font = pygame.font.SysFont(None, 25)


def cobra(tamanho_objeto, matriz):
    for posx_y in matriz:
        pygame.draw.rect(tela_jogo, green, [posx_y[0], posx_y[1], tamanho_objeto, tamanho_objeto])


def tela_msg(msg, cor):
    # desenha o texto em uma nova superficie
    tela_texto = font.render(msg, True, cor)
    tela_jogo.blit(tela_texto, [largura/ 2, altura/ 2])


def loop_jogo():
    sair_jogo = False
    gameOver = False

    # desempenho de colisao
    lado_x = largura/ 2
    lado_y = altura / 2

    # para a cobra ficar parada em (0) no inicio do jogo
    mudar_ladox = 0
    mudar_ladoy = 0

    matriz_cobra = []
    tamanho_cobra = 1

    # arredondamento de numeros aleatorios
    aleatorio_x = round(random.randrange(0, altura - tamanho_objeto) / 10.0) * 10.0
    aleatorio_y = round(random.randrange(0, largura - tamanho_objeto) / 10.0) * 10.0

    # bloquea a tela e so sairá com as opções abaixo
    while not sair_jogo:

        while gameOver == True:
            tela_jogo.fill(white)
            tela_msg("Game over, C = continuar, Q = sair", red)

            
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sair_jogo= True
                        gameOver = False
                    if event.key == pygame.K_c:
                        loop_jogo()

        # direções do blocos no teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair_jogo = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    mudar_ladox = -tamanho_objeto
                    mudar_ladoy = 0
                elif event.key == pygame.K_RIGHT:
                    mudar_ladox=tamanho_objeto
                    mudar_ladoy = 0
                elif event.key == pygame.K_UP:
                    mudar_ladoy = -tamanho_objeto
                    mudar_ladox = 0
                elif event.key == pygame.K_DOWN:
                    mudar_ladoy = tamanho_objeto
                    mudar_ladox = 0

        if lado_x >= largura or lado_x < 0 or lado_y >= altura or lado_y < 0:
            gameOver = True

        lado_x += mudar_ladox
        lado_y += mudar_ladoy

        # cor da tela principal
        tela_jogo.fill(white)
        # cor do segundo objeto (comida)
        pygame.draw.rect(tela_jogo, red, [aleatorio_x, aleatorio_y, tamanho_objeto, tamanho_objeto])

        # matriz comida
        cabeca_cobra = []
        cabeca_cobra.append(lado_x)
        cabeca_cobra.append(lado_y)
        matriz_cobra.append(cabeca_cobra)

        # pega o tamanho da matriz (listaCobra2) define maior que o cumprimento
        if len(matriz_cobra) > tamanho_cobra:
            # remove o indice da matriz (0)
            del matriz_cobra[0]

        for seguimento_cobra in matriz_cobra[:-1]:
            if seguimento_cobra == cabeca_cobra:
                gameOver = True

        cobra(tamanho_objeto, matriz_cobra)

        # atualiza o display
        pygame.display.update()

        # arredondamento de numeros aleatorios
        if lado_x== aleatorio_x and lado_y== aleatorio_y:
            aleatorio_x = round(random.randrange(0, altura - tamanho_objeto) / 10.0) * 10.0
            aleatorio_y = round(random.randrange(0, altura - tamanho_objeto) / 10.0) * 10.0
            tamanho_cobra += 1

        clock.tick(tempo_objeto)

    pygame.quit()
    quit()


loop_jogo()


