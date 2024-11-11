from lib.pydraw.kinematics.segment import Segment
import pygame, math

from lib.pydraw.math.translation import translation

class Face:
    def attach(surface, parent: Segment, scale: float, color: tuple):
        anchor: pygame.Vector2 = parent.b + (parent.a - parent.b) / 5
        
        eye_radius: float = 2 * scale
        
        offset = anchor + translation.get_transformation(parent.angle, scale)
        reflected_offset = anchor + translation.get_reflected_transformation(parent.angle, scale)
        
        pygame.draw.circle(surface, (0, 0, 0), offset, eye_radius)
        pygame.draw.circle(surface, (0, 0, 0), reflected_offset, eye_radius)