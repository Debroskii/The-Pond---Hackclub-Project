import pygame
import random
from fish.face import Face
from lib.pydraw.color.color_config import ColorConfig
import lib.pydraw.kinematics.segment as seg
from fish.tail import Tail
import math
from fish.side_fins import SideFins
from logic.logicpoint import LogicPoint

segmentSizes = [
    [48, 20], 
    [68, 20], 
    [64, 15], 
    [48, 15], 
    [34, 20], 
    [22, 30]
] # Entry format [radius, length]

class KoiFish:    
    def __init__(self, color_config: ColorConfig, scale):
        self.brain = LogicPoint()
        self.pos = pygame.Vector2()
        self.motion = pygame.Vector2(0, 0)
        self.speed = random.randint(25, 150) / 100
        self.color_config = color_config
        self.scale = scale
        self.segments = []
        self.side_fins = []

        self.pos = pygame.Vector2(random.randint(0, 900), random.randint(0, 900))
        for segmentSizeConfig in segmentSizes:
            self.segments.append(
                seg.Segment(0, 0, 0, segmentSizes, segmentSizes.index(segmentSizeConfig), self.color_config.primary_color, self.scale)
            )
        self.segments.append(
            Tail(0, 0, 0, self.scale, self.color_config.tertiary_color, self.color_config.primary_color)
        )
        
    def update(self, frame: int):
        headSegment = self.segments[0]
        self.brain.update(frame, headSegment.angle)
        previousSegment = headSegment
        headSegment.solve(self.brain.pos)
        for segment in self.segments:
            if segment != headSegment:
                segment.solve(previousSegment.a)
            previousSegment = segment
        
    def draw(self, surface):
        for segment in self.segments:
            if self.segments.index(segment) == 0:
                Face.attach(surface, segment, 2 * self.scale, self.color_config.primary_color)
            if self.segments.index(segment) == 1:
                SideFins.attach(surface, segment, 1.8 * self.scale, self.color_config.tertiary_color)
            elif self.segments.index(segment) == 4:
                SideFins.attach(surface, segment, 1 * self.scale, self.color_config.tertiary_color)
            segment.draw(surface);