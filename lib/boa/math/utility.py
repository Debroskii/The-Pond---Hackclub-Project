import math
import pygame


class math_util:
    def circ_position(angle: float, radius: float):
        return pygame.Vector2(radius * math.cos(angle), radius * math.sin(angle))