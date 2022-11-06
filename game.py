import pygame
import random

class MouseC:
    def __init__(self,screen,fps=-1,color = (255,0,0), radius = 10):
        self.screen = screen
        self.color = color
        self.radius = radius
        self.counter = fps*2
        self.x = 0
        self.y = 0
    def plotMouseC(self,x,y):
        if(self.counter >0):
            if(self.x == 0):
                self.x = x
                self.y = y
            pygame.draw.circle(self.screen,(255,0,0), [self.x,self.y], 10)  
            self.counter -=1
            print('here',self.counter)
            return 1
        else:
            return 0
    def setTime(self,fps,time = 2):
        if(self.counter == -2):
            self.counter = fps*time
        


class Dish:
    def __init__(self,screen, color = (255,255,255), radius = 200):   
        self.screen = screen
        self.center = [random.randint(radius,screen.get_width() - radius),random.randint(radius,screen.get_height() - radius)]
        self.color = color
        self.radius = radius
        self.MouseC = MouseC(self.screen)
        self.aux = 0
    def plotDish(self, x,y):    
        pygame.draw.circle(self.screen, self.color, [self.center[0], self.center[1]] , self.radius)
        pygame.draw.circle(self.screen, (50, 50, 50), [self.center[0], self.center[1]] , self.radius, int(self.radius/5))
        pygame.draw.circle(self.screen, (80, 80, 80), [self.center[0], self.center[1]] , int(self.radius/2), int(self.radius/10))
        pygame.draw.circle(self.screen, (170, 0, 0), [self.center[0], self.center[1]] , int(self.radius/10))
        cgAux = self.getColision(x,y)
        if(cgAux == 1):
            self.aux = 1
        if(not self.MouseC.plotMouseC(x,y) and self.aux == 1):
            print('here')
            self.MouseC.plotMouseC(x,y)
            self.aux = 0
        return cgAux
        
    def getColision(self, x, y):
        if (x - self.center[0])**2 + (y - self.center[1])**2 <= self.radius**2:
            self.radius -= int(self.radius/20)
            self.center = [random.randint(self.radius,self.screen.get_width() - self.radius),random.randint(self.radius,self.screen.get_height() - self.radius)]
            self.MouseC.setTime(30,2)
            return True
        else:
            return False
  