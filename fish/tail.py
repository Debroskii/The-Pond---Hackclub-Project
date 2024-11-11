import pygame
import math
from pygame import gfxdraw


class Tail:
    a = pygame.Vector2()
    b = pygame.Vector2()
    angle = 0
    scale = 0
    length = 0
    color = ()
    body_color = ()
    
    def __init__(self, x, y, angle, scale, color, body_color):
        self.a.update(x, y)
        self.angle = angle
        self.scale = scale
        self.length = 60 * scale
        self.color = color
        self.body_color = body_color
        self.b.update(math.sin(angle) * self.length, math.cos(angle) * self.length)
        
    def solveA(self):
        self.a.update(
            self.b.x + (self.length * math.cos(self.angle)),
            self.b.y + (self.length * math.sin(self.angle))
        )
        
    def align(self, c):
        transformation = self.a - pygame.Vector2(c[0], c[1])
        self.angle = math.atan2(transformation.y, transformation.x)
        
        self.a = pygame.Vector2.__add__(c, transformation)
           
    def anchor(self, c):
        self.b = pygame.Vector2(c[0], c[1])
        self.solveA()
        
    def solve(self, c):
        self.align(c)
        self.anchor(c)
        
    def draw(self, surface):
        a_radius = 15 * self.scale
        b_radius = 7.6 * self.scale
            
        a_radius /= 4
        b_radius /= 4
        
        self.outline(surface, self.a, self.b, a_radius, b_radius)
        gfxdraw.aacircle(surface, int(self.a.x), int(self.a.y), int(a_radius/1.025), self.color)
        gfxdraw.aacircle(surface, int(self.b.x), int(self.b.y), int(b_radius/1.025), self.body_color)
        gfxdraw.filled_circle(surface, int(self.a.x), int(self.a.y), int(a_radius/1.025), self.color)
        gfxdraw.filled_circle(surface, int(self.b.x), int(self.b.y), int(b_radius/1.025), self.body_color)
    
    def outline(self, surface, n: pygame.Vector2, m: pygame.Vector2, n_radius, m_radius):
        n1, n2 = n.copy(), n.copy()
        m1, m2 = m.copy(), m.copy()
        
        n_angle, m_angle = math.atan2((m - n).y, (m - n).x), math.atan2((n - m).y, (n - m).x)
        
        n1.update(
            n.x + n_radius * math.cos(n_angle + math.pi/2), 
            n.y + n_radius * math.sin(n_angle + math.pi/2)
        )
        n2.update(
            n.x + n_radius * math.cos(n_angle - math.pi/2), 
            n.y + n_radius * math.sin(n_angle - math.pi/2)
        )
        
        m1.update(
            m.x + m_radius * math.cos(m_angle + math.pi/2), 
            m.y + m_radius * math.sin(m_angle + math.pi/2)
        )
        m2.update(
            m.x + m_radius * math.cos(m_angle - math.pi/2), 
            m.y + m_radius * math.sin(m_angle - math.pi/2)
        )
        
        points = [n1, n2, m1, m2]
        
        gfxdraw.aapolygon(surface, points, self.color)
        gfxdraw.filled_polygon(surface, points, self.color)