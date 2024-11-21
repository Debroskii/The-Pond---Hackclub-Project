import pygame
from lib.boa.math.kinematics.unconstrained.chain import UIKinematicsChain
from lib.boa.math.kinematics.link import Link


class draw:
    def draw_kine_link(surface: pygame.Surface, link: Link):
        pygame.draw.circle(surface, (255,255,255), link.leading, 5)
        pygame.draw.circle(surface, (255,255,255), link.trailing, 5)
        pygame.draw.line(surface, (255,255,255), link.leading, link.trailing)

        
    def draw_kine_chain(surface, chain: UIKinematicsChain):
        for link in chain.links:
            draw.draw_kine_link(surface, link)
