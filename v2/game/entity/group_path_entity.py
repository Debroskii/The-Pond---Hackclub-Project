import math
import random

import pygame
from game.entity.path_entity import PathEntity


class GroupPathEntity:
    def __init__(self):
        self.lifetime = 0
        self.path_entity = PathEntity()
        self.capacity = random.randint(2, 5)
        self.radius = self.capacity * 15
        self.follower_positions = []
        
        for i in range(self.capacity):
            theta = (random.randint(0, 200) / 100) * math.pi
            r = (random.randint(65, 100) / 100) * self.radius
            self.follower_positions.append(
                [theta, r, random.randint(-1, 1) / 250] #Angle, radius, speed
            )
                
    def loop(self, timestamp):
        self.lifetime += 1
        self.path_entity.loop(timestamp)
        for pos in self.follower_positions:
            pos[0] += pos[2]
        
    def draw(self, surface):
        self.path_entity.debug_draw(surface)
        pygame.draw.circle(surface, (255, 255, 255), self.path_entity.pos, self.radius, 1)
        for pos in self.follower_positions:
            pygame.draw.circle(surface, (255, 0, 0), self.path_entity.pos + pygame.Vector2(pos[1] * math.cos(pos[0]), pos[1] * math.sin(pos[0])), 5)