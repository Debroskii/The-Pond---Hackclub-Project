import pygame
from logic.logicpoint import LogicPoint
from lib.pydraw.color.color_config import ColorConfig
import lib.pydraw.kinematics.segment as seg
import fish.koi as koi

# init
pygame.init()
pygame.display.set_caption("The Pond")

# core
screen = pygame.display.set_mode((900, 900))
clock = pygame.time.Clock()
running = True

testColorConfig = ColorConfig((255, 252, 237), (255, 252, 237), (255, 102, 31))
testKoi = koi.KoiFish(testColorConfig, 0.5)

testLogicPoint = LogicPoint()

# loop
while running:
    screen.fill((62, 149, 237))
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            
    testLogicPoint.update(clock.get_time(), testKoi.segments[0].angle)
    testLogicPoint.draw(screen)        
    
    testKoi.update((testLogicPoint.pos.x, testLogicPoint.pos.y))
    testKoi.draw(screen)
    
    pygame.display.update()
    clock.tick(60)
  
# final
pygame.quit()