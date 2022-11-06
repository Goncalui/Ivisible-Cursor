import math
import pygame

pygame.init()

screen = pygame.display.set_mode([1200,800]) #16x9

running = True

rectSize = 50
rectSize2 = rectSize/4
screenWidth = screen.get_width()

tela = 0
atuali = 144

while running:
    atuali+=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            print('clicked')

    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]

    screen.fill((255,255,255))

    pygame.display.flip()

pygame.quit()
