import pygame
from constants import *
from circleshape import *
from player import *



def main():
    print ("Starting Asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    BLACK = 0,0,0
    dt = 0
    game_clock = pygame.time.Clock()
    
    while True:
        screen.fill(BLACK)
        player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        player.draw(screen)
        pygame.display.flip()
        dt =   game_clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
if __name__ == "__main__":
    main()