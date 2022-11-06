import pygame
import random


circulo1, circulo2, circulo3 = [None, None, None]

def plotCircle(screen,tamanho):
    h = random.randint(tamanho,screen.get_height() - tamanho)
    w = random.randint(tamanho,screen.get_width() - tamanho)    
    pygame.draw.circle(screen, (255, 255, 255), [w,h] , tamanho)
    pygame.draw.circle(screen, (50, 50, 50), [w,h] , tamanho, 20)
    pygame.draw.circle(screen, (20, 20, 20), [w,h] , tamanho/2, 10)
    pygame.draw.circle(screen, (170, 0, 0), [w,h] , tamanho/10)
    
    return [w,h]

def game(x,y):
    global circulo1, circulo2, circulo3
    if circulo1 == None:
        circulo1 = plotCircle(screen, 130)
    if circulo2 == None:
        circulo2 = plotCircle(screen, 130)
    if circulo3 == None:
        circulo3 = plotCircle(screen, 130)
def checkColision(mouse):
    global circulo1, circulo2, circulo3
    
    if 
    
    
        