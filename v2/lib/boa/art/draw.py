import math
import pygame
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