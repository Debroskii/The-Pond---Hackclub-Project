import math
import pygame
import pygame.gfxdraw
from lib.boa.math.kinematics.unconstrained.chain import UIKinematicsChain
from lib.boa.math.kinematics.link import Link


class draw:
    def kine_link(surface: pygame.Surface, link: Link):
        pygame.draw.circle(surface, (255,255,255), link.leading, 5)
        pygame.draw.circle(surface, (255,255,255), link.trailing, 5)
        pygame.draw.line(surface, (255,255,255), link.leading, link.trailing)
        
    def kine_chain(surface, chain: UIKinematicsChain, sizes):
        for link in chain.links:
            if chain.links.index(link) == len(chain.links) - 1:
                draw.multi_radii_line(
                    surface, (255, 255, 255), link.leading, link.trailing, sizes[chain.links.index(link)], sizes[chain.links.index(link)])
                # print("Segment " + str(chain.links.index(link)) + "\t Radius " + str(sizes[chain.links.index(link)]))
            else:
                draw.multi_radii_connection(
                    surface, 
                    (255, 255, 255), 
                    link.trailing, 
                    link.leading, 
                    chain.links[(chain.links.index(link) + 1)].leading, 
                    sizes[chain.links.index(link)], 
                    sizes[chain.links.index(link) + 1],
                    chain.links.index(link)
                )
                
    def textured_kine_chain(surface, chain: UIKinematicsChain, sizes, texture: pygame.Surface):
        for link in chain.links:
            if chain.links.index(link) == len(chain.links) - 1:
                draw.textured_multi_radii_line(
                    surface, texture, link.leading, link.trailing, sizes[chain.links.index(link)], sizes[chain.links.index(link)])
                # print("Segment " + str(chain.links.index(link)) + "\t Radius " + str(sizes[chain.links.index(link)]))
            else:
                draw.textured_multi_radii_connection(
                    surface, 
                    texture, 
                    link.trailing, 
                    link.leading, 
                    chain.links[(chain.links.index(link) + 1)].leading, 
                    sizes[chain.links.index(link)], 
                    sizes[chain.links.index(link) + 1],
                    chain.links.index(link)
                )
                
    def textured_multi_radii_line(surface, texture: pygame.Surface, start: pygame.Vector2, end: pygame.Vector2, start_radius: int, end_radius: int):
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
        
        pygame.draw.circle(surface, (255, 255, 255), start, start_radius)
        pygame.draw.circle(surface, (255, 255, 255), end, end_radius)
        pygame.gfxdraw.textured_polygon(surface, points, texture, 0, 0)

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
        
    def textured_multi_radii_connection(surface, texture: pygame.Surface, start: pygame.Vector2, middle: pygame.Vector2, end: pygame.Vector2, start_radius: int, end_radius: int, index):
        middle_radius = start_radius
        if start_radius >= end_radius:
            middle_radius = end_radius
        else:
            middle_radius = start_radius

        # print('Segment ' + str(index) + '\t Start Radius ' + str(start_radius) + '\t Middle Radius ' + str(middle_radius) + '\t End Radius ' + str(end_radius))
            
        draw.textured_multi_radii_line(surface, texture, start, middle, start_radius, end_radius)
        
    def multi_radii_connection(surface, color, start: pygame.Vector2, middle: pygame.Vector2, end: pygame.Vector2, start_radius: int, end_radius: int, index):
        middle_radius = start_radius
        if start_radius >= end_radius:
            middle_radius = end_radius
        else:
            middle_radius = start_radius

        # print('Segment ' + str(index) + '\t Start Radius ' + str(start_radius) + '\t Middle Radius ' + str(middle_radius) + '\t End Radius ' + str(end_radius))
            
        draw.multi_radii_line(surface, color, start, middle, start_radius, end_radius)
        
    def text(surface, font: pygame.font.Font, text, color, position):
        text_surface = font.render(text, False, color)
        surface.blit(text_surface, position)
        
    def fract_circle(surface, color, position, radius, angle, span, resolution = 1):
        points = [position]
        for i in range(resolution):
            span_amount = (span / resolution) * (resolution + 1 - i)
            points.append(pygame.Vector2(position.x + math.cos(angle - span_amount) * radius, position.y + math.sin(angle - span_amount) * radius))
            
        points.append(pygame.Vector2(position.x + math.cos(angle) * radius, position.y + math.sin(angle) * radius))
        
        for i in range(resolution):
            span_amount = (span / resolution) * i
            points.append(pygame.Vector2(position.x + math.cos(angle + span_amount) * radius, position.y + math.sin(angle + span_amount) * radius))
            
        pygame.draw.polygon(surface, color, points)
        
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
        rotated_surf = pygame.transform.rotate(shape_surf, angle / math.pi * 180)
        surface.blit(rotated_surf, rotated_surf.get_rect(center = target_rect.topleft))
        
        # Debug
        pygame.draw.line(surface, (255, 0, 0), (target_rect.x, 0), (target_rect.x, 900), 2)
        pygame.draw.line(surface, (255, 0, 0), (0, target_rect.y), (900, target_rect.y), 2)
        pygame.draw.line(surface, (255, 0, 0), (0, 0), (900, 900), 2)
        pygame.draw.line(surface, (255, 0, 0), (0, 900), (900, 0), 2)

        pygame.draw.circle(surface, (0, 255, 0), (target_rect.x, target_rect.y), 5)