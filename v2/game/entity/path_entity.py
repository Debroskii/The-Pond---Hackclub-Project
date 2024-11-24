import math
import random
import pygame

from config.global_config import GLOBALCONFIG
import game_manager

class PathEntity:
    def __init__(self):
        self.pos = pygame.Vector2(random.randint(0, GLOBALCONFIG.window_width), random.randint(0, GLOBALCONFIG.window_height))
        self.target = pygame.Vector2((GLOBALCONFIG.window_width / 2) + random.randint(-100, 100), (GLOBALCONFIG.window_height / 2) + random.randint(-100, 100))
        self.heading = 0
        self.speed = 2
        
    def loop(self, time):
        self.heading = math.atan2((self.target - self.pos).y, (self.target - self.pos).x)
        self.pos += pygame.Vector2(
            math.cos(self.heading) * self.speed, 
            math.sin(self.heading) * self.speed
        )
        
        self.speed += (math.cos(time / 500)) * 0.01
        print(self.speed)
                
        if (self.target - self.pos).magnitude() <= 2:
            self.heading += random.uniform(-random.uniform(math.pi / 6, math.pi / 4), random.uniform(math.pi / 6, math.pi / 4))
            self.target.update(
                self.pos.x + math.cos(self.heading) * 250, 
                self.pos.y + math.sin(self.heading) * 250
            )
            
            if game_manager.ThePond.out_of_logic_bounds(self.pos):
                self.target.update((GLOBALCONFIG.window_width / 2) + random.randint(-100, 100), (GLOBALCONFIG.window_height / 2) + random.randint(-100, 100))
                
    def debug_draw(self, surface):
        pygame.draw.circle(surface, (0, 255, 0), self.pos, 3)
        pygame.draw.circle(surface, (255, 0, 255), self.target, 3)