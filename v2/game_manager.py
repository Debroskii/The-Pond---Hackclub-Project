import random
from typing import List
import pygame
from game.entity.fish import Fish
from lib.boa.art.draw import draw
from lib.boa.math.kinematics.unconstrained.chain import UIKinematicsChain
from config.global_config import GLOBALCONFIG
from game.entity.path_entity import EntityType, PathEntity
from game.entity.group_path_entity import GroupPathEntity
from game.entity.food_objective_entity import FoodObjectiveEntity
from lib.boa.art.pattern import Pattern
from game.art.fish_color_config import FishColorConfig

class GameManager:
    fish = []
    groups = []
    food_objectives = []
    
    for i in range(GLOBALCONFIG.fish_count):
      fish.append(Fish(FishColorConfig.random(), random.randint(50, 100) / 100))
    
    def update(timestamp):
      for fish in GameManager.fish:
        fish.update(timestamp)
      for group in GameManager.groups:
        group.loop(timestamp)
        if group.has_expired(): 
          group.dissolve()
          GameManager.groups.remove(group)
      
      if random.randint(1, 300) == 1 and len(GameManager.groups) < GLOBALCONFIG.group_count:
        GameManager.groups.append(GroupPathEntity())
        
    def draw(surface):
      for fish in GameManager.fish:
        fish.draw(surface)
        
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