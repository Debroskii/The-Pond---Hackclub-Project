from logic.trait_collection import TraitCollection

class Fish:
    def __init__(self, color_config, scale: float, traits: TraitCollection):
        self.color_config = color_config
        self.scale = scale
        self.traits = traits