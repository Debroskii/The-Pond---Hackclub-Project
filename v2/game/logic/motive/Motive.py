import pygame

class Motive:
    def __init__(self, location: pygame.Vector2, radius: float):
        self.lifetime = 0
        self.location = location
        self.radius = radius
    
    def update(self):
        self.lifetime += 1
        self.radius += 0.1