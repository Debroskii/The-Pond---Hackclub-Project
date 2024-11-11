import pygame
from fish.engine import KoiEngine
from game_config import GAMECONFIG
from logic.logicpoint import LogicPoint
from lib.pydraw.color.color_config import ColorConfig
import lib.pydraw.kinematics.segment as seg
import fish.koi as koi

# init
pygame.init()
pygame.display.set_caption("The Pond")

# core
screen = pygame.display.set_mode((GAMECONFIG.width, GAMECONFIG.height))
clock = pygame.time.Clock()
running = True

fishEngine = KoiEngine(10)

# loop
while running:
    screen.fill(GAMECONFIG.background_color)
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False   
    
    fishEngine.loop(pygame.time.get_ticks() / 1000, screen)
    
    pygame.display.update()
    clock.tick(GAMECONFIG.frame_rate)
  
# final
pygame.quit()