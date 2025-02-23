#Libraries
import pygame
import sys
#Self made modules
from circleshape import CircleShape
from asteroid import Asteroid
import constants
import player
from asteroidfield import AsteroidField
from shot import Shot
#Main
def main():
    #Initializing things
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    dt = 0

    #GROUPS
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    ammo = pygame.sprite.Group()

    #CONTAINERS
    Asteroid.containers = (asteroids, updatable, drawable)
    player.Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable, )
    Shot.containers = (updatable, drawable, ammo)

    #Asteroids and Player
    me = player.Player(640, 360)
    field = AsteroidField() 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,(0,0,0))
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        updatable.update(dt)

        for roid in asteroids:
            for shot in ammo:
                if shot.position.distance_to(roid.position) <= (shot.radius + roid.radius):
                    roid.split()
                    shot.kill()
                    roid.kill()


        for roid in asteroids:
            CircleShape.collision(me, roid)
        dt = (fps.tick(60) / 1000)

main()

