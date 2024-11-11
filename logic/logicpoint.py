import math
import pygame as pg
import random as rand

class LogicPoint:
    pos = pg.Vector2(rand.randint(0, 900), rand.randint(0, 900))
    vel = pg.Vector2(0, 0)
    target_vel = pg.Vector2(0, 0)
    target_pos = pg.Vector2(rand.randint(0, 900), rand.randint(0, 900))
    
    def update(self, angle: float, frame: float):
        self.pos += self.vel
        
        self.vel = self.target_vel
        self.vel *= math.cos(frame)
        
        if (self.target_pos - self.pos).magnitude() > 2:
            self.target_vel.x = (self.target_pos.x - self.pos.x) * 0.025
            self.target_vel.y = (self.target_pos.y - self.pos.y) * 0.025
            
        if (self.target_pos - self.pos).magnitude() <= 2:
            new_angle = angle + rand.randint(-100, 100) / 100 * (math.pi/2)
            new_magnitude = rand.randint(5, 100)
            
            self.target_pos = pg.Vector2(self.pos.x + math.cos(new_angle) * new_magnitude, self.pos.y + math.sin(new_angle) * new_magnitude)

    def draw(self, surface):
        pg.draw.circle(surface, (255, 0, 0), self.target_pos, 2)
        pg.draw.circle(surface, (255, 255, 255), self.pos, 3)
        pg.draw.line(surface, (0, 255, 0), self.pos, self.pos + self.vel)