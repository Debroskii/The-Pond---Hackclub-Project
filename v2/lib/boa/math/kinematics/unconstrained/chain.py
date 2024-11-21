import pygame
from lib.boa.math.kinematics.link import Link
from lib.boa.math.kinematics.unconstrained.solver import UIKinematicsSolver


class UIKinematicsChain:
    def __init__(self, chain_lengths):
        self.links = []
        
        for length in chain_lengths:
            self.links.append(Link(length, length, 0, length))
            
    def update(self):
        for link in self.links:
            if self.links.index(link) != len(self.links) - 1:
                UIKinematicsSolver.solve(link, self.links[self.links.index(link) + 1])
            else:
                UIKinematicsSolver.solveToVector(link, pygame.Vector2(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]))