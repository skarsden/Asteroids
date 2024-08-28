import pygame

#Base class for game object
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containters"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
    
    #to be overridden
    def draw(self, screen):
        pass

    #to be overridden
    def update(self, dt):
        pass