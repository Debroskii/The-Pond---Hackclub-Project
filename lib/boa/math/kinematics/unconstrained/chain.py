import pygame
from lib.boa.math.kinematics.link import Link
from lib.boa.math.kinematics.unconstrained.solver import UIKinematicsSolver


class UIKinematicsChain:
    def __init__(self, chain_lengths, max_bend):
        self.links = []
        self.max_bend = max_bend
        
        for length in chain_lengths:
            self.links.append(Link(length, length, 0, length))
            
    def update(self, leader):
        for link in self.links:
            if self.links.index(link) != len(self.links) - 1:
                UIKinematicsSolver.solve(link, self.links[self.links.index(link) + 1], self.max_bend)
            else:
                UIKinematicsSolver.solveToVector(link, leader)