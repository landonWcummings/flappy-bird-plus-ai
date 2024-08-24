import pygame
import math
import random


class Ball:
    MAX_VEL = 5
    RADIUS = 7

    def __init__(self, x, y):
        self.x = self.original_x = x
        self.y = self.original_y = y
        
        self.y_vel = -5


    def draw(self, win):
        pygame.draw.circle(win, (255, 255, 255), (self.x, self.y), self.RADIUS)

    def move(self):
        self.y += self.y_vel

        if(self.y <= 0):
            self.y_vel = 1
            self.y = self.RADIUS

        if(self.y_vel < 8):
            self.y_vel += 0.4
    
    def flap(self):
        self.y_vel = -7

    def reset(self):
        
        self.y = self.original_y

        

