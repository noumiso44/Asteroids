import pygame
import constants
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
    # in the player class
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
        self.rotation += (constants.PLAYER_TURN_SPEED * dt)


    #Shoot
    def shoot(self):
        new_shot = Shot(self.position.x, self.position.y, constants.SHOT_RADIUS)

        direction = pygame.Vector2(0,1)

        direction = direction.rotate(self.rotation)

        new_shot.velocity = direction * constants.PLAYER_SHOOT_SPEED    

    def update(self, dt):
        self.timer -= dt
        rev = dt * -1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(rev)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt)
        if self.timer <= 0 and keys[pygame.K_SPACE]:
            self.shoot()
            self.timer = constants.PLAYER_SHOOT_COOLDOWN
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt

