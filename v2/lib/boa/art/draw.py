import math
import pygame
from lib.boa.math.kinematics.unconstrained.chain import UIKinematicsChain
from lib.boa.math.kinematics.link import Link


class draw:
    def kine_link(surface: pygame.Surface, link: Link):
        pygame.draw.circle(surface, (255,255,255), link.leading, 5)
        pygame.draw.circle(surface, (255,255,255), link.trailing, 5)
        pygame.draw.line(surface, (255,255,255), link.leading, link.trailing)
        
    def kine_chain(surface, chain: UIKinematicsChain):
        for link in chain.links:
            if chain.links.index(link) == 0 or chain.links.index(link) == len(chain.links) - 1:
                draw.multi_radii_line(surface, (255, 255, 255), link.leading, link.trailing, 10, 10)
            else:
                draw.multi_radii_connection(surface, (255, 0, 255), link.leading, link.trailing, chain.links[chain.links.index(link) + 1].trailing, 10, 10)

    def multi_radii_line(surface, color, start: pygame.Vector2, end: pygame.Vector2, start_radius: int, end_radius: int):
        start1, start2 = start.copy(), start.copy()
        end1, end2 = end.copy(), end.copy()
        
        n_angle, m_angle = math.atan2((end - start).y, (end - start).x), math.atan2((start - end).y, (start - end).x)
        
        start1.update(
            start.x + start_radius * math.cos(n_angle + math.pi/2), 
            start.y + start_radius * math.sin(n_angle + math.pi/2)
        )
        start2.update(
            start.x + start_radius * math.cos(n_angle - math.pi/2), 
            start.y + start_radius * math.sin(n_angle - math.pi/2)
        )
        
        end1.update(
            end.x + end_radius * math.cos(m_angle + math.pi/2), 
            end.y + end_radius * math.sin(m_angle + math.pi/2)
        )
        end2.update(
            end.x + end_radius * math.cos(m_angle - math.pi/2), 
            end.y + end_radius * math.sin(m_angle - math.pi/2)
        )
        
        points = [start1, start2, end1, end2]
        
        pygame.draw.polygon(surface, color, points)
        pygame.draw.circle(surface, color, start, start_radius)
        pygame.draw.circle(surface, color, end, end_radius)
        
    def multi_radii_connection(surface, color, start: pygame.Vector2, middle: pygame.Vector2, end: pygame.Vector2, start_radius: int, end_radius: int):
        middle_radius = start_radius
        if start_radius < end_radius:
            middle_radius = end_radius
            
        draw.multi_radii_line(surface, color, start, middle, start_radius, middle_radius)
        draw.multi_radii_line(surface, color, middle, end, middle_radius, end_radius)