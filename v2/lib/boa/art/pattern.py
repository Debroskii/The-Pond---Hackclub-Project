import math
import random

import pygame


class Pattern:
    def __init__(self, resolution):
        self.res = resolution
        self.seed = random.randint(0, 1000000)
        self.points = []
        
        for i in range(15):
            self.points.append(pygame.Vector2(random.randint(0, pygame.display.get_window_size()[0]), random.randint(0, pygame.display.get_window_size()[1])))
        
    def draw(self, surface, base_color, pattern_color):
        pattern_surface = pygame.Surface(pygame.display.get_window_size())
        pattern_surface.fill(base_color)
        
        for row in range(self.res):
            for col in range(self.res):
                unit_width = pygame.display.get_window_size()[0] / self.res
                unit_height = pygame.display.get_window_size()[1] / self.res
                position = pygame.Vector2(unit_width * col, unit_height * row)
                closest_point_magnitude = 1000
                for point in self.points:
                    if (point - position).magnitude() < closest_point_magnitude:
                        closest_point_magnitude = (point - position).magnitude()
                
                scale = 1 - max(0, min(closest_point_magnitude * 0.025 * abs(row / (col + 1)), 1))
                
                pygame.draw.circle(pattern_surface, pattern_color, position - pygame.Vector2(unit_width / 2, unit_height / 2), unit_width * 2 * scale)
                
        # surface.blit(pattern_surface, (0, 0))
        return pattern_surface