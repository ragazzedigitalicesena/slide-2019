import pygame, random, sys, time
from pygame.locals import *


pygame.init()

# window
WINDOWWIDTH = 1600
WINDOWHEIGHT = 900
LIGHTBLUE = (0, 154, 205)
WHITE = (255, 255, 255)



# Set up window
windowSurface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Benvenuti su LE AVVENTURE DI TARTA')

#player
PLAYER_IMAGE = pygame.image.load('tarta.png')

playerRect = pygame.Rect(0, 400, 100,50)
playerStretchedImage = pygame.transform.scale(PLAYER_IMAGE, (100, 50))  

# BACKGROUND
BACKGROUND_IMAGE = pygame.image.load("background.tarta.jpg")
BACKGROUND_IMAGE2 = pygame.image.load("tarta_mare_level_1.jpg")
BACKGROUND_IMAGE3 = pygame.image.load("tarta_campagna_level_2.jpg")
BACKGROUND_IMAGE4 = pygame.image.load("tarta_galassia_level_3.jpg")
windowSurfaceRectangle = windowSurface.get_rect()
backgroundStretchedImage = pygame.transform.scale(BACKGROUND_IMAGE, (WINDOWWIDTH, WINDOWHEIGHT))

# TEXT
basicFont1 = pygame.font.SysFont("timesnewroman", 80)
basicFont2 = pygame.font.SysFont("timesnewroman", 80)
text1 = basicFont1.render('Benvenuti su', True, WHITE)
text2 = basicFont2.render('LE AVVENTURE DI TARTA!', True, WHITE)
textRect1 = text1.get_rect()
textRect1.centerx = windowSurface.get_rect().centerx
textRect1.centery = 300
textRect2 = text2.get_rect()
textRect2.centerx = windowSurface.get_rect().centerx
textRect2.centery = 400

#movement
moveLeft = False
moveRight = False
moveUp = False
moveDown = False
MOVE_SPEED = 6

while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT:
                moveLeft = False
                moveRight = True
            if event.key == K_UP:
                moveDown = False
                moveUp = True
            if event.key == K_DOWN:
                moveUp = False
                moveDown = True
    
    if moveDown and playerRect.bottom < WINDOWHEIGHT:
        playerRect.bottom = playerRect.bottom + MOVE_SPEED
    if moveUp and playerRect.top > 0:
        playerRect.top = playerRect.top - MOVE_SPEED
    if moveLeft and playerRect.left > 0:
       playerRect.left = playerRect.left - MOVE_SPEED 
    if moveRight and playerRect.right < WINDOWWIDTH:
        playerRect.right = playerRect.right + MOVE_SPEED


def terminate():
    pygame.quit()
    sys.exit()
    
    
def waitForPlayerToPressMouseButton():
    while True:
        for evet in pygame.event.get():
            if event.type == QUIT : #x dalla finestra
                terminate()
            if event.type == MOUSEBUTTONDOWN:
                return event.pos
            
#funzione da richiamare per aspettare che l'utente prema un pulsante
def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT: #x dalla finestra 
                terminate()
        if event.type == KEYDOWN:
            if event.type == K_ESCAPE: # tasto esc dalla tastiera
                terminate()
            return # esco dalla funzione  
        
        
windowSurface.blit(backgroundStretchedImage, windowSurfaceRectangle)
windowSurface.blit(text1, textRect1)
windowSurface.blit(text2, textRect2)
pygame.display.update()

waitForPlayerToPressKey()




while True:
    print("Dentro while")
    backgroundStretchedImage2 = pygame.transform.scale(BACKGROUND_IMAGE2, (WINDOWWIDTH, WINDOWHEIGHT))
    windowSurface.blit(backgroundStretchedImage2, windowSurfaceRectangle)
    windowSurface.blit(PLAYER_IMAGE, playerRect)
    pygame.display.update()
    
    
          
        
        
        
        