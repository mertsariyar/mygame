import pygame
from constants import *
from player import *

def main():
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
        

        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()


        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()