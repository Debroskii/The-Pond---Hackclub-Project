from game.entity.fish import Fish
from lib.boa.art.draw import draw
from lib.boa.math.kinematics.unconstrained.chain import UIKinematicsChain
from config.global_config import GLOBALCONFIG
from game.entity.path_entity import PathEntity
from game.entity.group_path_entity import GroupPathEntity

class GameManager:
    debug_path_entity = GroupPathEntity()
    
    def update(timestamp):
        GameManager.debug_path_entity.loop(timestamp)
        # GameManager.debug_path_entity.console_debugging()
    
    def draw(surface):
        GameManager.debug_path_entity.draw(surface)
        
    def out_of_logic_bounds(object):
        if object.x > GLOBALCONFIG.window_width + 200 or object.y > GLOBALCONFIG.window_height + 200:
            return True
        elif object.x < -200 or object.y < -200:
            return True
        else:
            return False