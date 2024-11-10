import pygame
import fish.logicpoint as lp
import kinematics.segment as seg
import fish.koi as koi

# init
pygame.init()
pygame.display.set_caption("The Pond")

# core
screen = pygame.display.set_mode((900, 900))
clock = pygame.time.Clock()
running = True

testKoi = koi.KoiFish((255, 255, 255), 1)

# loop
while running:
    screen.fill((0, 0, 0))
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            
    testKoi.update(pygame.mouse.get_pos())
    testKoi.draw(screen)
    
    pygame.display.update()
    clock.tick(60)
  
# final
pygame.quit()