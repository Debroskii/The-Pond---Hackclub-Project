import math
import pygame
from game.entity.path_entity import EntityType, PathEntity, PathMode
from lib.boa.art.draw import draw
from lib.boa.math.kinematics.unconstrained.chain import UIKinematicsChain
from lib.boa.math.kinematics.unconstrained.solver import UIKinematicsSolver
import game_manager
from lib.boa.math.utility import math_util
from game.entity.tail import Tail
from game.art.fish_color_config import FishColorConfig

class Fish:
    def __init__(self, color_config, scale: float):
        self.path_entity = PathEntity(EntityType.INDIVIDUAL)
        self.color_config: FishColorConfig = color_config
        self.scale = scale
        self.kine_chain = UIKinematicsChain([20 * scale, 20 * scale, 20 * scale, 20 * scale, 5 * scale, 7.5 * scale])
        self.kine_sizes = [1.5 * scale, 5 * scale, 10 * scale, 12 * scale, 12 * scale, 6 * scale]
        self.tail = Tail(35 * scale, scale)
        self.curve = 0
        
    def update(self, timestamp):
        speed_modifier = 1
        if self.path_entity.mode == PathMode.GROUP: 
            speed_modifier = max(0.1, min((self.path_entity.target - self.path_entity.pos).magnitude() * 0.01, 2))
        self.path_entity.loop(timestamp, game_manager.GameManager.fish.index(self), speed_modifier)
        
        self.kine_chain.update(self.path_entity.affector_pos)
        self.tail.update(self.kine_chain.links[0], self.kine_sizes[0])
        
        self.curve = 0
        for link in self.kine_chain.links:
            self.curve += self.kine_chain.links[len(self.kine_chain.links) - 1].angle - link.angle
        
    def draw(self, surface):     
        # Forefins   
        forefin_joint = self.kine_chain.links[len(self.kine_chain.links) - 3]
        forefine_joint_radius = self.kine_sizes[len(self.kine_chain.links) - 3]
        forefin_origin = forefin_joint.leading - ((forefin_joint.leading - forefin_joint.trailing) * 0.5)
        
        forefin_position_1 = forefin_origin + math_util.circ_position(forefin_joint.angle + math.pi / 2, forefine_joint_radius)
        forefin_position_2 = forefin_origin + math_util.circ_position(forefin_joint.angle - math.pi / 2, forefine_joint_radius)
        
        # Postfins
        postfin_joint = self.kine_chain.links[1]
        postfin_joint_radius = self.kine_sizes[1]
        postfin_origin = postfin_joint.leading - ((postfin_joint.leading - postfin_joint.trailing) * 0.5)
        
        postfin_position_1 = postfin_origin + math_util.circ_position(postfin_joint.angle + math.pi / 2, postfin_joint_radius)
        postfin_position_2 = postfin_origin + math_util.circ_position(postfin_joint.angle - math.pi / 2, postfin_joint_radius)
        fin_angle = math.pi / 3
        
        # Eyes
        head_joint = self.kine_chain.links[len(self.kine_chain.links) - 1]
        head_joint_radius = self.kine_sizes[len(self.kine_chain.links) - 1]
        eye_origin = head_joint.leading - ((head_joint.leading - head_joint.trailing) * 0.5)
        
        eye_position_1 = eye_origin + math_util.circ_position(head_joint.angle + math.pi / 2, head_joint_radius * 1.5)
        eye_position_2 = eye_origin + math_util.circ_position(head_joint.angle - math.pi / 2, head_joint_radius * 1.5)
        
        eye_lid_position_1 = eye_origin + math_util.circ_position(head_joint.angle + math.pi / 2, head_joint_radius * 1)
        eye_lid_position_2 = eye_origin + math_util.circ_position(head_joint.angle - math.pi / 2, head_joint_radius * 1)
        
        # Dorsal Fin
        front_joint = self.kine_chain.links[len(self.kine_chain.links) - 3]
        front_origin = front_joint.leading - ((front_joint.leading - front_joint.trailing) * 0.1)
        
        
        rear_joint = self.kine_chain.links[len(self.kine_chain.links) - 4]
        rear_origin = rear_joint.trailing + ((rear_joint.leading - rear_joint.trailing) * 0.1)
        
        # Forefins
        draw.rotated_ellipse(surface, self.color_config.accent_color, (forefin_position_1.x, forefin_position_1.y, 28 * self.scale, 13 * self.scale), -forefin_joint.angle - fin_angle)
        draw.rotated_ellipse(surface, self.color_config.accent_color, (forefin_position_2.x, forefin_position_2.y, 28 * self.scale, 13 * self.scale), -forefin_joint.angle + fin_angle)
        
        # Postfins
        draw.rotated_ellipse(surface, self.color_config.accent_color, (postfin_position_1.x, postfin_position_1.y, 22 * self.scale, 9 * self.scale), -postfin_joint.angle - fin_angle)
        draw.rotated_ellipse(surface, self.color_config.accent_color, (postfin_position_2.x, postfin_position_2.y, 22 * self.scale, 9 * self.scale), -postfin_joint.angle + fin_angle)
        
        # Body and Tail
        self.tail.draw(surface, self.color_config.accent_color, self.curve)
        draw.kine_chain(surface, self.color_config.base_color, self.kine_chain, self.kine_sizes)
        
        # Dorsal Fin
        draw.multi_radii_line(surface, self.color_config.accent_color, front_origin, front_joint.trailing, 0.75 * self.scale, 1.5 * self.scale)
        draw.multi_radii_line(surface, self.color_config.accent_color, front_joint.trailing, rear_origin, 1.5 * self.scale, 0.5 * self.scale)

        # Eyes
        pygame.draw.circle(surface, (0, 0, 0), eye_position_1, 4 * self.scale)
        pygame.draw.circle(surface, (0, 0, 0), eye_position_2, 4 * self.scale)
        
        draw.rotated_ellipse(surface, self.color_config.base_color, (eye_lid_position_1.x, eye_lid_position_1.y, 12 * self.scale, 6 * self.scale), -head_joint.angle)
        draw.rotated_ellipse(surface, self.color_config.base_color, (eye_lid_position_2.x, eye_lid_position_2.y, 12 * self.scale, 6 * self.scale), -head_joint.angle)
        
    def debug_draw(self, surface):
        self.path_entity.debug_draw(surface)