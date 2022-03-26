import pygame
from shooter import Shooter
from gcolors import GColor

class Player:
    def __init__(self, name, color, x_pos, y_pos, rotation):
        self.name = name
        self.blocks = []
        self.balls = []
        self.shooter = Shooter(x_pos, y_pos, color, rotation)
        
        self.spritegroup = pygame.sprite.Group()

        self.__startup()

    def __startup(self):
        """
        Initialize the player's blocks and shooter
        """
        self.spritegroup.add(self.shooter)
    
