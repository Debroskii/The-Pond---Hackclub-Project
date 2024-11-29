import math
import random
import pygame

from config.global_config import GLOBALCONFIG
from game_manager import GameManager
from lib.boa.art.draw import draw

pygame.init()
pygame.display.set_caption("The Pond - HackClub Project")

main_surface = pygame.display.set_mode((GLOBALCONFIG.window_width, GLOBALCONFIG.window_height))
running: bool = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    main_surface.fill(GLOBALCONFIG.window_color)
        
    GameManager.update(pygame.time.get_ticks())
    GameManager.draw(main_surface)
        
    pygame.display.update()
    pygame.time.Clock().tick(120)
    
pygame.quit()