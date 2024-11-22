from lib.boa.art.draw import draw
from lib.boa.math.kinematics.unconstrained.chain import UIKinematicsChain


class ThePond:
    sampleChain = UIKinematicsChain([60, 60, 30, 50, 20])
    
    def update():
        ThePond.sampleChain.update()
    
    def draw(surface):
        draw.kine_chain(surface, ThePond.sampleChain)