import random
import pygame

from config.global_config import GLOBALCONFIG
from game_manager import ThePond
from game.logic.motive.Motive import *
from game.logic.motive.PondMotives import PondMotives

pygame.init()
pygame.display.set_caption("The Pond - HackClub Project")

main_surface = pygame.display.set_mode((GLOBALCONFIG.window_width, GLOBALCONFIG.window_height))
running: bool = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            PondMotives.add(Motive(pygame.Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]), random.randint(20, 65)))
    
    main_surface.fill(0)
    
    ThePond.update(pygame.time.get_ticks())
    ThePond.draw(main_surface)
    
    pygame.draw.circle(main_surface, (255, 0, 255), PondMotives.generateTarget(), 5)
    
    pygame.display.update()
    pygame.time.Clock().tick(120)
    
pygame.quit()