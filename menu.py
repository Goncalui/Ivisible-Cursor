import pygame
pygame.init()

prato = pygame.image.load('assets/images/menu.png')
prato = pygame.transform.scale(prato,(prato.get_width()/2,prato.get_height()/2))
font = pygame.font.SysFont('assets/fonts/fontGame.otf', 54)
img = font.render('Play', True, (0,0,255))

def menuPrincipal(screen):
    screen.fill((255,255,255))
    screen.blit(prato,(int(screen.get_width()/2)-prato.get_width()/2,int(screen.get_height()/2)-prato.get_width()/2))
    screen.blit(img,(int(screen.get_width()/2)-img.get_width()/2,int(screen.get_height()/2)-img.get_width()/2))
    return ([int(screen.get_width()/2)-prato.get_width()/2,int(screen.get_width()/2)+prato.get_width()/2],[int(screen.get_height()/2)-prato.get_width()/2,int(screen.get_height()/2)+prato.get_width()/2])





























