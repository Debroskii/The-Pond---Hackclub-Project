import math
import random
import pygame

from config.global_config import GLOBALCONFIG
from game import ThePond


class PathGenerator:
    def __init__(self):
        self.pos = pygame.Vector2(random.randint(0, GLOBALCONFIG.window_width), random.randint(0, GLOBALCONFIG.window_height))
        self.target = pygame.Vector2((GLOBALCONFIG.window_width / 2) + random.randint(-100, 100), (GLOBALCONFIG.window_height / 2) + random.randint(-100, 100))
        self.heading = 0
        self.speed = 1
        
    def loop(self):
        self.heading = math.atan2((self.target - self.pos).y, (self.target - self.pos).x)
        self.pos += pygame.Vector2(math.cos(self.heading * math.pi / 180) * self.speed, math.sin(self.heading * math.pi / 180) * self.speed)
        
        if (self.target - self.pos).magnitude() <= 2:
            self.heading += random.randint(-random.randint(30, 55), random.randint(30, 55))
            self.target.update(
                self.pos.x + math.cos(self.heading) * 50, 
                self.pos.y + math.sin(self.heading) * 50
            )
            
            if ThePond.out_of_logic_bounds(self.pos):
                self.target.update((GLOBALCONFIG.window_width / 2) + random.randint(-100, 100), (GLOBALCONFIG.window_height / 2) + random.randint(-100, 100))
                
    def debug_draw(self, surface):
        pygame.draw.circle(surface, (0, 255, 0), self.pos, 10)
        pygame.draw.circle(surface, (255, 0, 255), self.target, 10)