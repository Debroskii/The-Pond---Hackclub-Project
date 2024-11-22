import math

import pygame
from lib.boa.math.kinematics.link import Link


class UIKinematicsSolver:
    def solve(follower: Link, leader: Link):
        transformation = follower.trailing - leader.trailing
        follower.angle = math.atan2(transformation.y, transformation.x)
        
        follower.leading = leader.trailing
        follower.trailing = leader.trailing + transformation
        follower.solveTrailing()
        
    def solveToVector(follower: Link, leader: pygame.Vector2):
        transformation = follower.trailing - leader
        follower.angle = math.atan2(transformation.y, transformation.x)
        
        follower.leading = leader
        follower.trailing = leader + transformation
        follower.solveTrailing()