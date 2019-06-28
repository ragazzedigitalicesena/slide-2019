# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 12:45:50 2019

@author: scr.002
"""

import pygame, random, sys
from pygame.locals import *

WINDOWWIDTH = 1500
WINDOWHEIGHT = 1000
TEXTCOLOR = (255,0,0)
TITLESCOLOR = (0,0,0)
BACKGROUNDCOLOR = (255,193,23)
FPS = 60
OBSTACLESMINSIZE = 100
OBSTACLESMAXSIZE = 300
SONICSIZE = 300
BROWSERSIZE = 80
MARIOSIZE = 50
SONICMOVERATE = 20
BROWSERMOVERATE = 3
OBSTACLESSPEED = 7
OBSTACLESADDRATE = 120
#scorrimento laterale?

def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: 
                    terminate()
                else:
                    return
            
def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect) 

def drawTitles(text, font, surface, x, y):
    textobj = font.render(text, 1, TITLESCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)  

def sonicHasHitObstacle( sonicRect , obstacles ): 
    for b in obstacles:
        if sonicRect.colliderect(b['rect']):
            return True
    return False        
            
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('World Tour')
pygame.mouse.set_visible(False)

font = pygame.font.SysFont(None, 70)
 
gameOverSound = pygame.mixer.Sound('gover.wav')
pygame.mixer.music.load('stones.mp3')
#victorySound = pygame.mixer.Sound('blow.mp3')
 
sonicImage = pygame.image.load('sonic.png')
sonicImageScaled = pygame.transform.scale(sonicImage, (200, 200))
sonicRect = sonicImageScaled.get_rect()
browserImage = pygame.image.load('browser.xcf')
worldImage = pygame.image.load('planisfero.jpg')
milanImage = pygame.image.load('milan.jpg')
londonImage = pygame.image.load('london.jpg')
buenosAiresImage = pygame.image.load('buenos aires.jpg')
newYorkImage = pygame.image.load('NYC.jpg')
tokyoImage = pygame.image.load('tokyo.jpg')
obstaclesImage = pygame.image.load('due_blocchi.png')
moneyImage = pygame.image.load('moneta.xcf')
marioBurntImage = pygame.image.load('mario_infuocato.jpg')

windowSurfaceRectangle = windowSurface.get_rect()
windowSurface.fill(BACKGROUNDCOLOR)
drawText ('WORLD TOUR', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3)) #misure???
drawText('Press a key to start.', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3) + 50) #misure??
pygame.display.update()
waitForPlayerToPressKey()

backgroundImage = pygame.image.load('planisfero.jpg')
backgroundStretchedImage = pygame.transform.scale(backgroundImage, (WINDOWWIDTH, WINDOWHEIGHT))
windowSurface.blit(backgroundStretchedImage, windowSurfaceRectangle)
pygame.display.update()
waitForPlayerToPressKey()

backgroundImage2 = pygame.image.load('milan.jpg')
backgroundStretchedImage2 = pygame.transform.scale(backgroundImage2, (WINDOWWIDTH, WINDOWHEIGHT))
drawTitles('MILAN ', font,backgroundStretchedImage2 , (WINDOWWIDTH -300),(WINDOWHEIGHT - 950))
windowSurface.blit(backgroundStretchedImage2, windowSurfaceRectangle)
pygame.display.update()

topScore = 0
while True:
    obstacles = []
    score = 0
    sonicRect.bottomleft = (50, 1000)
    moveLeft = moveRight = moveUp = moveDown = False
    obstaclesAddCounter = 0
    pygame.mixer.music.play(-1, 0.0)
   
    
    while True: # The game loop runs while the game part is playing.

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                if event.key == K_LEFT or event.key == K_a:
                    moveRight = False
                    moveLeft = False
                if event.key == K_RIGHT or event.key == K_d:
                    moveLeft = False
                    moveRight = False
                if event.key == K_UP or event.key == K_w:
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == K_s:
                    moveUp = False
                    moveDown = False

            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                        terminate()

                if event.key == K_LEFT or event.key == K_a:
                    moveRight =  moveUp = moveLeft = False
                    moveDown = True
                if event.key == K_RIGHT or event.key == K_d:
                    moveRight = moveUp =moveLeft = False
                    moveDown =  True
                if event.key == K_UP or event.key == K_w:
                    moveRight = moveUp = moveLeft =False
                    moveDown = True
                if event.key == K_DOWN or event.key == K_s:
                    moveRight = moveUp =moveLeft = False
                    moveDown =  True
                    
        if moveLeft and sonicRect.left > 0:
            sonicRect.move_ip(-1 * SONICMOVERATE, 0)
        if moveRight and sonicRect.right < WINDOWWIDTH:
            sonicRect.move_ip(SONICMOVERATE, 0)
        if moveUp and sonicRect.top > 0:
            sonicRect.move_ip(0, -1 * SONICMOVERATE)
        if moveDown and sonicRect.bottom < WINDOWHEIGHT:
            sonicRect.move_ip(0, SONICMOVERATE)            

        obstaclesAddCounter +=1
        if obstaclesAddCounter == OBSTACLESADDRATE:
            obstaclesAddCounter = 0
            obstaclesSize = random.randint(OBSTACLESMINSIZE, OBSTACLESMAXSIZE)
            newObstacles = {'rect': pygame.Rect(WINDOWWIDTH, WINDOWHEIGHT - obstaclesSize, obstaclesSize, obstaclesSize),
                        'speed': OBSTACLESSPEED,
                        'surface':pygame.transform.scale(obstaclesImage, (obstaclesSize, obstaclesSize)),
                        }

            obstacles.append(newObstacles)
            
        for b in obstacles:
            b['rect'].move_ip(-1*b['speed'],0)
            
        for b in obstacles[:]:
            if b['rect'].right < 0:
                obstacles.remove(b)
    
        windowSurface.blit(backgroundStretchedImage2, windowSurfaceRectangle)
        windowSurface.blit(sonicImageScaled, sonicRect)
       
        for b in obstacles:
            windowSurface.blit(b['surface'], b['rect'])
        pygame.display.update()
        
      
     
        if sonicHasHitObstacle( sonicRect , obstacles ):
            if score > topScore:
                topScore = score
            break
        mainClock . tick (FPS)
        pygame.display.update()
        
    pygame.mixer.music.stop()
    gameOverSound.play()

    drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
    drawText('Press a key to play again.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
    pygame.display.update()
    waitForPlayerToPressKey()

    gameOverSound.stop()

        
        
        
        
        
        
        
        
        
#backgroundImage3 = pygame.image.load('tokyo.jpg')
#backgroundStretchedImage3 = pygame.transform.scale(backgroundImage3, (WINDOWWIDTH, WINDOWHEIGHT))
#drawTitles('TOKYO ', font,backgroundStretchedImage3 , (WINDOWWIDTH -300),(WINDOWHEIGHT - 950))
#windowSurface.blit(backgroundStretchedImage3, windowSurfaceRectangle)
#pygame.display.update()
#waitForPlayerToPressKey()
        
        




