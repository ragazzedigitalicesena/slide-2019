import random, sys, pygame, time
from pygame.locals import *
pygame.init()
WINDOWWIDTH = 800
WINDOWHEIGHT = 800
FPSLABI = 10
PLAYERMOVERATE = 6
#colori
WHITE = (255,255,255)
RED = (255 , 0 , 0)
GREEN = (100, 225 , 0)
BLUE = (0 , 0 , 255)
BLACK=(0,0,0)

#crea finestra


def terminate():
    pygame.quit()
    sys.exit()
    
def aspettaPremaTasto():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # tasto ESC 
                    terminate()
                return

def drawTextLabi(text, font, surface, x, y):
    textobj = font.render(text, 1, GREEN) #crea il testo
    textrect = textobj.get_rect() #gli dà un rettangolo
    textrect.topleft = (x, y) #lo posiziona
    surface.blit(textobj, textrect) #lo disegna dove gli abbiamo detto
    
def colpireLabirinto(playerRect, linee):
    for l in linee: #per ogni roccia dentro la lista
        if playerRect.colliderect(l): # se l'area che occupa il giocatore è la stessa di un cattivo ..
#        b rect modo per prendere l'area che il cattivo sta usando 
            return True
    return False

def colpireLegna(playerRect, legnaRect):
    if playerRect.colliderect(legnaRect): # tocca la legna
        drawText('Bravo hai raccolto la legna!', font, windowSurface, (WINDOWWIDTH / 3) - 130, (WINDOWHEIGHT / 3) + 80)

fontTitolo = pygame.font.SysFont(None, 80)
font = pygame.font.SysFont(None, 60)
pygame.display.set_caption('boscaui')   #titoletto della finestra (in alto)
pygame.mouse.set_visible(False)

windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
backgroundImage = pygame.image.load('cartoon-background-of-forest-landscape-picture__k41561654.jpg')
backgroundStretchedImage = pygame.transform.scale(backgroundImage,(WINDOWWIDTH, WINDOWHEIGHT))
windowSurfaceRectangle = windowSurface.get_rect()

mainClock = pygame.time.Clock() 


drawText('', fontTitolo, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))  # vedi funzione sopra (stampa il testo)
drawText('Premi un tasto per iniziare', font, windowSurface, (WINDOWWIDTH / 3) - 130, (WINDOWHEIGHT / 3) + 80)

gameOverSound = pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('game of t.mp3') #cambia musicaa  

playerImage = pygame.image.load('BOSCAIOLO FINITO.png')
playerRect = playerImage.get_rect()
legnaImage = pygame.image.load('legna 2.png')
legnaRect = legnaImage.get_rect()
labirintoImage = pygame.image.load('ultimoLabi.png')
labirintoStretchedImage = pygame.transform.scale(labirintoImage,(800, 300))
labirintoRect = labirintoImage.get_rect()

