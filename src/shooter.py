import pygame
from sprites.rectangle import Rectangle

class Shooter(pygame.sprite.Sprite):
    def __init__(self, x_pos: int, y_pos: int, color: tuple, rotation: int):
        pygame.sprite.Sprite.__init__(self)

        rectangle = Rectangle(10, 100, color, 2, color)

        self.image = pygame.image.load_basic(rectangle.memory_file) # Can't load

        self.rotation_clockwise = True
        self.angle = rotation
        self.default_angle = rotation

        self.image = pygame.transform.rotate(self.image, self.angle)

    def update(self):
        # Rotate the shooter left and right +- 15 degrees
        if self.rotation_clockwise and self.angle <= (self.default_angle + 15):
            self.image = pygame.transform.rotate(self.image, +1)
        elif not self.rotation_clockwise and self.angle >= (self.default_angle - 15):
            self.image = pygame.transform.rotate(self.image, -1)
        else:
            self.rotation_clockwise = not self.rotation_clockwise
