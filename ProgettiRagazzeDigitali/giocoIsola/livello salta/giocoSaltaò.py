import pygame, random, sys
from pygame.locals import *

WINDOWWIDTH = 800
WINDOWHEIGHT = 800
TEXTCOLOR = (0, 0, 0)
FPS = 50
ROCKSIZE = 120
ROCKSPEED = 8
ADDNEWROCKRATE = 90
PLAYERMOVERATE = 8
PLAYERWIDTH = 110
PLAYERHEIGHT = 130
ADDNEWFLOWERRATE = 120
FLOWERSIZE = 60
BACKGROUNDCOLOR = (0,255,255)

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
            
def waitForPlayerToPressKeyExit():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                terminate()
                return

def playerHasHitRock(playerRect, rock):
    for r in rock:
        if playerRect.colliderect(r['rect']):
            return True
    return False

def playerHasHitFlower(playerRect, flower):
    for f in flower:
        if playerRect.colliderect(f['rect']):
            flower.remove(f)
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
pygame.display.set_caption('Salta la roccia')
pygame.mouse.set_visible(False)

font = pygame.font.SysFont(None, 60)

pygame.mixer.music.load('chuChu.mp3')

windowSurface.fill(BACKGROUNDCOLOR)

backgroundImage = pygame.image.load('VULCANO.jpg')
playerImage = pygame.image.load('dora.png')
playerStretchedImage = pygame.transform.scale(playerImage, (PLAYERWIDTH, PLAYERHEIGHT))
playerRect = playerStretchedImage.get_rect()
rockImage = pygame.image.load('indg.png')

flowerImage = pygame.image.load('fiore.png')

backgroundStretchedImage = pygame.transform.scale(backgroundImage,(WINDOWWIDTH, WINDOWHEIGHT))
drawText('Livello 1', font, windowSurface, 300, 150)
drawText('Per superare questo livello', font, windowSurface,110, 230)
drawText('prendi 10 fiori ma attento agli indigeni.', font, windowSurface, 20,290)
drawText('Premi un tasto per continuare.', font, windowSurface,120 , 400)
pygame.display.update()
waitForPlayerToPressKey()


windowSurfaceRectangle = windowSurface.get_rect()

topScore = 0
score = 0
topFiori = 0
win = False

while True:
    
    rock = []
    flower = []
    totFlower = 0
    playerRect.topleft = (0, WINDOWHEIGHT - PLAYERHEIGHT)
    moveUp = moveDown = False
    rockAddCounter = 0
    flowerAddCounter = 0
    pygame.mixer.music.load('chuChu.mp3')
    pygame.mixer.music.play(-1, 0.0)
    
    while True:
        

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
                    moveDown = True

            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                        terminate()

                if event.key == K_LEFT or event.key == K_a:
                    moveLeft = False
                if event.key == K_RIGHT or event.key == K_d:
                    moveRight = False
                if event.key == K_UP or event.key == K_w:
                    moveUp = False
                    moveDown = True
                if event.key == K_DOWN or event.key == K_s:
                    moveDown = False
            
        
        flowerAddCounter += 1
        if flowerAddCounter == ADDNEWFLOWERRATE:
            flowerAddCounter = 0
            flowerSize = (FLOWERSIZE, FLOWERSIZE)
            newFlower = {'rect': pygame.Rect(WINDOWWIDTH, random.randint(0, WINDOWHEIGHT - FLOWERSIZE), FLOWERSIZE, FLOWERSIZE),
                        'speed': ROCKSPEED,
                        'surface':pygame.transform.scale(flowerImage, (FLOWERSIZE, FLOWERSIZE)),
                        }

            flower.append(newFlower)
            
        for f in flower:
            f['rect'].move_ip(-1*f['speed'],0)        
                
        for f in flower[:]:
            if f['rect'].right < 0:
                flower.remove(f)
            
        rockAddCounter +=1
        if rockAddCounter == ADDNEWROCKRATE:
            rockAddCounter = 0
            rockSize = (ROCKSIZE, ROCKSIZE)
            newRock = {'rect': pygame.Rect(WINDOWWIDTH, random.randint(0, WINDOWHEIGHT - ROCKSIZE), ROCKSIZE, ROCKSIZE),
                        'speed': ROCKSPEED,
                        'surface':pygame.transform.scale(rockImage, (ROCKSIZE, ROCKSIZE)),
                        }

            rock.append(newRock)

        for r in rock:
            r['rect'].move_ip(-1*r['speed'],0)
            
        for r in rock[:]:
            if r['rect'].right < 0:
                rock.remove(r)
                
        
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * PLAYERMOVERATE)
        if moveDown and playerRect.bottom < WINDOWHEIGHT:
            playerRect.move_ip(0, PLAYERMOVERATE)
        
        #sfondo
        windowSurface.blit(backgroundStretchedImage, windowSurfaceRectangle)
        #giocatore
        windowSurface.blit(playerStretchedImage, playerRect)
        

        drawText('Score: %s' % (totFlower), font, windowSurface, 10, 0)
        drawText('Top Score: %s' % (topFiori), font, windowSurface, 10, 40)
        
        for r in rock:
            windowSurface.blit(r['surface'], r['rect'])
            
        for f in flower:
            windowSurface.blit(f['surface'], f['rect'])
            
        pygame.display.update()    


        if playerHasHitRock(playerRect, rock):
            if score > topScore:
                topScore = score  
            pygame.mixer.music.stop()
            pygame.mixer.music.load('gameover.mp3')
            pygame.mixer.music.play(-1, 0.0)
    
            drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
            drawText('Premi un tasto per', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
            drawText(' giocare di nuovo', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 85)
            pygame.display.update()
            
            waitForPlayerToPressKey()

            pygame.mixer.music.stop()
            break
            
        
        if playerHasHitFlower(playerRect, flower):
            totFlower = totFlower + 1
            if totFlower > topFiori:
                topFiori = totFlower
        
        
        if topFiori > 9:
            pygame.mixer.music.load('applausi.mp3')
            pygame.mixer.music.play(-1, 0.0)
            windowSurface.blit(backgroundStretchedImage, windowSurfaceRectangle)
            windowSurface.blit(playerStretchedImage, playerRect)
                
            drawText('HAI SUPERATO IL LIVELLO !', font, windowSurface, (WINDOWWIDTH / 5), (WINDOWHEIGHT / 3))
            drawText('Premi un tasto per', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
            drawText(' uscire ', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 85)
            pygame.display.update()
            waitForPlayerToPressKeyExit()
            pygame.mixer.music.stop()
            break
            
        
        pygame.display.update()
        mainClock.tick(FPS)
        
    #appena esco ho vinto
#    print(score)

