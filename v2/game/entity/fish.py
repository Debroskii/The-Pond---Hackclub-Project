from entity.path_entity import PathEntity
from logic.trait_collection import TraitCollection

class Fish:
    def __init__(self, color_config, scale: float, traits: TraitCollection):
        self.path_entity = PathEntity()
        self.color_config = color_config
        self.scale = scale
        self.traits = traits
        
    def update(self):
        self.path_entity.loop()
        
    def draw(self):
        pass