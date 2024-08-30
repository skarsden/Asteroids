import pygame
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        pygame.sprite.Sprite.__init__(self, UPDATABLE)
        pygame.sprite.Sprite.__init__(self, DRAWABLE)
        pygame.sprite.Sprite.__init__(self, ASTEROIDS)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, 2)

    def update(self, dt):
        self.position += self.velocity * dt