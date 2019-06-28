import pygame, sys 
from pygame.locals import *
pygame.init()

WINDOWWIDTH =900
WINDOWHEIGHT = 900

windowSurface = pygame.display.set_mode ((900,900) , 0 , 32)
#750 ,328

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255 , 0 , 0)
GREEN = (100, 225 , 0)
BLUE = (0 , 0 , 255)
YELLOW = (225,225,0)
TURCHESE = (0,128,228)
ARANCIO = (255,122,0)
MARRONE = (155,85,0)
CIANO = (0,225.225)
GIALLINO = (255,155,255)
ROSA = (255,155,255)
VERDESCOURO = (10,100,20)
ALTROAZZURRO = (100,155,255)
ROSAPASTELLO = (255,196,208)
BLUPETROLIO = (5,145,180)
VERDEPETROLIO = (0,128,128)
VIOLA = (150,5,175)


backgroundImage = pygame.image.load('fiume.jpg')
backgroundStretchedImage = pygame.transform.scale(backgroundImage,(WINDOWWIDTH, WINDOWHEIGHT))
windowSurfaceRectangle = windowSurface.get_rect()

windowSurface.blit(backgroundStretchedImage, windowSurfaceRectangle)

#immagine labirinto
labirintoImage = pygame.image.load('ultimoLabi.png')
labirintoStretchedImage = pygame.transform.scale(labirintoImage,(800, 300))
labirintoRect = labirintoImage.get_rect()
labirintoRect.topleft = (WINDOWWIDTH -820, WINDOWHEIGHT - 385) 
windowSurface.blit(labirintoImage, labirintoRect)


pygame . draw . line ( windowSurface , BLACK , (80, 517) ,(385, 517) , 5)    # OKK
pygame . draw . line ( windowSurface , BLACK , (84, 517) ,(84 , 842) , 9)    # OKK
pygame . draw . line ( windowSurface , BLACK , (80, 749) ,(235, 749) , 5)    # OKK
pygame . draw . line ( windowSurface , BLACK , (84, 840) ,(458, 840) , 5)    # OKK
pygame . draw . line ( windowSurface , BLACK , (377, 749),(455, 749) , 5)    # OKK
pygame . draw . line ( windowSurface , BLACK , (379, 748),(379, 840) , 9)    # OKK
pygame . draw . line ( windowSurface , BLACK , (450, 517),(828, 517) , 5)    # OKK
pygame . draw . line ( windowSurface , BLACK , (824, 517),(824, 842) , 9)    # OKK
pygame . draw . line ( windowSurface , BLACK , (155, 794),(236, 794) , 5)    # OKK
pygame . draw . line ( windowSurface , BLACK , (231, 794),(231, 841) , 9)    # OKK
pygame . draw . line ( windowSurface , BLACK , (158, 517),(158, 566) , 9)    # OKK
pygame . draw . line ( windowSurface , BLACK , (158, 608),(158, 703) , 9)    # OKK
pygame . draw . line ( windowSurface , BLACK , (155, 701),(384, 701) , 5)    # OKK
pygame . draw . line ( windowSurface , BLACK , (305, 703),(305, 796) , 9)    # OKK
pygame . draw . line ( windowSurface , BLACK , (231, 562),(231, 702) , 9)    # OKK
pygame . draw . line ( windowSurface , BLACK , (229, 562),(527, 562) , 5)    # OKK
pygame . draw . line ( windowSurface , BLACK , (305, 608),(305, 656) , 9)    # OKK
pygame . draw . line ( windowSurface , BLACK , (305, 654),(384, 654) , 5)    # OKK
pygame . draw . line ( windowSurface , BLACK , (381, 656),(381, 702) , 9)    # OKK
pygame . draw . line ( windowSurface , BLACK , (377, 608),(458, 608) , 5)    # OKK
pygame . draw . line ( windowSurface , BLACK , (454, 608),(454, 796) , 9)    # OKK
pygame . draw . line ( windowSurface , BLACK , (528, 517),(528, 612) , 9)    # OKK
pygame . draw . line ( windowSurface , BLACK , (528, 747),(528, 795) , 9)    # OKK
pygame . draw . line ( windowSurface , BLACK , (526, 840),(827, 840) , 5)    # OKK
pygame . draw . line ( windowSurface , BLACK , (526, 794),(606, 794) , 5)    # OKK
pygame . draw . line ( windowSurface , BLACK , (602, 794),(602, 841) , 9)    # OKK
pygame . draw . line ( windowSurface , BLACK , (455, 701),(755, 701) , 5)    # OKK 
pygame . draw . line ( windowSurface , BLACK , (526, 654),(826, 654) , 5)    # OKK 
pygame . draw . line ( windowSurface , BLACK , (602, 562),(602, 656) , 9)    # OKK 
pygame . draw . line ( windowSurface , BLACK , (602, 702),(602, 749) , 9)    # OKK
pygame . draw . line ( windowSurface , BLACK , (677, 518),(677, 566) , 9)    # OKK
pygame . draw . line ( windowSurface , BLACK , (677, 746),(677, 796) , 9)    # OKK
pygame . draw . line ( windowSurface , BLACK , (752, 562),(752, 611) , 9)    # OKK
pygame . draw . line ( windowSurface , BLACK , (751, 746),(751, 796) , 9)    # OKK
pygame . draw . line ( windowSurface , BLACK , (603, 608),(753, 608) , 5)    # OKK
pygame . draw . line ( windowSurface , BLACK , (603, 747),(679, 747) , 5)    # OKK
pygame . draw . line ( windowSurface , BLACK , (752, 747),(826, 747) , 5)    # OKK

pygame.display.update()


































