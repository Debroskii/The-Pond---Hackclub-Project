import random
from fish.koi import KoiFish
from fish.pond_config import PONDCONFIG


class KoiEngine:
    def __init__(self, count: int):
        self.fish_count = count
        self.fish = []
        for i in range(self.fish_count):
            self.fish.append(
                KoiFish(PONDCONFIG.color_configs[random.randint(0, len(PONDCONFIG.color_configs) - 1)], random.randint(50, 100) / 100)
            )
            
    def loop(self, frame, surface):
        for koi in self.fish:
            koi.update(frame);
            koi.draw(surface)