import pygame

# Base class for game objects
# to represent objects in our game that are treated as circles (even if they aren't)
# The CircleShape class handles the circular collision detection, but we're not drawing the circle
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        # CircleShape extends the Sprite class to also store a position, velocity, and radius
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    
    def check_collision(self, circle_obj):
        # If distance is less than or equal to r1 + r2, the circles are colliding. If not, they aren't.
        if self.position.distance_to(circle_obj.position) <= (self.radius + circle_obj.radius):
            return True
        return False