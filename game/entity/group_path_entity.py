import math
import random

import pygame
from game.entity.path_entity import EntityType, PathEntity, PathMode
import game_manager


class GroupPathEntity:
    def __init__(self):
        self.lifetime = 0
        self.path_entity = PathEntity(EntityType.GROUP)
        self.capacity = random.randint(2, 5)
        self.radius = self.capacity * 15
        self.follower_positions = []
        
        for i in range(self.capacity):
            theta = (random.randint(0, 200) / 100) * math.pi
            r = (random.randint(65, 100) / 100) * self.radius
            self.follower_positions.append(
                [theta, r, random.randint(-2, 2) / 500, False, -1] # 0: Angle, 1: radius, 2: speed, 3: occupied, 4: Bound index
            )
            
    def bind(self, position_index, fish_index):
        self.follower_positions[position_index][3] = True
        self.follower_positions[position_index][4] = fish_index 
        
    def unbind(self, position_index):
        self.follower_positions[position_index][3] = False
        game_manager.GameManager.fish[self.follower_positions[position_index][4]].path_entity.mode = PathMode.WANDER
        self.follower_positions[position_index][4] = -1 
                
    def loop(self, timestamp, dt):
        self.lifetime += 1 * dt
        occupations = ""
        self.path_entity.loop(timestamp, -1, 1, dt)
        for pos in self.follower_positions:
            occupations = occupations + ", Position[" + str(self.follower_positions.index(pos)) + "] Occupied: " + str(pos[3])
            pos[0] += pos[2] * dt
            if random.randint(0, 600) == 1:
                self.unbind(self.follower_positions.index(pos))
            if pos[3]:
                game_manager.GameManager.fish[pos[4]].path_entity.update_bound_target(self.path_entity.pos + pygame.Vector2(pos[1] * math.cos(pos[0]), pos[1] * math.sin(pos[0])))
        
    def draw(self, surface):
        self.path_entity.debug_draw(surface)
        pygame.draw.circle(surface, (255, 255, 255), self.path_entity.pos, self.radius, 1)
        
        pygame.draw.line(surface, (155, 155, 155), self.path_entity.pos, self.path_entity.target)
        
        for pos in self.follower_positions:
            pygame.draw.circle(surface, (255, 255, 0), self.path_entity.pos + pygame.Vector2(pos[1] * math.cos(pos[0]), pos[1] * math.sin(pos[0])), 3)
            
    def dissolve(self):
        for pos in self.follower_positions:
            self.unbind(self.follower_positions.index(pos))
            
    def has_expired(self):
        return False