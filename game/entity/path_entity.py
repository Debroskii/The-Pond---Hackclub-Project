from enum import Enum
import math
import random
import pygame

from config.global_config import GameConfig
import game_manager
from lib.boa.art.draw import draw

class PathMode(Enum):
    WANDER = 0
    GROUP = 1
    EAT = 2
    
class EntityType(Enum):
    INDIVIDUAL = 0
    GROUP = 1

class PathEntity:
    def __init__(self, type: EntityType):
        self.mode: PathMode = PathMode.WANDER
        self.type = type
        self.pos = pygame.Vector2(random.randint(0, GameConfig.window_width), random.randint(0, GameConfig.window_height))
        self.affector_pos = self.pos
        self.target = self.pos + pygame.Vector2(random.randint(-20, 20), random.randint(-20, 20))
        self.heading = 0
        self.seed = random.randint(0, 200) / 100 * math.pi
        self.speed = (2 - (self.seed / math.pi / 2)) * GameConfig.fish_speed
        
    def loop(self, time, path_entity_index, speed_modifier, dt):
        self.heading = math.atan2((self.target - self.pos).y, (self.target - self.pos).x)
        self.pos += pygame.Vector2(
            math.cos(self.heading) * self.speed * speed_modifier * dt, 
            math.sin(self.heading) * self.speed * speed_modifier * dt
        )
        
        self.affector_pos = self.pos + pygame.Vector2(
                (math.cos(self.heading + math.pi / 2) * math.sin(time / 250 + self.seed)) * self.speed / 2 * 7.5 * speed_modifier * dt,
                (math.sin(self.heading + math.pi / 2) * math.sin(time / 250 + self.seed)) * self.speed / 2 * 7.5 * speed_modifier * dt
        )
        
        self.speed += (math.cos((time / 500) + self.seed)) * 0.01 * GameConfig.fish_speed
         
        closest_food_zone = (10000000000, -1)
        closest_food = (10000000000, -1)
                
        if time % 30 and self.type != EntityType.GROUP:
            for food_zone in game_manager.GameManager.food_objectives:
                if (food_zone.position - self.pos).magnitude() < closest_food_zone[0] and food_zone.occupants <= food_zone.capacity: 
                    closest_food_zone = ((food_zone.position - self.pos).magnitude(), game_manager.GameManager.food_objectives.index(food_zone))
            
            if closest_food_zone[1] != -1:
                for pos in game_manager.GameManager.food_objectives[closest_food_zone[1]].feeding_positions:
                    cartesian_pos = game_manager.GameManager.food_objectives[closest_food_zone[1]].position + pygame.Vector2(pos[1] * math.cos(pos[0]), pos[1] * math.sin(pos[0]))
                    if (cartesian_pos - self.pos).magnitude() < closest_food[0] and pos[3] != True:
                        closest_food = (((cartesian_pos - self.pos).magnitude()), game_manager.GameManager.food_objectives[closest_food_zone[1]].feeding_positions.index(pos))
                
                
                if game_manager.GameManager.food_objectives[closest_food_zone[1]].feeding_positions[closest_food[1]][3] == False and self.mode != PathMode.EAT:
                    pos = game_manager.GameManager.food_objectives[closest_food_zone[1]].feeding_positions[closest_food[1]]
                    for group in game_manager.GameManager.groups:
                        for group_pos in group.follower_positions:
                            if group_pos[4] == path_entity_index:
                                group.unbind(group.follower_positions.index(group_pos))
                    food_zone.bind(game_manager.GameManager.food_objectives[closest_food_zone[1]].feeding_positions.index(pos), path_entity_index)
                    self.update_bound_target(game_manager.GameManager.food_objectives[closest_food_zone[1]].position + pygame.Vector2(pos[1] * math.cos(pos[0]), pos[1] * math.sin(pos[0])))
                    self.mode = PathMode.EAT
         
        if self.mode == PathMode.WANDER:
            if random.randint(0, 1000) == 1 and self.type == EntityType.INDIVIDUAL:
                for group in game_manager.GameManager.groups:
                    for pos in group.follower_positions:
                        if pos[3] == False and self.mode == PathMode.WANDER:
                            group.bind(group.follower_positions.index(pos), path_entity_index)
                            self.update_bound_target(group.path_entity.pos + pygame.Vector2(pos[1] * math.cos(pos[0]), pos[1] * math.sin(pos[0])))
                            self.mode = PathMode.GROUP
            
            if (self.target - self.pos).magnitude() <= 2:
                self.heading += random.uniform(-random.uniform(math.pi / 6, math.pi / 4), random.uniform(math.pi / 6, math.pi / 4))
                self.target.update(
                    self.pos.x + math.cos(self.heading) * 150, 
                    self.pos.y + math.sin(self.heading) * 150
                )
                
                if game_manager.GameManager.out_of_logic_bounds(self.pos):
                    self.target.update((pygame.display.get_window_size()[0] / 2) + random.randint(-300, 300), (pygame.display.get_window_size()[1] / 2) + random.randint(-300, 300))
              
    def update_bound_target(self, target):
        if self.mode != PathMode.WANDER:
            self.target = target
    
    def debug_draw(self, surface):
        pygame.draw.circle(surface, (0, 255, 0), self.pos, 3)
        pygame.draw.circle(surface, (255, 0, 255), self.target, 3)
        pygame.draw.line(surface, (155, 155, 155), self.pos, self.target)
        
        # draw.fract_circle(surface, (105, 55, 55), self.pos, 1000, self.heading, math.pi / 1.25, 10)
        
        draw.text(
            surface, 
            pygame.font.SysFont("Cascadia Code PL", 10),
            "Type: " + self.type.name + ", Mode: " + self.mode.name,
            (255, 255, 255),
            self.pos + pygame.Vector2(-20, -20)
        )
        
        draw.text(
            surface, 
            pygame.font.SysFont("Cascadia Code PL", 10),
            "Target",
            (255, 255, 255),
            self.target + pygame.Vector2(-18, -20)
        )
        
    def console_debugging(self):
        target_mode_string = "\tTarget Mode: " + self.mode.name
        target_string = "\tTarget: " + str(self.target)
        position_string = "\tPosition: " + str(self.pos)
        heading_string = "\tHeading (degrees): " + str(round((self.heading / math.pi) * 180, 2))
        speed_string = "\tSpeed: " + str(round(self.speed, 2))
        
        print("<PATH ENTITY>" + target_mode_string + target_string + position_string + heading_string + speed_string)