lineQ = pygame.draw.rect(windowSurface ,BLACK ,(30 , 444,  305 ,5))
lineW = pygame.draw.rect(windowSurface ,BLACK ,(34 , 444,  5 ,325))
lineE = pygame.draw.rect(windowSurface ,BLACK ,(30 , 675,  155 ,5))  #3
lineR = pygame.draw.rect(windowSurface ,BLACK ,(34 , 766,  374 ,5))
lineT = pygame.draw.rect(windowSurface ,BLACK ,(327, 675,  78 , 5))
lineY = pygame.draw.rect(windowSurface ,BLACK ,(329, 674,  5 , 92))   #6
lineU = pygame.draw.rect(windowSurface ,BLACK ,(400, 444,  378 ,5))
lineI = pygame.draw.rect(windowSurface ,BLACK ,(774, 443,  5 ,324))
lineO = pygame.draw.rect(windowSurface ,BLACK ,(105, 720,  81 , 5))   #9
lineP = pygame.draw.rect(windowSurface ,BLACK ,(182, 720,  5 , 47))
lineA = pygame.draw.rect(windowSurface, BLACK, (108, 443, 5, 491-442))
lineS = pygame.draw.rect(windowSurface, BLACK, (108, 534, 5, 628-533))   #12
lineD = pygame.draw.rect(windowSurface, BLACK, (105, 629, 334-105, 5))
lineF = pygame.draw.rect(windowSurface, BLACK, (255, 629, 5, 722-628))
lineG = pygame.draw.rect(windowSurface, BLACK, (181, 488, 5, 627-487))   #15
lineH = pygame.draw.rect(windowSurface, BLACK, (179, 488, 477-179, 5))
lineJ = pygame.draw.rect(windowSurface, BLACK, (255, 534, 5, 581-533))
lineK = pygame.draw.rect(windowSurface, BLACK, (255, 580, 334-255, 5))   #18
lineL = pygame.draw.rect(windowSurface, BLACK, (331, 582, 5, 627-581))
lineZ = pygame.draw.rect(windowSurface, BLACK, (327, 534, 408-327, 5))
lineX = pygame.draw.rect(windowSurface, BLACK, (404, 534, 5, 188))   #21
lineC = pygame.draw.rect(windowSurface, BLACK, (478, 443, 5, 95))  
lineV = pygame.draw.rect(windowSurface, BLACK, (478, 673, 5, 48))
lineB = pygame.draw.rect(windowSurface, BLACK, (476, 766, 301, 5))   #24
lineN = pygame.draw.rect(windowSurface, BLACK, (476, 720, 80, 5))
lineM = pygame.draw.rect(windowSurface, BLACK, (552, 720, 5, 47))
lineQQ = pygame.draw.rect(windowSurface, BLACK, (405, 627, 300, 5))   #27
lineWW = pygame.draw.rect(windowSurface, BLACK, (476, 580, 300, 5))
lineEE = pygame.draw.rect(windowSurface, BLACK, (552, 488, 5, 94))
lineRR = pygame.draw.rect(windowSurface, BLACK, (552, 672, 5, 3))   #30
lineTT = pygame.draw.rect(windowSurface, BLACK, (627, 444, 5, 48))
lineYY = pygame.draw.rect(windowSurface, BLACK, (627, 672, 5, 50))
lineUU = pygame.draw.rect(windowSurface, BLACK, (702, 488, 5, 49))   #33
lineII = pygame.draw.rect(windowSurface, BLACK, (701, 672, 5, 50))
lineOO = pygame.draw.rect(windowSurface, BLACK, (553, 534, 150, 5)) 
linePP = pygame.draw.rect(windowSurface, BLACK, (553, 673, 75, 5))   #36
lineAA = pygame.draw.rect(windowSurface ,BLACK ,(702, 673,  74 , 5))

pygame.display.update()

aspettaPremaTasto()


while True:
    linee = [lineQ, lineW, lineE, lineR, lineT, lineY, lineU, lineI, lineO, lineP, lineA, lineS, lineD, lineF, lineG, lineH, lineJ, lineK, lineL, lineZ, lineX, lineC, lineV, lineB, lineN, lineM, lineQQ, lineWW, lineEE, lineRR, lineTT, lineYY, lineUU, lineII, lineOO, linePP, lineAA] #metti tutte le linee
    playerRect.topleft = (WINDOWWIDTH -447, WINDOWHEIGHT - 395)
    legnaRect.topleft = (WINDOWWIDTH -387.5, WINDOWHEIGHT - 38)
    labirintoRect.topleft = (WINDOWWIDTH -770, WINDOWHEIGHT - 358)
    moveLeft = moveRight = moveUp = moveDown = False
    pygame.mixer.music.play(-1, 0.0)
    
    while True: # The game loop runs while the game part is playing.
        
         
#  codice che dice a python cosa fare quando il giocatore preme i tasti 
        for event in pygame.event.get(): # ogni vlta che succede qualcosa 
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
        #fa fermare il giocatore quando arriva al bordo della schermata
        #impostare le linee del labirinto come limite di movimento
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * PLAYERMOVERATELABI, 0)
        if moveRight and playerRect.right < WINDOWWIDTH:
            playerRect.move_ip(PLAYERMOVERATELABI, 0)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * PLAYERMOVERATELABI)
        if moveDown and playerRect.bottom < WINDOWHEIGHT:
            playerRect.move_ip(0, PLAYERMOVERATELABI)
        
        windowSurface.blit(backgroundStretchedImage, windowSurfaceRectangle) 
        
        windowSurface.blit(playerImage, playerRect)
        windowSurface.blit(legnaImage, legnaRect)
        windowSurface.blit(labirintoImage, labirintoRect)
        
        
        if colpireLabirinto(playerRect,linee)or colpireLegna (playerRect,legnaRect):
            break 
        
        pygame.display.update()
        
        mainClock.tick(FPS)
        
    if colpireLabirinto(playerRect,linee):
        pygame.mixer.music.stop()
        gameOverSound.play()
        drawText('GAME OVER', font, windowSurface, 325, (WINDOWHEIGHT/3))
        drawText('Premi un tasto per rigiocare.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
        pygame.display.update()
        aspettaPremaTasto()
    else:
        break

drawText('BRAVO!', font, windowSurface, 350, (WINDOWHEIGHT / 3))
drawText('Hai trovato la legna!', font, windowSurface, 140, (WINDOWHEIGHT / 3) + 50)
pygame.display.update()
        
        
