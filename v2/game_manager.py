from game.entity.fish import Fish
from lib.boa.art.draw import draw
from lib.boa.math.kinematics.unconstrained.chain import UIKinematicsChain
from config.global_config import GLOBALCONFIG
from game.entity.path_entity import EntityType, PathEntity
from game.entity.group_path_entity import GroupPathEntity
from game.entity.food_objective_entity import FoodObjectiveEntity

class GameManager:
    debug_path_entities = []
    
    for i in range(1):
      debug_path_entities.append(PathEntity(EntityType.INDIVIDUAL))
    
    def update(timestamp):
      for entity in GameManager.debug_path_entities:
        entity.loop(timestamp)
        # entity.console_debugging()
    
    def draw(surface):
      for entity in GameManager.debug_path_entities:
        entity.debug_draw(surface)
        
    def out_of_logic_bounds(object):
        if object.x > GLOBALCONFIG.window_width + 200 or object.y > GLOBALCONFIG.window_height + 200:
            return True
        elif object.x < -200 or object.y < -200:
            return True
        else:
            return False