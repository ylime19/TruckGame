# C
import pygame

COLOR_ORANGE = (255, 128, 0)
COLOR_PINK = (255, 2, 117)
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_ROSA = (255, 191, 247)
COLOR_GREEN = (0, 128, 0)
COLOR_CYAN = (0, 128, 128)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Level2Bg5': 0,
    'Level2Bg6': 0,
    'Player1': 1,
    'Player1Shoot':25,
    'Inimigo1': 1,
    'Inimigo1Shoot': 20,

}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Level2Bg5': 0,
    'Level2Bg6': 0,
    'Player1': 0,
    'Player1Shoot':0,
    'Inimigo1': 100,
    'Inimigo1Shoot': 0,

}

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'Level2Bg0': 0,
    'Level2Bg1': 1,
    'Level2Bg2': 2,
    'Level2Bg3': 3,
    'Level2Bg4': 4,
    'Level2Bg5': 5,
    'Level2Bg6': 6,
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
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Level2Bg5': 999,
    'Level2Bg6': 999,
    'Player1': 200,
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

# S
SPAWN_TIME = 3000

# T
TIMEOUT_STEP = 100 #100ms
TIMEOUT_LEVEL = 20000 #20s

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324