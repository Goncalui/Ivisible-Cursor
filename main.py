import math
import pygame
import game


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


screen.fill((0,0,0))
while running:
    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]
    
    game.game(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            print('click')
            
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
