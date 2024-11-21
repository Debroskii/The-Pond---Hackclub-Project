import math
import pygame

class Link:
    def __init__(self, x, y, angle, length):
        self.leading = pygame.Vector2(x, y)
        self.trailing = pygame.Vector2(x, y)
        self.angle = angle
        self.length = length
        self.solveTrailing()
        
    def solveTrailing(self):
        self.trailing.update(
            self.leading.x + (self.length * math.cos(self.angle)),
            self.leading.y + (self.length * math.sin(self.angle))
        )