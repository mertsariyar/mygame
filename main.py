import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
    clock = pygame.time.Clock()

    ## Groups 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    
    asteroid_field = pygame.sprite.Group()
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    Shot.containers = (shots,updatable,drawable)

    ## adding asteroid group
    Asteroid.containers = (updatable,drawable, asteroids)
    ## adding asteroid groupw
    Player.containers = (updatable, drawable)
    ##

    dt = 0
    ##

    ## player object 
    player = Player(SCREEN_HEIGHT / 2 , SCREEN_WIDTH / 2)


    while True:
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # player.update(dt)
        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game Over!")
                sys.exit()
            
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()
        
        
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
        # player.draw(screen)
        
        pygame.display.flip()


        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()