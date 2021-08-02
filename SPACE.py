# GRUPO
# Eduardo Gonçalves: 32028016
# Gustavo Coleto: 32076541
# João Vitor Teles Centrone:32033125
# Guilherme Afonso: 32030657
# Victor Prado Chavees: 32070772

import pygame 
import sys
import random 
import math

pygame.init()

pygame.display.set_caption("Space Invaders / Space Fighters")
icone = pygame.image.load("imagens/alien.png")
pygame.display.set_icon(icone)

#dimensoes da tela
altura = 600
largura = 800

#cores
VERMELHO = (255,0,0)
PRETO = (0,0,0)
AZUL = (0,0,255)
AMARELO = (255,255,0)
LARANJA = (255, 102, 0)

#caracteristicas do usuario
tam_usuario = 50
pos_x_u = 370
pos_y_u = 480
pos_usuario = [pos_x_u,pos_y_u]

#caracteristicas do inimigo
tam_inimigo = 50
pos_inimigo = [random.randint(0,largura-tam_inimigo), 0]
inimigos = [pos_inimigo]

#velocidade dos inimigos
vel = 5

#pontuação
pontos = 0

#projeteis
bala = pygame.image.load("imagens/bullet.png")
bala_y = pos_y_u
bala_x = 0
estado = "pronto"
bals_list = [bala_x,bala_y]

#fonte do jogo
fonte = pygame.font.SysFont("monospace", 35)

#criando a tela
tela = pygame.display.set_mode((largura, altura))

#definindo os fpd
fps = pygame.time.Clock()

#variavel par ao game loop
fim_de_jogo = False

#função que desenha os inimigos
def desenhando_inimigos(inimigos, pos_inimigo):
    for pos_inimigo in inimigos:
        meteoro = pygame.image.load('imagens/meteoro.png')
        tela.blit(meteoro,(pos_inimigo[0],pos_inimigo[1]))

#funcao que faz os inimigos cairem
def caindo_inimigos (inimigos):
    delay = random.random()
    if len(inimigos) < 10 and delay < 0.1:
        pos_x = random.randint(0, (largura - tam_inimigo))
        y_pos = 0
        inimigos.append([pos_x , y_pos])


#função que atualiza a posicao dos inimigos 
def atualiza_posicao_inimigo (inimigos, pontos):
    for idx, pos_inimigo in enumerate(inimigos):
        if pos_inimigo[1] >= 0 and pos_inimigo[1] < altura:
            pos_inimigo[1] += vel
        else:
            inimigos.pop(idx)
            pontos += 1
    return pontos

#fuunçao que faz atirar
def atirar (pos_x_u, bala_y):
    global estado
    estado = "fogo"
    tela.blit(bala, (pos_x_u+16, bala_y+10))

def tiroRecebido ():
    inimigos[1]
    
#dificuldade
def dificuldade (pontos, vel):
    if pontos < 15:
        vel = 5
    elif pontos < 25:
        vel = 8
    elif pontos < 35:
        vel= 12
    elif pontos < 50:
        vel = 15
    else:
        vel = 20
    return vel

#funcao que ve se há colisao
def colisao (pos_usuario, pos_inimigo):
    u_x = pos_usuario[0]
    u_y = pos_usuario[1]

    i_x = pos_inimigo[0]
    i_y = pos_inimigo[1]

    if (i_x >= u_x and i_x < (u_x + tam_usuario)) or (u_x >= i_x and u_x < (i_x + tam_inimigo)):
        if (i_y >= u_y and i_y < (u_y + tam_usuario)) or (u_y >= i_y and u_y < (i_y + tam_inimigo)):
            return True
    return False

#funcao que verifica se ocorre uma colisao para os inimigos
def verifica_colisao (inimigos, pos_usuario):
    for pos_inimigo in inimigos:
        if colisao(pos_inimigo, pos_usuario ):
            return True
    return False

def texto_tela_final (mensagem, cor):
    texto = font.render()


#loop do jogo
while not fim_de_jogo:
    while fim_de_jogo:
        tela.fill(LARANJA)


    #sair do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #pegadno as teclas direita/esquerda
        if event.type == pygame.KEYDOWN:
            x = pos_usuario[0]
            y = pos_usuario[1]
            if event.type == pygame.MOUSEMOTION:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
            elif event.key == pygame.K_SPACE:
                if estado == "pronto":
                    bala_x = pos_usuario[0]
                    atirar(bala_x, bala_y)

            pos_usuario = [x,y]

    #plano de fundo
    background = pygame.image.load('imagens/terraplana.jpeg')
    tela.blit(background,(0,0))

    #saida do jogo se houver colisao
    if colisao(pos_usuario, pos_inimigo):
        fim_de_jogo = True
        
    #fucao que faz cair os inimigos
    caindo_inimigos(inimigos)

    #funcao que atauliza as posicoes e os pontos do usário
    pontos = atualiza_posicao_inimigo(inimigos, pontos)

    #colocando na tela os pontos
    texto = "Pontos" + str(pontos)
    printado = fonte.render(texto,1,AMARELO)
    tela.blit(printado,(largura-200,altura-40))

    #funcao que verifica as colisoes e sai do jogo
    if verifica_colisao(inimigos, pos_usuario):
        fim_de_jogo = True
        break 
    
    #desenha os inimigos
    desenhando_inimigos(inimigos, pos_inimigo)

    vel = dificuldade(pontos, vel)

    #desenha o usuário
    nave = pygame.image.load('imagens/battleship.png')
    tela.blit(nave,(pos_usuario[0],pos_usuario[1]))
    
    
    #proprieedades do tiro
    if bala_y < 0:
        bala_y = pos_y_u
        estado = "pronto"

    if estado == "fogo":
        atirar(bala_x, bala_y)
        bala_y -=  40

    #muda o fps
    fps.tick(30)
        
    #atualiza o display
    pygame.display.update()