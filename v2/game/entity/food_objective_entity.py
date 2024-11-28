import math
import random

import pygame


class FoodObjectiveEntity:
    def __init__(self, position):
        self.lifetime = 0
        self.position = position
        self.capacity = random.randint(3, 7)
        self.radius = self.capacity * 10
        self.feeding_positions = []
        
        for i in range(self.capacity):
            theta = (random.randint(0, 200) / 100) * math.pi
            r = (random.randint(45, 100) / 100) * self.radius
            self.feeding_positions.append(
                [theta, r, random.randint(-2, 2) / 500] #Angle, radius, speed
            )
        
    def loop(self, timestamp):
        self.lifetime += 1
        self.radius += 0.1
        for pos in self.feeding_positions:
            pos[1] += (math.cos((timestamp / 500) + self.feeding_positions.index(pos))) * 0.1
            pos[1] += 0.05
        
    def debug_draw(self, surface):
        pygame.draw.circle(surface, (0, 255, 0), self.position, 3)
        pygame.draw.circle(surface, (255, 255, 255), self.position, self.radius, 1)
        
        for pos in self.feeding_positions:
            pygame.draw.circle(surface, (255, 255, 0), self.position + pygame.Vector2(pos[1] * math.cos(pos[0]), pos[1] * math.sin(pos[0])), 3)