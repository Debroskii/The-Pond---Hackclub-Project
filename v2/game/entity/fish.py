import math
import pygame
from game.entity.path_entity import EntityType, PathEntity
from lib.boa.art.draw import draw
from lib.boa.math.kinematics.unconstrained.chain import UIKinematicsChain
from lib.boa.math.kinematics.unconstrained.solver import UIKinematicsSolver
import game_manager

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
        draw.kine_chain(surface, self.kine_chain, self.kine_sizes)
        self.path_entity.debug_draw(surface)