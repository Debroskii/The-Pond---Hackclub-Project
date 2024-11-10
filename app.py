import pygame
import fish.logicpoint as lp
import kinematics.segment as seg

# init
pygame.init()
pygame.display.set_caption("The Pond")

# core
screen = pygame.display.set_mode((900, 900))
clock = pygame.time.Clock()
running = True

sampleSegment = seg.Segment(0, 0, 0, 20)

# loop
while running:
    screen.fill((0, 0, 0))
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            
    sampleSegment.solve(pygame.mouse.get_pos())
    sampleSegment.draw(screen)
    
    pygame.display.update()
  
# final
pygame.quit()