import pygame, random, sys
from pygame.locals import *

WINDOWWIDTH = 800
WINDOWHEIGHT = 800
TEXTCOLOR = (255, 255, 255)
FPS = 50
FISHMINSIZE = 40
FISHMAXSIZE = 80
FISHMINSPEED = 1
FISHMAXSPEED = 8
ADDNEWFISHRATE = 10
PLAYERMOVERATE = 5
PLAYERWIDTH = 60
PLAYERHEIGHT = 80

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

def playerHasHitFish(playerRect, fish):
    for f in fish:
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
pygame.display.set_caption('Schiva i pesci')
pygame.mouse.set_visible(False)

font = pygame.font.SysFont(None, 60)

pygame.mixer.music.load('babyshark.mp3')


backgroundImage = pygame.image.load('mare.jpg')
playerImage = pygame.image.load('tipo2.png')
playerStretchedImage = pygame.transform.scale(playerImage, (PLAYERWIDTH, PLAYERHEIGHT))
playerRect = playerStretchedImage.get_rect()
fishImage = pygame.image.load('PESCI4.png')

backgroundStretchedImage = pygame.transform.scale(backgroundImage,(WINDOWWIDTH, WINDOWHEIGHT))
drawText('Schiva i pesci', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
drawText('premi un tasto per inizare', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3) + 50)
pygame.display.update()
waitForPlayerToPressKey()


windowSurfaceRectangle = windowSurface.get_rect()

topScore = 0
score = 0
win = False

while True:
    
    fish = []
    score = 0
    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False
    fishAddCounter = 0
    pygame.mixer.music.load('babyshark.mp3')
    pygame.mixer.music.play(-1, 0.0)
    
    while True:
        score += 1 

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                if event.key == K_z:
                    reverseCheat = True
                if event.key == K_x:
                    slowCheat = True
                if event.key == K_LEFT or event.key == K_a:
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == K_d:
                    moveLeft = False
                    moveRight = True
                if event.key == K_UP or event.key == K_w:
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == K_s:
                    moveUp = False
                    moveDown = True

            if event.type == KEYUP:
                if event.key == K_z:
                    reverseCheat = False
                    score = 0
                if event.key == K_x:
                    slowCheat = False
                    score = 0
                if event.key == K_ESCAPE:
                        terminate()

                if event.key == K_LEFT or event.key == K_a:
                    moveLeft = False
                if event.key == K_RIGHT or event.key == K_d:
                    moveRight = False
                if event.key == K_UP or event.key == K_w:
                    moveUp = False
                if event.key == K_DOWN or event.key == K_s:
                    moveDown = False
            
            if event.type == MOUSEMOTION:
                playerRect.centerx = event.pos[0]
                playerRect.centery = event.pos[1]
        if not reverseCheat and not slowCheat:
            fishAddCounter += 1
        if fishAddCounter == ADDNEWFISHRATE:
            fishAddCounter = 0
            fishSize = random.randint(FISHMINSIZE, FISHMAXSIZE)
            newFish = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - fishSize), 0 - fishSize, fishSize, fishSize),
                        'speed': random.randint(FISHMINSPEED, FISHMAXSPEED),
                        'surface':pygame.transform.scale(fishImage, (fishSize, fishSize)),
                        }

            fish.append(newFish)
        
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
        if moveRight and playerRect.right < WINDOWWIDTH:
            playerRect.move_ip(PLAYERMOVERATE, 0)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * PLAYERMOVERATE)
        if moveDown and playerRect.bottom < WINDOWHEIGHT:
            playerRect.move_ip(0, PLAYERMOVERATE)

        for f in fish:
            if not reverseCheat and not slowCheat:
                f['rect'].move_ip(0, f['speed'])
            elif reverseCheat:
                f['rect'].move_ip(0, -5)
            elif slowCheat:
                f['rect'].move_ip(0, 1)

        for f in fish[:]:
            if f['rect'].top > WINDOWHEIGHT:
                fish.remove(f)
        
        
        windowSurface.blit(backgroundStretchedImage, windowSurfaceRectangle)
        windowSurface.blit(playerStretchedImage, playerRect)

        drawText('Score: %s' % (score), font, windowSurface, 10, 0)
        drawText('Top Score: %s' % (topScore), font, windowSurface, 10, 40)
        
        for f in fish:
            windowSurface.blit(f['surface'], f['rect'])


        if playerHasHitFish(playerRect, fish):
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
            pygame.display.update()

            pygame.mixer.music.stop()
            pygame.display.update()
            break
        
        if score > 500:
            pygame.mixer.music.load('applausi.mp3')
            pygame.mixer.music.play(-1, 0.0)
            windowSurface.blit(backgroundStretchedImage, windowSurfaceRectangle)
            windowSurface.blit(playerStretchedImage, playerRect)
            
            drawText('Score: %s' % (score), font, windowSurface, 10, 0)
            drawText('Top Score: %s' % (topScore), font, windowSurface, 10, 40)
            
            for f in fish:
                windowSurface.blit(f['surface'], f['rect'])
                
            drawText('HAI VINTO !!', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
            drawText('Premi un tasto per', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
            drawText(' uscire ', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 85)
            pygame.display.update()
            waitForPlayerToPressKeyExit()
            pygame.mixer.music.stop()
            pygame.display.update()
            
        
        pygame.display.update()
        mainClock.tick(FPS)
        
    #appena esco ho vinto
#    print(score)
#   
#    

            
        
        
    
            

    
    
    

    

       
    

    

























