import pygame
import math
from kinematics.segment import Segment
from pygame import gfxdraw
from lib.pydraw.draw import draw

class SideFins:
    
    def get_transformation(angle: float, scale: float):
        return pygame.Vector2(
            math.sin(-angle) * 7.5 * scale,
            math.cos(-angle) * 7.5 * scale
        )
        
    def get_reflected_transformation(angle: float, scale: float):
        return pygame.Vector2(
            math.sin(-angle + math.pi) * 7.5 * scale,
            math.cos(-angle + math.pi) * 7.5 * scale
        )
    
    def attach(surface, parent: Segment, scale: float, color: tuple):
        anchor: pygame.Vector2 = parent.b + (parent.a - parent.b) / 1.5
        
        fin_width: float = 20 * scale
        fin_height: float = 8 * scale
        
        offset = anchor + SideFins.get_transformation(parent.angle, scale)
        reflected_offset = anchor + SideFins.get_reflected_transformation(parent.angle, scale)
        
        draw.rotated_ellipse(surface, color, [offset.x, offset.y, fin_width, fin_height], -parent.angle - math.pi/2.5)
        draw.rotated_ellipse(surface, color, [reflected_offset.x, reflected_offset.y, fin_width, fin_height], -parent.angle + math.pi/2.5)
        