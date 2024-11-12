import pygame
from constants import *
from player import *

def main():

    ## Groups 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    ##

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
    clock = pygame.time.Clock()
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


        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
        # player.draw(screen)
        
        pygame.display.flip()


        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()