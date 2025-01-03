import math
from lib.boa.math.kinematics.link import Link
from lib.boa.art.draw import draw
from lib.boa.math.kinematics.unconstrained.solver import UIKinematicsSolver


class Tail:
    def __init__(self, length, scale: float):
        self.link = Link(0, 0, 0, length)
        self.radii: tuple
        self.scale = scale
        
    def update(self, leader, radius):
        UIKinematicsSolver.solve(self.link, leader, math.pi / 4)
        self.radii = (radius * self.scale, radius * 2 * self.scale)
        
    def draw(self, surface, color, curve):
        draw.multi_radii_line(surface, color, self.link.leading, self.link.trailing, self.radii[0], self.radii[1] * max(1, min(abs(curve * 0.5), 1.25)))