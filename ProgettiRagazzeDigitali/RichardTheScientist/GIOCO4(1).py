import pygame, sys, random
from pygame.locals import *
import time

def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # Pressing ESC quits.
                    terminate()
                return
def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, WHITE)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)   
    return
def drawText1(text, font, surface, x, y):
    textobj = font.render(text, 1, BLACK)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)   
    return

#FUNZIONI GIOCO 1
def checkTheAnswer():
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
             return str(chr(event.key))
         
pygame.init()
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 1000

WHITE=(255,255,255)
BLACK=(0,0,0)

font= pygame.font.SysFont(None, 48)

mainClock = pygame.time.Clock()
windowSurface=pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('NOME DEL GIOCO')
pygame.mouse.set_visible(True)


sfondoLaboratorio=pygame.image.load('laboratorio.jpg')
windowSurfaceRectangle=windowSurface.get_rect()
waitForPlayerToPressKey()
sfondoLaboratorioStretchedImage=pygame.transform.scale(sfondoLaboratorio, (WINDOW_WIDTH, WINDOW_HEIGHT))
windowSurface.blit(sfondoLaboratorioStretchedImage ,windowSurfaceRectangle )

text1=["Sei arrivato all'ultimo livello ."]
drawText1(text1[0] ,font, windowSurface, 100,200)
pygame.display.update()

score=0
waitForPlayerToPressKey()

while True:    
    for event in pygame.event.get(): 
        if event.type==QUIT:
            terminate()
    
    windowSurface.blit(sfondoLaboratorioStretchedImage, windowSurfaceRectangle)
    pygame.display.update()
    
    drawText('SO3 + H2O --->' ,font, windowSurface, 100,200)


    


