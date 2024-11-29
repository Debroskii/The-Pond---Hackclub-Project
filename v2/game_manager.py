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
    
    for i in range(1):
      debug_path_entities.append(Fish(0, 1))
    
    def update(timestamp):
      for entity in GameManager.debug_path_entities:
        entity.update(timestamp)
    
    def draw(surface):
      for entity in GameManager.debug_path_entities:
        entity.draw(surface)
        
    def out_of_view_bounds(object):
      if object.x > GLOBALCONFIG.window_width or object.y > GLOBALCONFIG.window_height:
          return True
      elif object.x < 0 or object.y < 0:
          return True
      else:
          return False
        
    def out_of_logic_bounds(object):
        if object.x > GLOBALCONFIG.window_width + 200 or object.y > GLOBALCONFIG.window_height + 200:
            return True
        elif object.x < -200 or object.y < -200:
            return True
        else:
            return False