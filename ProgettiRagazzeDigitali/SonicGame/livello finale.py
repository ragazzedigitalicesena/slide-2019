# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 09:17:46 2019

@author: scr.003
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
ADDNEWMARIORATE=50
MARIOMINSIZE=50
MARIOMAXSIZE=150
MARIOMINSPEED=6
MARIOMAXSPEED=10

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

def sonicHasHitMario(sonicRect, marios):
    for b in marios:
        if sonicRect.colliderect(b['rect']):
            return True
    return False

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

# Set up pygame, the window, and the mouse cursor.
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
#pygame.display.set_caption('Dodger')
pygame.mouse.set_visible(False)

# Set up the fonts.
font = pygame.font.SysFont(None, 48)

# Set up sounds.
gameOverSound = pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('stones.mp3')
victorySound = pygame.mixer.Sound('blow.wav')
# Set up images.
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
marioImage = pygame.image.load('mario.png')

windowSurfaceRectangle = windowSurface.get_rect()
windowSurface.fill(BACKGROUNDCOLOR)
drawText ('WORLD TOUR', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3)) 
drawText('Press a key to start.', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3) + 50) 
pygame.display.update()
waitForPlayerToPressKey()

backgroundImage = pygame.image.load('planisfero.jpg')
backgroundStretchedImage = pygame.transform.scale(backgroundImage, (WINDOWWIDTH, WINDOWHEIGHT))
windowSurface.blit(backgroundStretchedImage, windowSurfaceRectangle)
pygame.display.update()
waitForPlayerToPressKey()

backgroundImage5 = pygame.image.load('tokyo.jpg')
backgroundStretchedImage5 = pygame.transform.scale(backgroundImage5, (WINDOWWIDTH, WINDOWHEIGHT))
drawTitles('TOKYO ', font,backgroundStretchedImage5 , (WINDOWWIDTH -300),(WINDOWHEIGHT - 950))
windowSurface.blit(backgroundStretchedImage5, windowSurfaceRectangle)
pygame.display.update()

topScore = 0
while True:
    # Set up the start of the game.
    marios = []
    score = 0
    timer=0
    sonicRect.bottomleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    marioAddCounter = 0
    pygame.mixer.music.play(-1, 0.0)

    while True: # The game loop runs while the game part is playing.
        score += 1
        timer+=1# Increase score.

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                if event.key == K_LEFT or event.key == K_a:
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == K_d:
                    moveLeft = False
                    moveRight = True

            if event.type == KEYUP:
               
                if event.key == K_ESCAPE:
                        terminate()

                if event.key == K_LEFT or event.key == K_a:
                    moveLeft = False
                if event.key == K_RIGHT or event.key == K_d:
                    moveRight = False
               

        marioAddCounter +=1   
        if marioAddCounter == ADDNEWMARIORATE:
            marioAddCounter = 0
            marioSize = random.randint(MARIOMINSIZE, MARIOMAXSIZE)
            newMario = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - marioSize), 0 - marioSize, marioSize, marioSize),
                        'speed': random.randint(MARIOMINSPEED, MARIOMAXSPEED),
                        'surface':pygame.transform.scale(marioImage, (marioSize, marioSize)),
                        }

            marios.append(newMario)

        # Move the player around.
        if moveLeft and sonicRect.left > 0:
            sonicRect.move_ip(-1 * SONICMOVERATE, 0)
        if moveRight and sonicRect.right < WINDOWWIDTH:
            sonicRect.move_ip(SONICMOVERATE, 0)
        

        # Move the baddies down.
        for b in marios:
                b['rect'].move_ip(0, b['speed'])

        # Delete baddies that have fallen past the bottom.
        for b in marios[:]:
            if b['rect'].top > WINDOWHEIGHT:
                marios.remove(b)

        # Draw the game world on the window.
        windowSurface.blit(backgroundStretchedImage5, windowSurfaceRectangle)

       
        

        # Draw the player's rectangle.
        
        windowSurface.blit(sonicImageScaled, sonicRect)

        # Draw each baddie.
        for b in marios:
            windowSurface.blit(b['surface'], b['rect'])

        pygame.display.update()
        
        
        if sonicHasHitMario( sonicRect , marios ):
               
            pygame.mixer.music.stop()
            mainClock.tick(FPS)
            gameOverSound.play()
            
            drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
            drawText('Press a key to play again.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
            pygame.display.update()
            waitForPlayerToPressKey()
            gameOverSound.stop()
           
           
            
            break


        if timer == 500:
            
            pygame.mixer.music.stop()
            mainClock.tick(FPS)
            victorySound.play()
          
            drawText('YOU WIN!!', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
            drawText('Press a key to play again.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
            pygame.display.update()
            waitForPlayerToPressKey()
            victorySound.stop()
           
           
           
            break 
            
            
        pygame.display.update()
        