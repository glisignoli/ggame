import pygame
from gcolors import GColor

class GUI:
    class Wall(pygame.sprite.Sprite):
        def __init__(self, x_pos: int, y_pos: int, length: int, width: int, color: tuple):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((length, width))
            self.image.fill(color)
            self.rect = self.image.get_rect()
            self.rect.x = x_pos
            self.rect.y = y_pos
            self.color = color

            pygame.draw.rect(self.image, self.color, rect=self.rect)

    def __init__(self):
        self.spritegroup = pygame.sprite.Group()

        # Create walls for the game
        wall_left = self.Wall(0, 0, 2, 1080, GColor.WHITE.tupple_format())
        wall_right = self.Wall(1918, 0, 2, 1080, GColor.WHITE.tupple_format())
        wall_mid_left = self.Wall(418, 0, 2, 1080, GColor.WHITE.tupple_format())
        wall_mid_right = self.Wall(1500, 0, 2, 1080, GColor.WHITE.tupple_format())
        wall_top = self.Wall(0, 0, 1920, 2, GColor.WHITE.tupple_format())
        wall_bottom = self.Wall(0, 1078, 1920, 2, GColor.WHITE.tupple_format())

        self.spritegroup.add(wall_left)
        self.spritegroup.add(wall_right)
        self.spritegroup.add(wall_mid_left)
        self.spritegroup.add(wall_mid_right)
        self.spritegroup.add(wall_top)
        self.spritegroup.add(wall_bottom)
