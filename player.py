import pygame
from circleshape import *
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED

class Player(CircleShape):
    #initialize the PLayer using the circleshape class
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    #draw the player using the pygame draw polygon method, will be rendered as a white traingle
    def draw(self, screen):
        self.screen = pygame.draw.polygon (screen, "white", self.triangle(), 2)
    
    #rotates the player left or right with the arrow keys
    def rotate(self, dt):
        
        self.rotation += PLAYER_TURN_SPEED * dt
        
    
    #binds A and D keys to move the player
    def update(self, dt):
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
    
        if keys[pygame.K_d]:
            
            self.rotate(dt)

# in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]