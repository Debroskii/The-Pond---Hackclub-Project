import random
from typing import List
import pygame
from game.entity.fish import Fish
from lib.boa.art.draw import draw
from lib.boa.math.kinematics.unconstrained.chain import UIKinematicsChain
from config.global_config import GameConfig
from game.entity.path_entity import EntityType, PathEntity
from game.entity.group_path_entity import GroupPathEntity
from game.entity.food_objective_entity import FoodObjectiveEntity
from lib.boa.art.pattern import Pattern
from game.art.fish_color_config import FishColorConfig

class GameManager:
    fish = []
    groups = []
    food_objectives = []
    
    for i in range(GameConfig.fish_count):
      fish.append(Fish(FishColorConfig.random(), random.randint(50, 100) / 100))
    
    def update(timestamp, dt):
      for fish in GameManager.fish:
        fish.update(timestamp, dt)
      for group in GameManager.groups:
        group.loop(timestamp, dt)
        if group.has_expired(): 
          group.dissolve()
          GameManager.groups.remove(group)
      for food_zone in GameManager.food_objectives:
        food_zone.loop(timestamp, dt)
        if food_zone.has_expired():
          food_zone.dissolve()
          GameManager.food_objectives.remove(food_zone)
      
      if random.randint(1, 300) == 1 and len(GameManager.groups) < GameConfig.group_count:
        GameManager.groups.append(GroupPathEntity())
        
    def draw(surface):
      for food_zone in GameManager.food_objectives:
        food_zone.draw(surface)
        food_zone.debug_draw(surface)
      for fish in GameManager.fish:
        fish.draw(surface)
        fish.debug_draw(surface)
      for group in GameManager.groups:
        group.draw(surface)
        
    def out_of_view_bounds(object):
      if object.x > pygame.display.get_window_size()[0] or object.y > pygame.display.get_window_size()[1]:
          return True
      elif object.x < 0 or object.y < 0:
          return True
      else:
          return False
        
    def out_of_logic_bounds(object):
        if object.x > pygame.display.get_window_size()[0] + 200 or object.y > pygame.display.get_window_size()[1] + 200:
            return True
        elif object.x < -200 or object.y < -200:
            return True
        else:
            return False