import pygame, random
from circleshape import *
from constants import *



class Asteroid(CircleShape):
    #initialize the PLayer using the circleshape class
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
# Override the draw() method to draw the asteroid as a pygame.draw.circle. 
# Use its position, radius, and a width of 2
    def draw (self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    #Override the update() method so that it moves in a straight line
    # at constant speed. On each frame, it should add (self.velocity * dt) 
    # to its position (get self.velocity from its parent class, CircleShape).

    def update (self, dt):
        self.position += self.velocity * dt
    
    def split (self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform (20,30)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)

        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_1.velocity = new_velocity1 * 1.4
        #pygame.math.Vector2.rotate(random_angle)

        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2.velocity = new_velocity2 * 1.4
        #pygame.math.Vector2.rotate(-random_angle)

        
