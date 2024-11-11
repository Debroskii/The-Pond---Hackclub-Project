import pygame
import math
from kinematics.segment import Segment
from pygame import gfxdraw

class SideFins:
    
    points = [
        [-30, 100],
        [15, 200],
        [-15, 300],
        [30, 300],
    ]
    
    def getTransformation(angle: float, offset: float, scale: float):
        return pygame.Vector2(
            math.cos(angle + offset - math.pi/2) * scale,
            math.sin(angle + offset - math.pi/2) * scale
        )
    
    def getInvertedTransformation(angle: float, offset: float, scale: float):
        return pygame.Vector2(
            math.cos(angle + offset + math.pi/2) * scale,
            math.sin(angle + offset + math.pi/2) * scale
        )
    
    def attach(surface, parent: Segment, scale: float, color: tuple):
        anchor: pygame.Vector2 = parent.b + (parent.a - parent.b) / 3
        
        fin_points = []
        inverted_fin_points = []
        
        for point in SideFins.points:
            fin_points.append(anchor + SideFins.getTransformation(parent.angle, point[0], scale) * point[1] * scale)
            inverted_fin_points.append(anchor + SideFins.getInvertedTransformation(parent.angle, -point[0], scale) * point[1] * scale)
            
        gfxdraw.aapolygon(surface, fin_points, (255, 0, 0))
        gfxdraw.filled_polygon(surface, fin_points, (255, 0, 0))            
        gfxdraw.aapolygon(surface, inverted_fin_points, (0, 255, 0))
        gfxdraw.filled_polygon(surface, inverted_fin_points, (0, 255, 0))       