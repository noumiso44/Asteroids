import pygame
from circleshape import CircleShape
import random
import constants

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x,y)
        self.radius = radius
        self.velocity = pygame.math.Vector2(1,0)
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            self.kill()
            return
        elif self.radius > constants.ASTEROID_MIN_RADIUS:
            self.kill()
            angle = random.uniform(20,50)
            new_vel1 = self.velocity.rotate(angle)
            new_vel2 = self.velocity.rotate(angle * -1)
            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
            m1 = Asteroid(self.position.x, self.position.y, new_radius)
            m2 = Asteroid(self.position.x, self.position.y, new_radius)
            m1.velocity += (new_vel1 * 1.2)
            m2.velocity += (new_vel2)

