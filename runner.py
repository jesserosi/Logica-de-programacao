import pygame
import random

# Iniciar o pygame
pygame.init()

# Configurações da tela
LARGURA = 800
ALTURA = 400
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Runner 2D")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 200, 0)

# Relógio
clock = pygame.time.Clock()

# Personagem
player_size = 50
player_x = 100
player_y = ALTURA - player_size - 50
player_vel_y = 0
gravidade = 1
no_chao = True

# Obstáculos
obstaculos = []
velocidade_jogo = 7

# Fonte
fonte = pygame.font.SysFont("Arial", 30)

# Score
pontos = 0

# Loop principal
rodando = True
while rodando:
    tela.fill(BRANCO)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and no_chao:
                player_vel_y = -20
                no_chao = False

    # Física do jogador
    player_y += player_vel_y
    player_vel_y += gravidade

    if player_y >= ALTURA - player_size - 50:
        player_y = ALTURA - player_size - 50
        no_chao = True

    # Gerar obstáculos
    if random.randint(1, 60) == 1:  # chance de aparecer
        obstaculos.append([LARGURA, ALTURA - 70, 40, 40])  # x, y, largura, altura

    # Mover obstáculos
    for obs in obstaculos:
        obs[0] -= velocidade_jogo
        pygame.draw.rect(tela, VERDE, obs)

        # Colisão
        if (player_x < obs[0] + obs[2] and
            player_x + player_size > obs[0] and
            player_y < obs[1] + obs[3] and
            player_y + player_size > obs[1]):
            rodando = False  # Fim de jogo

    # Remover obstáculos fora da tela
    obstaculos = [obs for obs in obstaculos if obs[0] > -50]

    # Pontuação
    pontos += 1
    texto = fonte.render(f"Pontos: {pontos}", True, PRETO)
    tela.blit(texto, (10, 10))

    # Desenhar jogador
    pygame.draw.rect(tela, PRETO, (player_x, player_y, player_size, player_size))

    # Atualizar tela
    pygame.display.update()
    clock.tick(30)

pygame.quit()
