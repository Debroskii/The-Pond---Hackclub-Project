from lib.boa.art.draw import draw
from lib.boa.math.kinematics.unconstrained.chain import UIKinematicsChain
from config.global_config import GLOBALCONFIG

class ThePond:
    # sampleChain = UIKinematicsChain([60, 60, 30, 50, 20])
    samplePathGenerator = PathGenerator()
    
    def update():
        # ThePond.sampleChain.update()
        ThePond.samplePathGenerator.loop()
    
    def draw(surface):
        # draw.kine_chain(surface, ThePond.sampleChain)
        ThePond.samplePathGenerator.debugDraw()
        
    def out_of_logic_bounds(object):
        if object.x > GLOBALCONFIG.window_width + 200 or object.y > GLOBALCONFIG.window_height + 200:
            return True
        elif object.x < -200 or object.y < -200:
            return True
        else:
            return False