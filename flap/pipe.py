import pygame
import math
import random

class Pipe():
    GAP = -1
    WIDTH = -1
    HEIGHT = -1

    def __init__(self, window_width, window_height): 
        self.GAP = window_height / 5 -8
        self.WIDTH = window_width / 15
        self.HEIGHT = window_height / 2

        self.x = window_width 
        self.centery = random.uniform(self.GAP * 1.5 , window_height - self.GAP * 1)


    def draw(self, win) -> None:
        pygame.draw.rect(win, (255, 255, 255), (self.x , 0,                     self.WIDTH, self.centery - self.GAP))
        pygame.draw.rect(win, (255, 255, 255), (self.x , self.centery,          self.WIDTH, self.centery * 3))

        




class Pipes:
    x_vel = -2

    wwidth = -1
    wheight = -1

    ispast = False
    spawnline = -1
    scoreable = True

    storemid = 0

    pipelist: list[Pipe]
    


    def __init__(self, wwidth, wheight):
        self.x = self.original_x = wwidth
        self.pipelist = []
        self.spawnline = (wwidth/3) * 2
        self.wwidth = wwidth
        self.wheight = wheight
        
        self.spawn(wwidth, wheight)


    def draw(self, win):
        
        for pipe in self.pipelist:
            pipe.draw(win)

    def move(self):
        self.ispast = True
        for pipe in self.pipelist:
            if(pipe.x > self.spawnline):
                self.ispast = False
            
            pipe.x += self.x_vel

        
        if(self.ispast):
            self.spawn(self.wwidth, self.wheight)

        self.removeold()
        

    def scored(self, x): 
        if(self.scoreable):
            for pipe in self.pipelist:
                if(x >= pipe.x + pipe.WIDTH):
                    self.scoreable = False
                    return True
        return False

    
    def mid(self, x):
        closest = self.wwidth
        store = None
        for pipe in self.pipelist:
            if(pipe.x + pipe.WIDTH - x > 0 and pipe.x + pipe.WIDTH - x < closest):
                closest = pipe.x + pipe.WIDTH - x
                store = pipe
        if(store != None):
            self.storemid = store.centery
            return store.centery
        else:
            return self.storemid

    def removeold(self):
        for pipe in self.pipelist:
            if(pipe.x <= 0):
                self.pipelist.remove(pipe)
        

    def spawn(self, wwidth, wheight):
        madepipe = Pipe(wwidth, wheight)
        self.pipelist.append(madepipe)
        self.scoreable = True

    def collided(self, x, y, rad):
        for pipe in self.pipelist:
            if(pipe.x <= x  and pipe.x + self.wwidth / 15 >= x ):
                if(y + rad > pipe.centery or y - rad < pipe.centery - pipe.GAP):
                    return True


        return False

    def reset(self):
        
        self.pipelist = []

        

