from game.entity.fish import Fish
from lib.boa.art.draw import draw
from lib.boa.math.kinematics.unconstrained.chain import UIKinematicsChain
from config.global_config import GLOBALCONFIG
from game.logic.trait_collection import TraitCollection

class ThePond:
    fish = Fish(0, 1, TraitCollection(1))
    
    def update(timestamp):
        ThePond.fish.update(timestamp)
    
    def draw(surface):
        ThePond.fish.draw(surface)
        
    def out_of_logic_bounds(object):
        if object.x > GLOBALCONFIG.window_width + 200 or object.y > GLOBALCONFIG.window_height + 200:
            return True
        elif object.x < -200 or object.y < -200:
            return True
        else:
            return False