import math
import pygame
from game.entity.path_entity import EntityType, PathEntity
from lib.boa.art.draw import draw
from lib.boa.math.kinematics.unconstrained.chain import UIKinematicsChain
from lib.boa.math.kinematics.unconstrained.solver import UIKinematicsSolver
import game_manager
from lib.boa.math.utility import math_util

class Fish:
    def __init__(self, color_config, scale: float):
        self.path_entity = PathEntity(EntityType.INDIVIDUAL)
        self.color_config = color_config
        self.scale = scale
        self.kine_chain = UIKinematicsChain([25, 20, 20, 20, 5, 0])
        self.kine_sizes = [2, 5, 10, 12, 12, 10]
        
    def update(self, timestamp):
        self.path_entity.loop(timestamp)
        self.kine_chain.update(self.path_entity.affector_pos)
        
    def draw(self, surface):        
        forefin_joint = self.kine_chain.links[len(self.kine_chain.links) - 3]
        forefine_joint_radius = self.kine_sizes[len(self.kine_chain.links) - 3]
        forefin_origin = forefin_joint.leading - ((forefin_joint.leading - forefin_joint.trailing) * 0.5)
        
        forefin_position_1 = forefin_origin + math_util.circ_position(forefin_joint.angle + math.pi / 2, forefine_joint_radius)
        forefin_position_2 = forefin_origin + math_util.circ_position(forefin_joint.angle - math.pi / 2, forefine_joint_radius)
        fin_angle = math.pi / 3
        
        postfin_joint = self.kine_chain.links[1]
        postfin_joint_radius = self.kine_sizes[1]
        postfin_origin = postfin_joint.leading - ((postfin_joint.leading - postfin_joint.trailing) * 0.5)
        
        postfin_position_1 = postfin_origin + math_util.circ_position(postfin_joint.angle + math.pi / 2, postfin_joint_radius)
        postfin_position_2 = postfin_origin + math_util.circ_position(postfin_joint.angle - math.pi / 2, postfin_joint_radius)
        
        draw.rotated_ellipse(surface, (0, 0, 0), (forefin_position_1.x, forefin_position_1.y, 28, 13), -forefin_joint.angle - fin_angle)
        draw.rotated_ellipse(surface, (0, 0, 0), (forefin_position_2.x, forefin_position_2.y, 28, 13), -forefin_joint.angle + fin_angle)
        
        draw.rotated_ellipse(surface, (0, 0, 0), (postfin_position_1.x, postfin_position_1.y, 22, 9), -postfin_joint.angle - fin_angle)
        draw.rotated_ellipse(surface, (0, 0, 0), (postfin_position_2.x, postfin_position_2.y, 22, 9), -postfin_joint.angle + fin_angle)
        
        draw.kine_chain(surface, self.kine_chain, self.kine_sizes)
        
    def debug_draw(self, surface):
        self.path_entity.debug_draw(surface)

        forefin_joint = self.kine_chain.links[len(self.kine_chain.links) - 3]
        forefine_joint_radius = self.kine_sizes[len(self.kine_chain.links) - 3]
        forefin_joint_offset = (forefin_joint.leading - forefin_joint.trailing) * 0.3
        forefin_origin = forefin_joint.leading - forefin_joint_offset
        
        forefin_position_1 = forefin_origin + math_util.circ_position(forefin_joint.angle + math.pi / 2, forefine_joint_radius)
        forefin_position_2 = forefin_origin + math_util.circ_position(forefin_joint.angle - math.pi / 2, forefine_joint_radius)
        
        pygame.draw.circle(surface, (255, 0, 0), forefin_origin, 3)
        pygame.draw.circle(surface, (255, 0, 0), forefin_position_1, 2)
        pygame.draw.circle(surface, (255, 0, 0), forefin_position_2, 2)
