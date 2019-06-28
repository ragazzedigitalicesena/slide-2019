import pygame, sys, random, time
from pygame.locals import *
pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255 , 0 , 0)
GREEN = (140, 235 , 97)
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

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 900
windowSurface = pygame . display . set_mode (( WINDOW_WIDTH , WINDOW_HEIGHT ) , 0 , 32)


windowSurface.fill(GREEN)

#INTRO

basicFont = pygame.font.SysFont (None , 100)
text = basicFont.render('Into the woods', True, BLACK)
textRect = text.get_rect ()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

windowSurface . blit ( text , textRect )

pygame . display . update ()

time.sleep(5)

backgroundImage = pygame.image.load('sfondo montagna.jpeg')
backgroundStretchedImage = pygame.transform.scale(backgroundImage,(WINDOW_WIDTH, WINDOW_HEIGHT))
windowSurfaceRectangle = windowSurface.get_rect()

windowSurface.blit(backgroundStretchedImage, windowSurfaceRectangle)

playerImage = pygame.image.load('boscaiolo2.png')
playerRect = playerImage.get_rect()
windowSurface.blit(playerImage, playerRect)

pygame . display . update ()

while True :
    for event in pygame . event . get () :
        if event . type == QUIT :
            pygame . quit ()
            sys . exit ()

