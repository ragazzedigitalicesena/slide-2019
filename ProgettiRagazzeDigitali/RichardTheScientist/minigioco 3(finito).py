import pygame, random, sys
from pygame.locals import *

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
TEXTCOLOR = (0, 0, 0)
WHITE=(255,255,255)

windowSurface=pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
windowSurfaceRectangle=windowSurface.get_rect()

windowSurface.fill(WHITE)
FPS = 60
SIZE=50
BADDIEMINSPEED = 2
BADDIEMAXSPEED = 5
GOODIEMINSPEED= 2
GOODIEMAXSPEED= 5
ADDNEWBADDIERATE = 18
ADDNEWGOODIERATE= 18
PLAYERMOVERATE = 5
PLAYER_WIDTH=100
PLAYER_HEIGHT=150

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
                return
            
def playerHasHitBaddie(playerRect, baddies):
    for b in baddies:
        if playerRect.colliderect(b['rect']):
            baddies.remove(b)
            return True
    return False

def playerHasHitGoodie(playerRect, goodies):
    for g in goodies:
        if playerRect.colliderect(g['rect']):
            goodies.remove(g)
            return True
    return False
    
def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
    
pygame.init() #DA TOGLIERE DOPO
mainClock = pygame.time.Clock()

pygame.display.set_caption('NOME GIOCO')
pygame.mouse.set_visible(False)

font = pygame.font.SysFont(None, 48) #DA TOGLIERE DOPO


#gameOverSound = pygame.mixer.Sound('gameover.wav')
#pygame.mixer.music.load('background.mid')

sfondoAula=pygame.image.load('sfondo-aula.jpg')
playerImage = pygame.image.load('Scientist-Transparent.png')
baddieImage1 = pygame.image.load('radiation.png')
baddieImage2 = pygame.image.load('simbolo_velenoso.png')
goodieImage1=pygame.image.load('beutapng.png')
goodieImage2=pygame.image.load('provetta-png.png')
goodieImage3=pygame.image.load('termometro.png')

playerRect = playerImage.get_rect() 
baddieImage1Rect=baddieImage1.get_rect()
baddieImage2Rect=baddieImage2.get_rect()
goodieImage1Rect=goodieImage1.get_rect()
goodieImage2Rect=goodieImage2.get_rect()
goodieImage3Rect=goodieImage3.get_rect()

playerStretchedImage=pygame.transform.scale(playerImage,(PLAYER_WIDTH, PLAYER_HEIGHT))
baddieStretchedImage1=pygame.transform.scale(baddieImage1,(SIZE,SIZE))
baddieStretchedImage2=pygame.transform.scale(baddieImage2,(SIZE,SIZE))
goodieStretchedImage1=pygame.transform.scale(goodieImage1,(SIZE,SIZE))
goodieStretchedImage2=pygame.transform.scale(goodieImage2,(SIZE,SIZE))
goodieStretchedImage3=pygame.transform.scale(goodieImage3,(SIZE,SIZE))

playerRect = playerStretchedImage.get_rect()
baddieImage1Rect = baddieStretchedImage1.get_rect()
baddieImage2Rect = baddieStretchedImage2.get_rect()
goodieImage1Rect = goodieStretchedImage1.get_rect()
goodieImage2Rect = goodieStretchedImage2.get_rect()
goodieImage3Rect = goodieStretchedImage3.get_rect()

baddieImage=[baddieImage1, baddieImage2]
goodieImage=[goodieImage1,goodieImage2,goodieImage3]


baddieStretchedImage=[baddieStretchedImage1,baddieStretchedImage2]
goodieStretchedImage=[goodieStretchedImage1,goodieStretchedImage2,goodieStretchedImage3]

baddieImageRect=[baddieImage1Rect,baddieImage2Rect]
goodieImageRect=[goodieImage1Rect,goodieImage2Rect,goodieImage3Rect]




