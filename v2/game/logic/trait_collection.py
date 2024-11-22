from random import random
from logic.trait import Trait


class TraitCollection:
    def __init__(self, trait_count: int):
        self.trait_count = trait_count
        self.traits = []
        
    def populate_random(self):
        for i in range(self.trait_count):
            self.traits.append(random.choice(list(Trait)))