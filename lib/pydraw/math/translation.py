import pygame, math

class translation:
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