from enum import Enum
import math
import random
import pygame

from config.global_config import GLOBALCONFIG
import game_manager
from lib.boa.art.draw import draw

class PathMode(Enum):
    WANDER = 0
    GROUP = 1
    EAT = 2
    
class EntityType(Enum):
    INDIVIDUAL = 0
    GROUP = 1

class PathEntity:
    def __init__(self, type: EntityType):
        self.mode: PathMode = PathMode.WANDER
        self.type = type
        self.pos = pygame.Vector2((GLOBALCONFIG.window_width / 2) + random.randint(-100, 100), (GLOBALCONFIG.window_height / 2) + random.randint(-100, 100))
        self.affector_pos = self.pos
        self.target = self.pos + pygame.Vector2(random.randint(-20, 20), random.randint(-20, 20))
        self.heading = 0
        self.speed = 2
        
    def loop(self, time):
        self.heading = math.atan2((self.target - self.pos).y, (self.target - self.pos).x)
        self.pos += pygame.Vector2(
            math.cos(self.heading) * self.speed, 
            math.sin(self.heading) * self.speed
        )
        
        self.affector_pos = self.pos + pygame.Vector2(
                (math.cos(self.heading + math.pi / 2) * math.sin(time / 250)) * self.speed * 7.5,
                (math.sin(self.heading + math.pi / 2) * math.sin(time / 250)) * self.speed * 7.5
        )
        
        self.speed += (math.cos(time / 500)) * 0.01
                
        if (self.target - self.pos).magnitude() <= 2 and self.mode == PathMode.WANDER:
            self.heading += random.uniform(-random.uniform(math.pi / 6, math.pi / 4), random.uniform(math.pi / 6, math.pi / 4))
            self.target.update(
                self.pos.x + math.cos(self.heading) * 150, 
                self.pos.y + math.sin(self.heading) * 150
            )
            
            if game_manager.GameManager.out_of_logic_bounds(self.pos):
                self.target.update((GLOBALCONFIG.window_width / 2) + random.randint(-300, 300), (GLOBALCONFIG.window_height / 2) + random.randint(-300, 300))
                
    def debug_draw(self, surface):
        pygame.draw.circle(surface, (0, 255, 0), self.pos, 3)
        pygame.draw.circle(surface, (255, 0, 255), self.target, 3)
        pygame.draw.line(surface, (155, 155, 155), self.pos, self.target)
        
        # draw.fract_circle(surface, (105, 55, 55), self.pos, 1000, self.heading, math.pi / 1.25, 10)
        
        draw.text(
            surface, 
            pygame.font.SysFont("Cascadia Code PL", 10),
            "Entity",
            (255, 255, 255),
            self.pos + pygame.Vector2(-20, -20)
        )
        
        draw.text(
            surface, 
            pygame.font.SysFont("Cascadia Code PL", 10),
            "Target",
            (255, 255, 255),
            self.target + pygame.Vector2(-18, -20)
        )
        
    def console_debugging(self):
        target_mode_string = "\tTarget Mode: " + self.mode.name
        target_string = "\tTarget: " + str(self.target)
        position_string = "\tPosition: " + str(self.pos)
        heading_string = "\tHeading (degrees): " + str(round((self.heading / math.pi) * 180, 2))
        speed_string = "\tSpeed: " + str(round(self.speed, 2))
        
        print("<PATH ENTITY>" + target_mode_string + target_string + position_string + heading_string + speed_string)