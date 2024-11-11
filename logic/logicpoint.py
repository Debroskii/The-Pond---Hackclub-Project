import math
import pygame as pg
import random as rand

from lib.pydraw.math.translation import translation

class LogicPoint:
    def __init__(self):
        self.pos = pg.Vector2(rand.randint(0, 900), rand.randint(0, 900))
        self.vel = pg.Vector2(0, 0)
        self.target_vel = pg.Vector2(0, 0)
        self.target_pos = pg.Vector2(rand.randint(0, 900), rand.randint(0, 900))
        self.speed = 1
    
    def update(self, frame: float, angle: float):
        angle = math.atan2((self.target_pos - self.pos).y, (self.target_pos - self.pos).x)
        self.pos += self.vel
        
        self.speed = (0.5 * math.sin(frame)) + 1.25
        
        if (self.target_pos - self.pos).magnitude() > 2:
            self.vel.update(math.cos(angle) * 2 * self.speed, math.sin(angle) * self.speed)
            
        if (self.target_pos - self.pos).magnitude() <= 2:
            new_angle = angle + rand.randint(-100, 100) / 100 * ((math.pi/8))
            new_magnitude = rand.randint(50, 100)
            new_pos = pg.Vector2(self.pos.x + math.cos(new_angle) * new_magnitude, self.pos.y + math.sin(new_angle) * new_magnitude)
                        
            if translation.out_of_bounds(new_pos):
                new_angle *= 2
                new_pos = pg.Vector2(self.pos.x + math.cos(new_angle) * new_magnitude, self.pos.y + math.sin(new_angle) * new_magnitude)
                        
            self.target_pos = new_pos
        print(self.target_pos)