
import random, sys, pygame, time
from pygame.locals import *

WINDOWWIDTH = 900
WINDOWHEIGHT = 900
TEXTCOLOR = (0, 0, 0)
BACKGROUNDCOLOR = (100,155,255)


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ALTROAZZURRO = (100,155,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN=(101,67,33)
SABBIA=(218,189,171)

PESCIWINNER = 10

FPS = 60
PESCEMINSIZE = 40
PESCEMAXSIZE = 70
PESCEMINSPEED = 1
PESCEMAXSPEED = 4
ADDNEWPESCERATE = 20
PLAYERMOVERATE = 3 # di quanto si muove il giocatore (tieni un valore basso)

X_POSITION = 400
Y_POSITION = 850
PLAYER_WIDTH = 20
PLAYER_HEIGHT = 20
player = pygame . Rect ( X_POSITION , Y_POSITION , PLAYER_WIDTH , PLAYER_HEIGHT )


SCOREWINNER = 10

def terminate():
    pygame.quit()
    sys.exit()

def aspettaPremaTasto():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # Pressing ESC quits.
                    terminate()
                return
            
def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, ALTROAZZURRO)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)  
    
def pescaPesci(playerRect, pesceLista, pesciScore):
    for b in pesceLista:
        if playerRect.colliderect(b['rect']):
            pesceLista.remove(b)
            pesciScore = pesciScore + 1
    scoreText= 'Score: ' + str(pesciScore)
    drawText(scoreText, font, windowSurface, 10, 0)
    return pesciScore

def colpireOstacolo(playerRect, ostacoli):
    for o in ostacoli: #per ogni roccia dentro la lista
        if playerRect.colliderect(o): 
            return True
    return False



pygame.init()
mainClock = pygame.time.Clock()

windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
backgroundImage = pygame.image.load('fondale.jpg')
backgroundStretchedImage = pygame.transform.scale(backgroundImage,(WINDOWWIDTH, WINDOWHEIGHT))
windowSurfaceRectangle = windowSurface.get_rect()

pygame.display.set_caption('Into the wood')   #titoletto della finestra (in alto)
pygame.mouse.set_visible(False) #prendi ilmouse e quando è sulla finestra nascondilo
font = pygame.font.SysFont(None, 48)
gameOverSound = pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('river.mp3')

playerImage = pygame.image.load('boscaiolo2.png')
playerRect = playerImage.get_rect()
pesceImage = pygame.image.load('pesce.png')
pesceRect = pesceImage.get_rect()

drawText('PESCA 10 PESCI PER LA CENA!', font, windowSurface, 100, 100) 
drawText('FAI ATTENZIONE AGLI OSTACOLI.', font, windowSurface, 100, 150) # vedi funzione sopra (stampa il testo)
drawText('PREMI UN TASTO PER PARTIRE.', font, windowSurface, 155, 700)
drawText('Per muoverti potrai usare le freccette ', font, windowSurface, 132, 350)
drawText('o i seguenti tasti: a per andare a sinistra,', font, windowSurface, 112, 380)
drawText('s per scendere, d per andare a destra, w per salire.', font, windowSurface, 50, 410)

pygame.display.update()

aspettaPremaTasto()


ostacoloA = pygame.draw.rect(windowSurface, BROWN, (40, 327, 114, 50))
ostacoloB = pygame.draw.rect(windowSurface, BROWN, (300, 83, 178, 150))
ostacoloC = pygame.draw.rect(windowSurface, BROWN, (589, 764, 200, 50))

pesciScore = 0
while True:
    # Set up the start of the game.
    ostacoli = [ostacoloA, ostacoloB, ostacoloC]
    pesceLista = []
    
    playerRect.topleft = (WINDOWWIDTH / 2 - 37.5, WINDOWHEIGHT - 85)
    moveLeft = moveRight = moveUp = moveDown = False
    pesciAddCounter = 0
    pygame.mixer.music.play(-1, 0.0)
    
    while True: # The game loop runs while the game part is playing.
         # Increase score
        #pesciAddCounter +=1
        for event in pygame.event.get(): # ogni volta che succede qualcosa 
            if event.type == QUIT: # se clicca la x 
                terminate()

            if event.type == KEYDOWN: #se il giocatore preme un tasto
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

            if event.type == KEYUP: # se il giocatore rilascia un tasto
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
                
        if pesciAddCounter == ADDNEWPESCERATE:
            pesciAddCounter = 0
            pesceSize = random.randint(PESCEMINSIZE, PESCEMAXSIZE)
            newPesce = {'rect': pygame.Rect(0, random.randint(0, WINDOWHEIGHT - pesceSize), pesceSize, pesceSize),
                    'speed': random.randint(PESCEMINSPEED, PESCEMAXSPEED),
                    'surface':pygame.transform.scale(pesceImage, (pesceSize, pesceSize))}
            pesceLista.append(newPesce)

        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
        if moveRight and playerRect.right < WINDOWWIDTH:
            playerRect.move_ip(PLAYERMOVERATE, 0)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * PLAYERMOVERATE)
        if moveDown and playerRect.bottom < WINDOWHEIGHT:
            playerRect.move_ip(0, PLAYERMOVERATE)
            
        
        for b in pesceLista:
            b['rect'].move_ip(b['speed'], 0)
        
        for b in pesceLista:
            if b['rect'].left > WINDOWWIDTH:
                pesceLista.remove(b)
        

        
        windowSurface.blit(backgroundStretchedImage, windowSurfaceRectangle)
        
        ostacoloA = pygame.draw.rect(windowSurface, BROWN, (40, 327, 114, 50))
        ostacoloB = pygame.draw.rect(windowSurface, BROWN, (300, 83, 178, 150))
        ostacoloC = pygame.draw.rect(windowSurface, BROWN, (589, 764, 200, 50))
     
        
        pesciScore = pescaPesci(playerRect, pesceLista, pesciScore)
        
        if pesciScore == PESCIWINNER or colpireOstacolo(playerRect, ostacoli):
            break
        else:
            pesciAddCounter +=1
        
        windowSurface.blit(playerImage, playerRect)
        
        for b in pesceLista:
            windowSurface.blit(b['surface'], b['rect'])
            
        pygame.display.update()
    
        mainClock.tick(FPS)
        
    if colpireOstacolo(playerRect, ostacoli):
            pygame.mixer.music.stop()
            gameOverSound.play()
            drawText('GAME OVER', font, windowSurface, 325
            , (WINDOWHEIGHT / 3))
            drawText('Premi un tasto per rigiocare.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
            pygame.display.update() #aggiorno la schermata 
            aspettaPremaTasto()
    else: 
        break

pygame.mixer.music.stop()
drawText('BRAVO!', font, windowSurface, 350, (WINDOWHEIGHT / 3))
drawText('Hai pescato pesci a sufficienza!', font, windowSurface, 140, (WINDOWHEIGHT / 3) + 50)

pygame.display.update()








