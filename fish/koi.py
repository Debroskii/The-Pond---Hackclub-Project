import pygame
import random
import kinematics.segment as seg

segmentSizes = [
    [52, 15*2], 
    [84, 20*2], 
    [64, 15], 
    [46, 15], 
    [22, 20], 
    [22, 30]
] # Entry format [radius, length]

class KoiFish:
    pos = pygame.Vector2()
    motion = pygame.Vector2(0, 0)
    speed = random.randint(25, 150) / 100
    color = ()
    scale = 1
    segments = []
    
    def __init__(self, color, scale):
        self.color = color
        self.scale = scale

        self.pos = pygame.Vector2(random.randint(0, 900), random.randint(0, 900))
        for segmentSizeConfig in segmentSizes:
            self.segments.append(
                seg.Segment(0, 0, 0, segmentSizes, segmentSizes.index(segmentSizeConfig))
            )
        
    def update(self, follow):
        headSegment = self.segments[0]
        previousSegment = headSegment
        headSegment.solve(pygame.Vector2(follow[0], follow[1]))
        for segment in self.segments:
            if segment != headSegment:
                segment.solve(previousSegment.a);
            previousSegment = segment
        
    def draw(self, surface):
        for segment in self.segments:
            segment.draw(surface);