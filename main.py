import pygame
import menu
import numpy as np
import time

pygame.init()

screen = pygame.display.set_mode([1200,800]) #16x9

running = True

rectSize = 50
rectSize2 = rectSize/4
screenWidth = screen.get_width()

tela = 0
atuali = 144

playStartPos = []

while running:
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

pygame.quit()
