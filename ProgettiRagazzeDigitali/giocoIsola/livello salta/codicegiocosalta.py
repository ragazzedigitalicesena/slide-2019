import pygame, random, sys
from pygame.locals import *

WINDOWWIDTH = 900
WINDOWHEIGHT = 900
TEXTCOLOR = (255, 255, 255)
PLAYERWIDTH = 100
PLAYERHEIGHT = 120
SASSIWIDTH = 80
SASSIHEIGHT = 90

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # Pressing ESC quit
                    terminate()
                return
            
def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
            
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('     Salta la roccia')
pygame.mouse.set_visible(False)

font = pygame.font.SysFont(None, 60)

#pygame.mixer.music.load('babyshark.mp3')


backgroundImage = pygame.image.load('prato.jpg')

playerImage = pygame.image.load('dora.png')
playerStretchedImage = pygame.transform.scale(playerImage, (PLAYERWIDTH, PLAYERHEIGHT))
playerRect = playerStretchedImage.get_rect()
    
sassoUno = pygame.image.load('sassi.png')
sassoDue = pygame.image.load('sassi1.png')

backgroundStretchedImage = pygame.transform.scale(backgroundImage,(WINDOWWIDTH, WINDOWHEIGHT))
drawText('Salta la roccia', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
drawText('premi un tasto per inizare', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3) + 50)
pygame.display.update()

waitForPlayerToPressKey()


windowSurfaceRectangle = windowSurface.get_rect()