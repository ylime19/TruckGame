import pygame

pygame.init()

# Janela
WIN_WIDTH, WIN_HEIGHT = 576, 324
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Teste de Tiro")

# Cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Classe Tiro
class PlayerShoot:
    def __init__(self, position):
        self.surf = pygame.Surface((20, 10))
        self.surf.fill(RED)
        self.rect = self.surf.get_rect(center=position)
        self.speed = 8

    def move(self):
        self.rect.x += self.speed

    def draw(self, surface):
        surface.blit(self.surf, self.rect)

# Player fixo
player_y = WIN_HEIGHT // 2
shoots = []

clock = pygame.time.Clock()

while True:
    clock.tick(60)
    window.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        shoots.append(PlayerShoot((100, player_y)))

    for s in shoots:
        s.move()
        s.draw(window)

    pygame.display.update()
