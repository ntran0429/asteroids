import pygame
import circleshape
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)
        
    def update(self, dt):
        # Override the update() method so that it moves in a straight line at constant speed. 
        # On each frame, it should add (velocity * dt) to its position.
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # need to spawn 2 new asteroids
        # want new asteroids to move in new random directions.
        random_angle = random.uniform(20,50)
        
        vector1 = self.velocity.rotate(random_angle)
        vector2 = self.velocity.rotate(-random_angle)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = vector1 * 1.2
        
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = vector2 * 1.2