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

pygame.font.init()
comicSans = pygame.font.SysFont('Comic Sans MS', 30)

points = game.Points()


playStartPos = []

circle1, circle2, circle3 = [game.Dish(screen), game.Dish(screen), game.Dish(screen)]

counter = 0
while running: 
    x = -1
    y = -1

    screen.fill((255,255,255))
    
    screen.blit(comicSans.render("Pontuação: " + str(points.value), False, (0, 0, 0)), (5,5))

    
    
    mousePos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]          
            radius = int((- playStartPos[0][0] + playStartPos[0][1] )/2)
            center =  [playStartPos[0][0]+radius,playStartPos[1][0]+radius]
            if tela == 0:
                pygame.mouse.set_visible(True)
                if( np.sqrt((mousePos[0]-center[0])**2 +(mousePos[1]-center[1])**2)< radius-7 ):
                    tela = 2
                    points.Clear()
                    circle1.gameOver()
                    circle2.gameOver()
                    circle3.gameOver()
                    counter = 0
                    print('click')
                    
            elif tela == 2:
                    
                if circle1.getColision(x,y) or circle2.getColision(x,y) or circle3.getColision(x,y):
                    points.Add()
                else:
                    tela = 0
    
    if(tela == 0):
        playStartPos = menu.menuPrincipal(screen)
    elif(tela == 1):
        print('options')
    elif(tela == 2):
        #game
        counter += 1
        circle1.plotDish(x,y)
        circle2.plotDish(x,y)
        circle3.plotDish(x,y)
        
        sec = counter/fps
        if sec <= 1:
            screen.blit(comicSans.render("3", False, (255, 0, 0)), [mousePos[0] - 3, mousePos[1] + 10 ])
        elif sec <= 2:
            screen.blit(comicSans.render("2", False, (255, 0, 0)), [mousePos[0] - 3, mousePos[1] + 10 ])
        elif sec <= 3:
            screen.blit(comicSans.render("1", False, (255, 0, 0)), [mousePos[0] - 3, mousePos[1] + 10 ])
        elif sec >= 3:
                    pygame.mouse.set_visible(False)
        if sec >=3 and sec <= 5:
            screen.blit(comicSans.render("Invisivel", False, (255, 0, 0)), [mousePos[0] - 50, mousePos[1] + 10 ])
        
    else:
        tela = 1
        


    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
