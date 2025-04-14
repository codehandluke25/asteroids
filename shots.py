from circleshape import *
from constants import PLAYER_SHOOT_SPEED, SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, radius = SHOT_RADIUS):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2 (0,0)
    
    
    def draw(self, screen):
        # Draw a small white circle
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius)
    
    def update(self, dt):
        # Move the shot according to its velocity
        self.position += self.velocity * dt


