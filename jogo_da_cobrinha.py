import pygame
import random
from pygame.locals import *

# Inicialização do pygame
pygame.init()

# Definição de constantes
LARGURA, ALTURA = 640, 480
TAMANHO_GRADE = 20
LARGURA_GRADE = LARGURA // TAMANHO_GRADE
ALTURA_GRADE = ALTURA // TAMANHO_GRADE
VELOCIDADE_COBRA = 10

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)

# Direções
CIMA = (0, -1)
BAIXO = (0, 1)
ESQUERDA = (-1, 0)
DIREITA = (1, 0)

# Função para desenhar a cobra na tela


def desenhar_cobra(cobra):
    for segmento in cobra:
        pygame.draw.rect(tela, VERDE, (segmento[0] * TAMANHO_GRADE,
                         segmento[1] * TAMANHO_GRADE, TAMANHO_GRADE, TAMANHO_GRADE))

# Função para gerar comida em uma posição aleatória


def gerar_comida(cobra):
    while True:
        comida = (random.randint(0, LARGURA_GRADE - 1),
                  random.randint(0, ALTURA_GRADE - 1))
        if comida not in cobra:
            return comida


# Inicialização da tela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da Cobrinha")

# Inicialização da cobra
cobra = [(LARGURA_GRADE // 2, ALTURA_GRADE // 2)]
direcao_cobra = DIREITA

# Inicialização da comida
comida = gerar_comida(cobra)

# Inicialização do relógio para controlar a velocidade do jogo
relogio = pygame.time.Clock()

# Loop principal do jogo
jogando = True
while jogando:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            jogando = False
        elif evento.type == KEYDOWN:
            if evento.key == K_UP and direcao_cobra != BAIXO:
                direcao_cobra = CIMA
            elif evento.key == K_DOWN and direcao_cobra != CIMA:
                direcao_cobra = BAIXO
            elif evento.key == K_LEFT and direcao_cobra != DIREITA:
                direcao_cobra = ESQUERDA
            elif evento.key == K_RIGHT and direcao_cobra != ESQUERDA:
                direcao_cobra = DIREITA

    # Atualização da posição da cabeça da cobra
    nova_cabeca = (cobra[0][0] + direcao_cobra[0],
                   cobra[0][1] + direcao_cobra[1])

    # Verificação de colisão com as bordas
    if nova_cabeca[0] < 0 or nova_cabeca[0] >= LARGURA_GRADE or nova_cabeca[1] < 0 or nova_cabeca[1] >= ALTURA_GRADE:
        jogando = False

    # Verificação de colisão com o próprio corpo
    if nova_cabeca in cobra:
        jogando = False

    # Verificação de colisão com a comida
    if nova_cabeca == comida:
        cobra.insert(0, nova_cabeca)
        comida = gerar_comida(cobra)
    else:
        cobra.insert(0, nova_cabeca)
        cobra.pop()

    # Preenchimento do fundo
    tela.fill(PRETO)

    # Desenho da comida
    pygame.draw.rect(tela, VERMELHO, (comida[0] * TAMANHO_GRADE,
                     comida[1] * TAMANHO_GRADE, TAMANHO_GRADE, TAMANHO_GRADE))

    # Desenho da cobra
    desenhar_cobra(cobra)

    # Atualização da tela
    pygame.display.update()

    # Controle de velocidade
    relogio.tick(VELOCIDADE_COBRA)

# Encerramento do pygame
pygame.quit()
