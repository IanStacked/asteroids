import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    Shot.containers = (updateable, drawable, shots)
    AsteroidField.containers = (updateable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    AsteroidField()

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill((0, 0, 0))
        updateable.update(dt)
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game Over!")
                exit(0)
            for shot in shots:
                if shot.collision(asteroid):
                    asteroid.split()
                    shot.kill()
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000  # Limit to 60 FPS

if __name__ == "__main__":
    main()
