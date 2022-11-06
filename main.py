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
fps = 2

clock = pygame.time.Clock()


playStartPos = []

screen.fill((0,0,0))

while running:    
    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]
    
    game.game(screen)
    atuali+=1
    screen.fill((255,255,255))

    if(tela == 0):
        playStartPos = menu.menuPrincipal(screen)
    elif(tela == 1):
        print('options')
    elif(tela == 2):
        #game
        print("on game")
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
                tela = 2
   
   
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
