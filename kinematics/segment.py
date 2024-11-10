import pygame
import math

class Segment:
    a = pygame.Vector2()
    b = pygame.Vector2()
    angle = 0
    length = 0
    
    def __init__(self, x, y, angle, length):
        self.a.update(x, y)
        self.b.update(math.sin(angle) * length, math.cos(angle) * length)
        self.angle = angle
        self.length = length
        
    def solveA(self):
        self.a.update(
            self.b.x + (self.length * math.cos(self.angle)),
            self.b.y + (self.length * math.sin(self.angle))
        )
        
    def align(self, c):
        transformation = self.a - pygame.Vector2(c[0], c[1])
        self.angle = math.atan(transformation.y / transformation.x) * 2
        self.angle += math.pi
        print(self.angle) 
           
    def anchor(self, c):
        self.b = pygame.Vector2(c[0], c[1])
        self.solveA()
        
    def solve(self, c):
        self.align(c)
        self.anchor(c)
        
    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), self.a, 3)
        pygame.draw.circle(surface, (255, 255, 255), self.b, 3)