import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # updatable - all the objects that can be updated
    updatable = pygame.sprite.Group()
    # drawable - all the objects that can be drawn
    drawable = pygame.sprite.Group()
    
    # to add all instances of a Player to the two groups
    Player.containers = (updatable, drawable)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    
    
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # player.update(dt)
        for obj in updatable:
            obj.update(dt)
            
        for asteroid in asteroids:
            if asteroid.check_collision(player):
                sys.exit("Game over!")
            for bullet in shots:
                if asteroid.check_collision(bullet):
                    bullet.kill()
                    asteroid.split()

        screen.fill(color= (0, 0, 0))
        
        # player.draw(screen)
        for obj in drawable:
            obj.draw(screen)
            
        pygame.display.flip()
        
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000        
        

if __name__ == "__main__":
    main()