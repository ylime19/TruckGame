import pygame

from code.Const import ENTITY_SPEED
from code.Entity import Entity


class PlayerShoot(Entity):
   def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        # Redimensiona o tiro do player
        self.surf = pygame.image.load("./asset/" + name + ".png").convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (20, 10))
        self.rect = self.surf.get_rect(center=position)

   def move(self, ):
       self.rect.centerx += ENTITY_SPEED[self.name]
