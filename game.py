import pygame
import random


class Dish:
    def __init__(self,screen, color = (255,255,255), radius = 200):   
        self.screen = screen
        self.center = [random.randint(radius,screen.get_width() - radius),random.randint(radius,screen.get_height() - radius)]
        self.color = color
        self.radius = radius
    def plotDish(self, x,y):
        pygame.draw.circle(self.screen, self.color, [self.center[0], self.center[1]] , self.radius)
        pygame.draw.circle(self.screen, (50, 50, 50), [self.center[0], self.center[1]] , self.radius, int(self.radius/5))
        pygame.draw.circle(self.screen, (80, 80, 80), [self.center[0], self.center[1]] , int(self.radius/2), int(self.radius/10))
        pygame.draw.circle(self.screen, (170, 0, 0), [self.center[0], self.center[1]] , int(self.radius/10))
        self.getColision(x,y)
        
    def getColision(self, x, y):
        if (x - self.center[0])**2 + (y - self.center[1])**2 <= self.radius**2:
            self.radius -= int(self.radius/20)
            self.center = [random.randint(self.radius,self.screen.get_width() - self.radius),random.randint(self.radius,self.screen.get_height() - self.radius)]
            pygame.draw.circle(self.screen,(255,0,0), [x,y], 10)  
            return True
        else:
            return False  
        
    
        