sfondoAulaStretchedImage=pygame.transform.scale(sfondoAula, (WINDOW_WIDTH, WINDOW_HEIGHT))



windowSurface.blit( sfondoAulaStretchedImage ,windowSurfaceRectangle )
drawText('Minigioco 3', font, windowSurface, (WINDOW_WIDTH / 3), (WINDOW_HEIGHT / 3))
drawText('Premi un tasto per iniziare.', font, windowSurface, (WINDOW_WIDTH / 3) - 30, (WINDOW_HEIGHT / 3) + 50)
pygame.display.update()

#topScore = 0
waitForPlayerToPressKey()
  
windowSurface.blit( sfondoAulaStretchedImage ,windowSurfaceRectangle )



while True:
    
    score = 0 #DA TOGLIERE DOPO
    life=3
    baddies = []
    goodies = []
    playerRect.topleft = (550,650)
    moveLeft = moveRight = moveUp = moveDown = False

    baddieAddCounter = 0
    goodieAddCounter= 0
    #pygame.mixer.music.play(-1, 0.0)
    


    while True:
        
        

        windowSurface.blit( sfondoAulaStretchedImage ,windowSurfaceRectangle )
        windowSurface.blit(playerStretchedImage, playerRect)
        
        drawText('Punteggio:  '+str(score), font, windowSurface, 10, 0)
        drawText('Vite:  '+str(life), font, windowSurface, 10, 50)
          
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
                    
        baddieAddCounter +=1    
        if baddieAddCounter == ADDNEWBADDIERATE:
            baddieAddCounter = 0
            randomBaddieImage = baddieImage[random.randint(0,1)]
            newBaddie = {'rect': pygame.Rect(random.randint(0, WINDOW_WIDTH - SIZE), 0 - SIZE, SIZE, SIZE),
                        'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                        'surface':pygame.transform.scale(randomBaddieImage, (SIZE, SIZE))}

            baddies.append(newBaddie)
            
        goodieAddCounter +=1    
        if goodieAddCounter == ADDNEWGOODIERATE:
            goodieAddCounter= 0
            randomGoodieImage = goodieImage[random.randint(0,2)]
            newGoodie= {'rect':pygame.Rect(random.randint(0, WINDOW_WIDTH - SIZE),0 - SIZE, SIZE, SIZE),
                       'speed':random.randint(GOODIEMINSPEED, GOODIEMAXSPEED),
                       'surface':pygame.transform.scale(randomGoodieImage,(SIZE, SIZE))}
            
            goodies.append(newGoodie)
            
            
            
       
      
        if moveLeft and playerRect.left > 0:
           
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
        if moveRight and playerRect.right < 1200:
          
            playerRect.move_ip(PLAYERMOVERATE, 0)
            
        for b in baddies:
                b['rect'].move_ip(0, b['speed'])
                
        for g in goodies:
                g['rect'].move_ip(0, g['speed'])

        
#        pygame.display.update()
         # Draw each baddie.
        for b in baddies:
            windowSurface.blit(b['surface'], b['rect'])
             
        for g in goodies:
            windowSurface.blit(g['surface'], g['rect'])

        pygame.display.update()
         
        if playerHasHitBaddie(playerRect, baddies):  
           print(life)       
           life -=1
           
           if life==0:
               break
        
      
        if playerHasHitGoodie(playerRect, goodies):
            score+=10
            
        
        pygame.display.update()
        mainClock.tick(FPS)

     
#    pygame.mixer.music.stop()
#    gameOverSound.play()

    drawText('GAME OVER', font, windowSurface, (WINDOW_WIDTH / 3), (WINDOW_HEIGHT / 3))
    drawText('Premi un tasto per giocare di nuovo.', font, windowSurface, (WINDOW_WIDTH / 3) - 80, (WINDOW_HEIGHT / 3) + 50)
    pygame.display.update()
#    waitForPlayerToPressKey()

#    gameOverSound.stop()

