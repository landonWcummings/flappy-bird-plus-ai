import pygame
import random
from .ball import Ball
from .pipe import Pipes
pygame.init()


class GameInformation:
    def __init__(self, score):
        self.score = score


class Game:
    
    SCORE_FONT = pygame.font.SysFont("comicsans", 50)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

    score = 0
    tries = 0

    def __init__(self, window, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.window = window

        self.ball = Ball(self.window_width // 5, self.window_height // 2)
        self.pipes = Pipes(window_width, window_height)
        self.score = 0
        self.tries = 0



    def draw(self):
        self.window.fill(self.RED)

        self.ball.draw(self.window)
        self.pipes.draw(self.window)
        self._draw_score()

    def loop(self):
        self.ball.move()
        self.pipes.move()
        if(self.ball.y >= self.window_height):
            self.reset()
        
        if(self.pipes.collided(self.ball.x, self.ball.y, self.ball.RADIUS)):
            self.reset()
        
        if(self.pipes.scored(self.ball.x)):
            self.score +=1
        

    def _draw_score(self):
        score_text = self.SCORE_FONT.render(
            f"{self.score}", 1, self.BLACK)
        
        self.window.blit(score_text, (self.window_width / 2, 20))

        
        tries_text = self.SCORE_FONT.render(
            f"{self.tries}", 1, self.BLACK)
        
        self.window.blit(tries_text, (20, 20))

    def reset(self):
        self.ball.reset()    
        self.pipes.reset()
        self.score = 0
        self.tries +=1
