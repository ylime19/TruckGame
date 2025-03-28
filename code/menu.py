import pygame.image
from pygame import Surface, Rect
from pygame.font import Font
import pygame

from code.Const import WIN_WIDTH, COLOR_PINK, MENU_OPTION, COLOR_WHITE, COLOR_ROSA


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/orig.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 2
        pygame.mixer_music.load('./asset/InicialSong.flac')
        pygame.mixer_music.play(-1)
        while True:
            # DRAW IMAGES
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, 'Benny', COLOR_PINK, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, 'Boom', COLOR_PINK, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_ROSA, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))
            pygame.display.flip()

            # Check for all event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close window
                    quit()  # End pygame
                if event.type == pygame.KEYDOWN: # DOWN KEY
                    if event.key == pygame.K_DOWN:
                       if menu_option < len(MENU_OPTION) - 1:
                           menu_option +=1
                       else:
                           menu_option = 0
                    if event.key == pygame.K_UP: # UP KEY
                       if menu_option > 0:
                           menu_option -= 1
                       else:
                           menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN: # ENTER
                       return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
