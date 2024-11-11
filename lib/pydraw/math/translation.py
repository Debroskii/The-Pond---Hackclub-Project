import pygame, math

from game_config import GAMECONFIG

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
        
    def out_of_bounds(position: pygame.Vector2):
        if position.x > GAMECONFIG.width or position.y > GAMECONFIG.height:
            return True
        if position.x < 0 or position.y < 0:
            return True
        return False