import pygame as pg
import random as rand

class LogicPoint:
    pos = pg.Vector2(rand.randint(0, 900), rand.randint(0, 900))
    vel = pg.Vector2(0, 0)
    target_vel = pg.Vector2(0, 0)
    target_pos = pg.Vector2(rand.randint(0, 900), rand.randint(0, 900))
    
    def update(self):
        self.pos += self.vel
        
        self.vel = self.target_vel
        
        if (self.target_pos - self.pos).magnitude() > 2:
            self.target_vel.x += (self.target_pos.x - self.pos.x) * 0.001
            self.target_vel.y += (self.target_pos.y - self.pos.y) * 0.001
            
        if (self.target_pos - self.pos).magnitude() <= 2:
            self.target_pos = pg.Vector2(rand.randint(0, 900), rand.randint(0, 900))

    def draw(self, surface):
        pg.draw.circle(surface, (255, 0, 0), self.target_pos, 2)
        pg.draw.circle(surface, (255, 255, 255), self.pos, 3)
        pg.draw.line(surface, (0, 255, 0), self.pos, self.pos + self.vel)