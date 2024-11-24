import math
import pygame
from game.entity.path_entity import PathEntity
from lib.boa.art.draw import draw
from lib.boa.math.kinematics.unconstrained.chain import UIKinematicsChain
from lib.boa.math.kinematics.unconstrained.solver import UIKinematicsSolver
from game.logic.trait_collection import TraitCollection

class Fish:
    def __init__(self, color_config, scale: float, traits: TraitCollection):
        self.path_entity = PathEntity()
        self.color_config = color_config
        self.scale = scale
        self.traits = traits
        self.kine_chain = UIKinematicsChain([30, 30, 30, 30, 30])
        
    def update(self, timestamp):
        self.path_entity.loop(timestamp)
        self.kine_chain.update(
            self.path_entity.pos + pygame.Vector2(
                (math.cos(self.path_entity.heading + math.pi / 2) * math.sin(timestamp / 250)) * 35,
                (math.sin(self.path_entity.heading + math.pi / 2) * math.sin(timestamp / 250)) * 35
            ))
        
    def draw(self, surface):
        draw.kine_chain(surface, self.kine_chain)
        self.path_entity.debug_draw(surface)