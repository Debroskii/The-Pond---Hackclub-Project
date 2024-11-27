from enum import Enum

import pygame

class MotiveType(Enum):
    FOOD:0 

class Motive:
    def __init__(self, type: MotiveType, location: pygame.Vector2, radius: float):
        self.lifetime = 0
        self.type = type
        self.location = location
        self.radius = radius
    
    def update(self):
        self.lifetime += 1
        self.radius += 0.1