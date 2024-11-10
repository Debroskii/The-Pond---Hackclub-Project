import pygame
import random

class KoiFish:
    pos = pygame.Vector2()
    motion = pygame.Vector2()
    speed = random.randint(25, 150) / 100
    color = ()
    scale = 1
    segments = []
    
    def __init__(self, color, scale):
        self.color = color
        self.scale = scale
        
        self.pos = pygame.Vector2(random.randint(900), random.randint(900))
        
    def update(self):
        for segment in self.segments:
            segment.update();
        
    def draw(self):
        for segment in self.segments:
            segment.draw();