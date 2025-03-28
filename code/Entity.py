#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
import pygame
from pygame.image import load
from code.Const import WIN_WIDTH, WIN_HEIGHT

class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = load("./asset/" + name + '.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0

    @abstractmethod
    def move(self, ):
        pass

