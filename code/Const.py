# C
import pygame

COLOR_ORANGE = (255, 128, 0)
COLOR_PINK = (255, 2, 117)
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_ROSA = (255, 191, 247)

# E
EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'Player1': 3,
    'Player1Shoot': 10,
    'Inimigo1': 1,
    'Inimigo1Shoot': 2,
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Player1': 300,
    'Player1Shoot': 1,
    'Inimigo1': 100,
    'Inimigo1Shoot': 1,
}

ENTITY_SHOOT_DELAY ={
    'Player1': 20,
    'Inimigo1': 200,

}

ENTITY_SIZE = {
    'Player1': (48, 48),
    'Player1Shoot': (56, 13),
    'Inimigo1': (50, 50),
    'Inimigo1Shoot': (20, 10),
}


# M
MENU_OPTION = ('NOVO JOGO',
               'CONTINUAR JOGO',
               'SCORE',
               'SAIR')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_SPACE}


# W
WIN_WIDTH = 576
WIN_HEIGHT = 324