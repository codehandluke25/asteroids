import pygame, sys
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *


def main():
    pygame.init()
    print ("Starting Asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    # Create a new AsteroidField object
    asteroid_field = AsteroidField()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)

        screen.fill("black")
        
        for drawn in drawable:
            drawn.draw(screen)

        pygame.display.flip()

        dt =   game_clock.tick(60) / 1000 

        for asteroid in asteroids:
            if player.collision(asteroid) == True: 
                print ("Game over!")
                pygame.quit()
                sys.exit()     # This will exit the program
        for asteroid in asteroids:
            for shot in shots:
                if shot.collision (asteroid) == True:
                    asteroid.split()
                    shot.kill()
if __name__ == "__main__":
    main()