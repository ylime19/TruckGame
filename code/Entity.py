#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
import pygame
from pygame.image import load
from code.Const import WIN_WIDTH, WIN_HEIGHT, ENTITY_HEALTH, ENTITY_SIZE


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = load("./asset/" + name + '.png').convert_alpha()
        if "Bg" in self.name:
            self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))
        else:
            size = ENTITY_SIZE.get(self.name, (50, 50))  # tamanho padrão caso não ache
            self.surf = pygame.transform.scale(self.surf, size)

        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]

    @abstractmethod
    def move(self, ):
        pass

