import math
import random

import pygame
from game.logic.motive.Motive import Motive


class PondMotives:
    motives = [Motive(pygame.Vector2(0, 0), 10)]
    
    def add(motive: Motive):
        PondMotives.motives.append(motive)
        
    def generateTarget():
        if len(PondMotives.motives) == 0:
            return
        motive = random.choice(list(PondMotives.motives))
        angle = (random.randint(0, 200) / 100) * math.pi
        radius = motive.radius * (random.randint(0, 100) / 100)
        target_delta = pygame.Vector2(
            math.cos(angle) * radius,
            math.sin(angle) * radius
        )
        return motive.location + target_delta
    
    def debug_draw(surface):
        for motive in PondMotives.motives:
            pygame.draw.circle(surface, (0, 255, 0), motive.location, 5)
            pygame.draw.circle(surface, (255, 255, 255), motive.location, motive.radius, 1)
            