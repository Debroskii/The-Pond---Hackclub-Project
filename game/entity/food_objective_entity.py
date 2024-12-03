import math
import random
import pygame

import game_manager
from game.entity.path_entity import PathMode

class FoodObjectiveEntity:
    def __init__(self, position):
        self.position = position
        self.capacity = random.randint(3, 7)
        self.occupants = 0
        self.food = 500 * self.capacity
        self.radius = self.capacity * 10
        self.feeding_positions = []
        
        dust_positions = []
        for x in range(random.randint(50, 150)):
            dtheta = random.uniform(-math.pi, math.pi)
            dr = random.gauss(0, random.randint(15, 50))
            dust_positions.append([pygame.Vector2(dr * math.cos(dtheta), dr * math.sin(dtheta)), random.uniform(1, 3), random.randint(0, 1)])
        self.feeding_positions.append([0, 0, 0, False, -1, dust_positions])
        
        for i in range(self.capacity - 1):
            theta = (random.randint(0, 200) / 100) * math.pi
            r = (random.randint(45, 100) / 100) * self.radius
            dust_positions = []
            for x in range(random.randint(5, 50)):
                dtheta = random.uniform(-math.pi, math.pi)
                dr = random.uniform(1, 15)
                dust_positions.append([pygame.Vector2(dr * math.cos(dtheta), dr * math.sin(dtheta)), random.uniform(1, 3), random.randint(0, 1)])
            self.feeding_positions.append(
                [theta, r, random.randint(-2, 2) / 500, False, -1, dust_positions] # 0: Angle, 1: radius, 2: speed, 3: Bound, 4: bound_index, 5: dust
            )
            
    def bind(self, position_index, fish_index):
        self.feeding_positions[position_index][3] = True
        self.feeding_positions[position_index][4] = fish_index 
        
    def unbind(self, position_index):
        self.feeding_positions[position_index][3] = False
        game_manager.GameManager.fish[self.feeding_positions[position_index][4]].path_entity.mode = PathMode.WANDER
        self.feeding_positions[position_index][4] = -1 
        
    def loop(self, timestamp, dt):
        self.radius += 0.1 * dt
        
        self.occupants = 0
        for pos in self.feeding_positions:
            if self.feeding_positions.index(pos) != 0:
                pos[1] += (math.cos((timestamp / 500) + self.feeding_positions.index(pos))) * 0.05 * dt
            pos[1] += pos[2] * 5 * dt
            if pos[3]:
                game_manager.GameManager.fish[pos[4]].path_entity.update_bound_target(self.position + pygame.Vector2(pos[1] * math.cos(pos[0]), pos[1] * math.sin(pos[0])))
                self.occupants += 1
            for dust in pos[5]:
                dust[0] *= 1.0002 * dt
                if random.randint(0, int(1000 * (self.food / (500 * self.capacity)))) == 1 and self.occupants != 0:
                    pos[5].remove(dust)
                
        # print(self.food)
        self.food -= self.occupants * dt
        
    def draw(self, surface):
        for pos in self.feeding_positions:
            for dust in pos[5]:
                color = (255, 233, 196)
                if dust[2] == 1:
                    color = (217, 196, 160)
                pygame.draw.circle(
                    surface, 
                    color, 
                    self.position + pygame.Vector2(pos[1] * math.cos(pos[0]), pos[1] * math.sin(pos[0])) + dust[0],
                    dust[1]
                )
        
    def debug_draw(self, surface):
        pygame.draw.circle(surface, (0, 255, 0), self.position, 3)
        pygame.draw.circle(surface, (255, 255, 255), self.position, self.radius, 1)
        
        for pos in self.feeding_positions:
            pygame.draw.circle(surface, (255, 255, 0), self.position + pygame.Vector2(pos[1] * math.cos(pos[0]), pos[1] * math.sin(pos[0])), 3)
            
    def dissolve(self):
        for pos in self.feeding_positions:
            self.unbind(self.feeding_positions.index(pos))
            
    def has_expired(self):
        return self.food <= 0