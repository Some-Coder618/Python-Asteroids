from circleshape import *
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def pentagon(self):
        forward = pygame.Vector2(0, 1)
        right = pygame.Vector2(0, 1).rotate(90) * self.radius / 1.5
        a = self.position - forward * self.radius
        b = self.position - forward * 0.05 * self.radius - right
        c = self.position + forward * self.radius - right * 0.5
        d = self.position + forward * self.radius + right * 0.5
        e = self.position - forward * 0.05 * self.radius + right
        return [a,b,c,d,e]


    
    def draw(self, screen):
        #pygame.draw.polygon(screen, "white", self.pentagon() , 2)
        # optional circular asteroids
         pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        rand_angle = random.uniform(20,50)
        New_Vector = self.velocity.rotate(rand_angle)
        New_Vector2 = self.velocity.rotate(-rand_angle)
        New_Radius = self.radius - ASTEROID_MIN_RADIUS
        Asteroid_1 = Asteroid(self.position[0], self.position[1], New_Radius)
        Asteroid_1.velocity = New_Vector * 1.2
        Asteroid_2 = Asteroid(self.position[0], self.position[1], New_Radius)
        Asteroid_2.velocity = New_Vector2 * 1.2 
