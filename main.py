import pygame
import game
import menu
import numpy as np
import time

pygame.init()

screen_size = [1200,800] # sempre par
center = [screen_size[0]/2,screen_size[1]/2]
screen = pygame.display.set_mode(screen_size) #16x9

running = True

rectSize = 50
rectSize2 = rectSize/4
screenWidth = screen.get_width()

tela = 0
fps = 144


clock = pygame.time.Clock()



playStartPos = []

screen.fill((0,0,0))# SET_VISIBLE of cursor to False

circle1, circle2, circle3 = [game.Dish(screen), game.Dish(screen), game.Dish(screen)]


while running:    
    x = -1
    y = -1
    
    screen.fill((255,255,255))

    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]          
            mousePos = pygame.mouse.get_pos()
            radius = int((- playStartPos[0][0] + playStartPos[0][1] )/2)
            center =  [playStartPos[0][0]+radius,playStartPos[1][0]+radius]
            if( np.sqrt((mousePos[0]-center[0])**2 +(mousePos[1]-center[1])**2)< radius-7 ):
                tela = 2
                pygame.mouse.set_visible(False)
    
    if(tela == 0):
        playStartPos = menu.menuPrincipal(screen)
    elif(tela == 1):
        #game# SET_VISIBLE of cursor to False
        pygame.mouse.set_visible(False) 
        circle1.plotDish(x,y)
        circle2.plotDish(x,y)
        circle3.plotDish(x,y)
    else:
        print('game over')
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            mousePos = pygame.mouse.get_pos()
            radius = int((- playStartPos[0][0] + playStartPos[0][1] )/2)
            center =  [playStartPos[0][0]+radius,playStartPos[1][0]+radius]
            if( np.sqrt((mousePos[0]-center[0])**2 +(mousePos[1]-center[1])**2)< radius-7 ):
                tela = 1
   


   
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
