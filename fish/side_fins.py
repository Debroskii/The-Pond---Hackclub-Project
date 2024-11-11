import pygame
import math
from lib.pydraw.kinematics.segment import Segment
from pygame import gfxdraw
from lib.pydraw.draw import draw
from lib.pydraw.math.translation import translation

class SideFins:
    
    def attach(surface, parent: Segment, scale: float, color: tuple):
        anchor: pygame.Vector2 = parent.b + (parent.a - parent.b) / 1.5
        
        fin_width: float = 20 * scale
        fin_height: float = 8 * scale
        
        offset = anchor + translation.get_transformation(parent.angle, scale)
        reflected_offset = anchor + translation.get_reflected_transformation(parent.angle, scale)
        
        draw.rotated_ellipse(surface, color, [offset.x, offset.y, fin_width, fin_height], -parent.angle - math.pi/2.5)
        draw.rotated_ellipse(surface, color, [reflected_offset.x, reflected_offset.y, fin_width, fin_height], -parent.angle + math.pi/2.5)
        