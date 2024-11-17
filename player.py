import circleshape
import shot
import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN 

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255,255,255), self.triangle(), 2)
        
    def rotate(self, dt):
        # dt = clock.tick(60) / 1000
        # dt represents the time that has passed since the last frame (in seconds)
        # dt normalizes the movement speed across different frame rates.
        # On a 60 FPS computer: dt ≈ 1/60 ≈ 0.016 seconds / frame
        # On a 30 FPS computer: dt ≈ 1/30 ≈ 0.033 seconds / frame
        self.rotation += PLAYER_TURN_SPEED * dt # degrees per frame
    
    
    def update(self, dt):
        """
        The update method dynamically updates the player's behavior or state each frame of the game loop.
        """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
            
        if keys[pygame.K_SPACE]:
            if self.timer <= 0:
                self.shoot()
                self.timer = PLAYER_SHOOT_COOLDOWN
            # Decrease the timer by dt every time update is called on the player
            self.timer -= dt
            
    def move(self, dt):
        """need the ship to move back and forth with the W and S keys."""
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        
    def shoot(self):
        x = self.position.x
        y = self.position.y
        new_shot = shot.Shot(x, y, SHOT_RADIUS)
        new_shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
