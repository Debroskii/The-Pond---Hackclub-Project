import pygame
import random
import kinematics.segment as seg
from fish.tail import Tail
import math
from fish.side_fins import SideFins

segmentSizes = [
    [48, 20], 
    [68, 20], 
    [64, 15], 
    [48, 15], 
    [34, 20], 
    [22, 30]
] # Entry format [radius, length]

class KoiFish:
    pos = pygame.Vector2()
    motion = pygame.Vector2(0, 0)
    speed = random.randint(25, 150) / 100
    color = ()
    scale = 1
    segments = []
    side_fins = []
    
    def __init__(self, color, scale):
        self.color = color
        self.scale = scale

        self.pos = pygame.Vector2(random.randint(0, 900), random.randint(0, 900))
        for segmentSizeConfig in segmentSizes:
            self.segments.append(
                seg.Segment(0, 0, 0, segmentSizes, segmentSizes.index(segmentSizeConfig), (255, 252, 237), self.scale)
            )
        self.segments.append(
            Tail(0, 0, 0, self.scale, (255, 102, 31), (255, 252, 237))
        )
        
    def update(self, follow):
        headSegment = self.segments[0]
        previousSegment = headSegment
        headSegment.solve(pygame.Vector2(follow[0], follow[1]))
        for segment in self.segments:
            if segment != headSegment:
                segment.solve(previousSegment.a)
            previousSegment = segment
        
    def draw(self, surface):
        for segment in self.segments:
            if self.segments.index(segment) == 1:
                SideFins.attach(surface, segment, 1, self.color)
            elif self.segments.index(segment) == 4:
                SideFins.attach(surface, segment, 0.6, self.color)
            segment.draw(surface);