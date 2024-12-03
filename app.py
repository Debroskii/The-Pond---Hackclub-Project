import math
import random
import pygame

from config.global_config import GameConfig
from game_manager import GameManager
from lib.boa.art.draw import draw
from game.entity.food_objective_entity import FoodObjectiveEntity

pygame.init()
pygame.display.set_caption("The Pond - HackClub Project")

main_surface = pygame.display.set_mode((GameConfig.window_width, GameConfig.window_height), pygame.RESIZABLE)
game_clock = pygame.time.Clock()
dt = 0
running: bool = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            GameManager.food_objectives.append(FoodObjectiveEntity(pygame.mouse.get_pos()))
    
    main_surface.fill(GameConfig.window_color)
        
    GameManager.update(pygame.time.get_ticks(), 1)
    GameManager.draw(main_surface)
        
    pygame.display.update()
    game_clock.tick(60)
    
pygame.quit()