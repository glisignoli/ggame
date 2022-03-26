import pygame
from gcolors import GColor

class Shooter(pygame.sprite.Sprite):
    def __init__(self, x_pos: int, y_pos: int, color: tuple, rotation: int):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface((100, 20))
        self.image.fill(GColor.GRAY.tupple_format())

        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.rect.width = 100
        self.rect.height = 20
        
        pygame.draw.rect(
            surface=self.image,
            color=GColor.RED1.tupple_format(),
            rect=self.rect,
            width=4
        )
