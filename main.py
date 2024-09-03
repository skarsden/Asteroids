import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for x in UPDATABLE:
            x.update(dt)

        for x in ASTEROIDS:
            if x.collision_detect(player):
                print("Game Over")
                return

        screen.fill("black")
        for x in DRAWABLE:
            x.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()