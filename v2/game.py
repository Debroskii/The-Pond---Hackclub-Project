from lib.boa.art.draw import draw
from lib.boa.math.kinematics.unconstrained.chain import UIKinematicsChain


class ThePond:
    sampleChain = UIKinematicsChain([30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30])
    
    def update():
        ThePond.sampleChain.update()
    
    def draw(surface):
        draw.draw_kine_chain(surface, ThePond.sampleChain)