#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_SHOOT, ENTITY_SHOOT_DELAY
from code.Entity import Entity
from code.PlayerShoot import PlayerShoot


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shoot_delay = ENTITY_SHOOT_DELAY[self.name]

        player_width = WIN_WIDTH // 8 # 12.5% da largura da tela
        player_height = WIN_HEIGHT // 4  # 25% da altura da tela

        # Redimensiona a imagem apenas para o Player1
        self.surf = pygame.image.load("./asset/" + name + ".png").convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (player_width, player_height))

        # Ajusta a posição correta do Player
        self.rect = self.surf.get_rect()
        self.rect.x = 50

        self.velocity = 5
        self.movement = {'left': False, 'right': False}



    def update(self, ):
        pass


    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]

        if pressed_key[pygame.K_DOWN] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]

        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]

        if pressed_key[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]

        pass

    def shoot(self):
        keys = pygame.key.get_pressed()
        self.shoot_delay -= 1
        if keys[PLAYER_KEY_SHOOT[self.name]] and self.shoot_delay <= 0:
            self.shoot_delay = ENTITY_SHOOT_DELAY[self.name]
            return PlayerShoot(name='Player1Shoot', position=(self.rect.right, self.rect.centery))
        return None

    # self.shoot_delay -= 1
       # if self.shoot_delay == 0:
       # pressed_key = pygame.key.get_pressed()
       #  if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
       #    return PlayerShoot(name=f'{self.name}Shoot', position=(self.rect.centerx, self.rect.centery))
