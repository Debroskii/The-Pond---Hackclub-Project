import math
import random

import pygame
from logic.motive.Motive import Motive


class PondMotives:
    motives = []
    
    def add(motive: Motive):
        PondMotives.motives.append(motive)
        
    def generateTarget():
        motive = PondMotives.motives[len(PondMotives.motives) - 1]
        angle = (random.randint(0, 200) / 100) * math.pi
        radius = motive.radius() * (random.randint(0, 100) / 100)
        target_delta = pygame.Vector2(
            math.cos(angle) * radius,
            math.sin(angle) * radius
        )
        return motive.location + target_delta