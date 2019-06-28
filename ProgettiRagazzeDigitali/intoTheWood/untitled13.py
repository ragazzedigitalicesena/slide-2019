import pygame, sys 
from pygame.locals import *
pygame.init()

windowSurface = pygame.display.set_mode ((500 ,400) , 0 , 32)

basicFont = pygame.font.SysFont ('forte' , 48)

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

text = basicFont . render(' Hello world ! ', True ,
WHITE , BLUE )

textRect = text . get_rect ()
textRect . centerx = windowSurface . get_rect () . centerx
textRect . centery = windowSurface . get_rect () . centery

windowSurface . fill ( WHITE )

pygame . draw . polygon ( windowSurface , GREEN , ((146 ,
0) , (291 , 106) ,
(236 , 277) , (56 , 277) , (0 , 106) ) )


pygame . draw . line ( windowSurface , RED , (60 , 60) ,
(420 , 35) , 3)
pygame . draw . line ( windowSurface , RED , (420 , 35) ,
(60 , 200) , 8)

pygame . draw . line ( windowSurface , RED , (60 , 200) ,
(359 , 300) , 1)


pygame . draw . circle ( windowSurface , BLUE , (300 ,
50) , 20 , 0)


pygame . draw . ellipse ( windowSurface , GREEN , (309 ,
262 , 20 , 54) , 9)

pygame . draw . ellipse ( windowSurface , YELLOW , (304 ,
255 , 30 , 67) , 9)

pygame . draw . ellipse ( windowSurface , BLUE , (299 ,
248 , 40 , 80) , 9)


pygame . draw . rect ( windowSurface , YELLOW ,
( textRect . left - 20 ,
textRect . top - 20 , textRect . width + 40 ,
textRect . height + 40) )

windowSurface . blit ( text , textRect )





windowSurface . blit ( text , textRect )

pygame . display . update ()



while True :
    for event in pygame . event . get () :
        if event . type == QUIT :
            pygame . quit ()
            sys . exit ()







