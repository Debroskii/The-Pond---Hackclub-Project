import pygame
from game.entity.fish import Fish
from lib.boa.art.draw import draw
from lib.boa.math.kinematics.unconstrained.chain import UIKinematicsChain
from config.global_config import GLOBALCONFIG
from game.entity.path_entity import EntityType, PathEntity
from game.entity.group_path_entity import GroupPathEntity
from game.entity.food_objective_entity import FoodObjectiveEntity
from lib.boa.art.pattern import Pattern

class GameManager:
    debug_path_entities = []
    pattern: Pattern
    # test_pattern: Pattern
    
    for i in range(1):
      debug_path_entities.append(Fish(0, 1))
      
    def init():
      # GameManager.test_pattern = Pattern(300)
      GameManager.pattern = Pattern(300)
    
    def update(timestamp):
      for entity in GameManager.debug_path_entities:
        entity.update(timestamp)
        # entity.console_debugging()
        # return
    
    def draw(surface):
      for entity in GameManager.debug_path_entities:
        entity.draw(surface, GameManager.pattern.draw(surface, (255, 255, 255), (168, 58, 50)))
      # GameManager.test_pattern.draw(surface, pygame.Color(255, 255, 255), pygame.Color(168, 58, 50))
        
    def out_of_logic_bounds(object):
        if object.x > GLOBALCONFIG.window_width + 200 or object.y > GLOBALCONFIG.window_height + 200:
            return True
        elif object.x < -200 or object.y < -200:
            return True
        else:
            return False