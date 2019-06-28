import pygame, random, sys
from pygame.locals import *

WINDOWWIDTH = 900
WINDOWHEIGHT = 900
TEXTCOLOR = (255, 255, 255)
PLAYERWIDTH = 100
PLAYERHEIGHT = 120
SASSIMINSIZE = 70
SASSIMAXSIZE = 90
ADDNEWSASSIRATE = 6

def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # Pressing ESC quit
                    terminate()
                return
            
def playerHasHitRock(playerRect, fish):
    for s in sassi:
        if playerRect.colliderect(f['rect']):
            return True
    return False            
            
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

#pygame.mixer.music.load('chuChu.mp3').


backgroundImage = pygame.image.load('prato.jpg')

playerImage = pygame.image.load('dora.png')
playerStretchedImage = pygame.transform.scale(playerImage, (PLAYERWIDTH, PLAYERHEIGHT))
playerRect = playerStretchedImage.get_rect()
pygame.display.update()
    
sassoDue = pygame.image.load('sassi1.png')

backgroundStretchedImage = pygame.transform.scale(backgroundImage,(WINDOWWIDTH, WINDOWHEIGHT))
drawText('Salta la roccia', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
drawText('premi un tasto per inizare', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3) + 50)
pygame.display.update()

waitForPlayerToPressKey()
windowSurfaceRectangle = windowSurface.get_rect()

topScore = 0
score = 0
win = False

while True:
    sassi = []
    score = 0
    playerRect.topleft = (0, WINDOWHEIGHT - PLAYERHEIGHT)
    moveUp = moveDown = False
    #fishAddCounter = 0
    #pygame.mixer.music.load('babyshark.mp3')
    #pygame.mixer.music.play(-1, 0.0)
    
    while True:
        score += 1 

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                if event.key == K_UP or event.key == K_w:
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == K_s:
                    moveUp = False
                    moveDown = True

            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                        terminate()

                if event.key == K_UP or event.key == K_w:
                    moveUp = False
                if event.key == K_DOWN or event.key == K_s:
                    moveDown = False
                    
        if sassiAddCounter == ADDNEWSASSIRATE:
            sassiAddCounter = 0
            sassiSize = random.randint(SASSIMINSIZE, SASSIMAXSIZE)
            newSassi = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - sassiSize), 0 - sassiSize, sassiSize, sassiSize),
                        'speed': random.randint(FISHMINSPEED, FISHMAXSPEED),
                        'surface':pygame.transform.scale(sassoDue, (sassiSize, sassiSize)),
                        }

            fish.append(newFish)
        
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * PLAYERMOVERATE)
        if moveDown and playerRect.bottom < WINDOWHEIGHT:
            playerRect.move_ip(0, PLAYERMOVERATE)
            
        for f in fish:
            if not reverseCheat and not slowCheat:
                f['rect'].move_ip(- s['speed'], 0)
                
         windowSurface.blit(backgroundStretchedImage, windowSurfaceRectangle)
        windowSurface.blit(playerStretchedImage, playerRect)

        drawText('Score: %s' % (score), font, windowSurface, 10, 0)
        drawText('Top Score: %s' % (topScore), font, windowSurface, 10, 40)
        
        for s in sassi:
            windowSurface.blit(s['surface'], s['rect'])


        if playerHasHitRock(playerRect, sassi):
            if score > topScore:
                topScore = score  
            pygame.mixer.music.stop()
            #pygame.mixer.music.load('gameover.mp3')
            #pygame.mixer.music.play(-1, 0.0)
    
            drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
            drawText('Premi un tasto per', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
            drawText(' giocare di nuovo', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 85)
            pygame.display.update()
            
            waitForPlayerToPressKey()
            pygame.display.update()

            #pygame.mixer.music.stop()
            pygame.display.update()
            break
        
#        if score > 500:
#            pygame.mixer.music.load('applausi.mp3')
#            pygame.mixer.music.play(-1, 0.0)
#            windowSurface.blit(backgroundStretchedImage, windowSurfaceRectangle)
#            windowSurface.blit(playerStretchedImage, playerRect)
#            
#            drawText('Score: %s' % (score), font, windowSurface, 10, 0)
#            drawText('Top Score: %s' % (topScore), font, windowSurface, 10, 40)
#            
#            for f in fish:
#                windowSurface.blit(f['surface'], f['rect'])
#                
#            drawText('HAI VINTO !!', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
#            drawText('Premi un tasto per', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
#            drawText(' uscire ', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 85)
#            pygame.display.update()
#            waitForPlayerToPressKeyExit()
#            pygame.mixer.music.stop()
#            pygame.display.update()
            
        
        pygame.display.update()
        mainClock.tick(FPS)
            















