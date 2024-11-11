import pygame
import math

class draw:
    def rotated_rect(surface, color: tuple, rect, angle: float, width: int = 0):
        target_rect: pygame.Rect = pygame.Rect(rect)
        shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
        pygame.draw.rect(shape_surf, color, (0, 0, *target_rect.size), width)
        rotated_surf = pygame.transform.rotate(shape_surf, angle * 180/math.pi)
        surface.blit(rotated_surf, rotated_surf.get_rect(center = target_rect.topleft))
        
    def rotated_ellipse(surface, color: tuple, rect, angle: float, width: int = 0):
        target_rect = pygame.Rect(rect)
        shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
        pygame.draw.ellipse(shape_surf, color, (0, 0, *target_rect.size), width)
        rotated_surf = pygame.transform.rotate(shape_surf, angle * 180/math.pi)
        surface.blit(rotated_surf, rotated_surf.get_rect(center = target_rect.topleft))