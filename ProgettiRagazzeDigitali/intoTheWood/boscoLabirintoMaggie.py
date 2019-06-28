import random, sys, pygame, time
from pygame.locals import *
pygame.init()
WINDOWWIDTH = 800
WINDOWHEIGHT = 800
FPS = 10
PLAYERMOVERATE = 2
#colori
WHITE = (255,255,255)
RED = (255 , 0 , 0)
GREEN = (100, 225 , 0)
BLUE = (0 , 0 , 255)
BLACK=(0,0,0)

#crea finestra
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
windowSurfaceRectangle = windowSurface.get_rect()

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

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, BLACK) #crea il testo
    textrect = textobj.get_rect() #gli dà un rettangolo
    textrect.topleft = (x, y) #lo posiziona
    surface.blit(textobj, textrect) #lo disegna dove gli abbiamo detto
    
def colpireLabirinto(playerRect, linee):
    for l in linee: 
        if playerRect.colliderect(l):
            return True
    return False

def colpireLegna(playerRect, legnaRect):
    if playerRect.colliderect(legnaRect): # tocca la legna
        drawText('Bravo hai raccolto la legna!', font, windowSurface, (WINDOWWIDTH / 3) - 50, (WINDOWHEIGHT / 3) + 80)

#font
fontTitolo = pygame.font.SysFont(None, 80)
font = pygame.font.SysFont(None, 60)
pygame.display.set_caption('boscaui')   #titoletto della finestra (in alto)
pygame.mouse.set_visible(False) #prendi ilmouse e quando è sulla finestra nascondilo

#schermata iniziale
windowSurface.fill(GREEN)
drawText('Labirinto', fontTitolo, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))  # vedi funzione sopra (stampa il testo)
drawText('Premi un tasto per iniziare', font, windowSurface, (WINDOWWIDTH / 3) - 50, (WINDOWHEIGHT / 3) + 80)
pygame.display.update()

aspettaPremaTasto()

backgroundImage = pygame.image.load('cartoon-background-of-forest-landscape-picture__k41561654.jpg')
backgroundStretchedImage = pygame.transform.scale(backgroundImage,(WINDOWWIDTH, WINDOWHEIGHT))
windowSurfaceRectangle = windowSurface.get_rect()



#immagine labirinto
labirintoImage = pygame.image.load('ultimoLabi.png')
labirintoStretchedImage = pygame.transform.scale(labirintoImage,(800, 300))
labirintoRect = labirintoImage.get_rect()

#immagini giocatore e legna
playerImage = pygame.image.load('boscaiolo labirinto def.png')
playerRect = playerImage.get_rect()


legnaImage = pygame.image.load('legna 2.png')
legnaRect = legnaImage.get_rect()


gameOverSound = pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('game of t.mp3')                     #CAMBIA LA MUSICAAA


#pygame.draw.rect(windowSurface ,BLUE ,(30 , 444,  305 ,5))
#pygame.draw.rect(windowSurface ,BLUE ,(34 , 443,  5 ,325))
#pygame.draw.rect(windowSurface ,BLUE ,(30 , 675,  155 ,5))  #3
#pygame.draw.rect(windowSurface ,BLUE ,(34 , 766,  374 ,5))
#pygame.draw.rect(windowSurface ,BLUE ,(327, 675,  78 , 5))
#pygame.draw.rect(windowSurface ,BLUE ,(329, 673,  5 , 92))   #6
#pygame.draw.rect(windowSurface ,BLUE ,(400, 444,  378 ,5))
#pygame.draw.rect(windowSurface ,BLUE ,(774, 442,  5 ,324))
#pygame.draw.rect(windowSurface ,BLUE ,(105, 720,  81 , 5))   #9
#pygame.draw.rect(windowSurface ,BLUE ,(182, 719,  5 , 47))
#pygame.draw.rect(windowSurface, RED, (108, 442, 5, 491-442))
#pygame.draw.rect(windowSurface, BLACK, (108, 533, 5, 628-533))   #12
#pygame.draw.rect(windowSurface, BLACK, (105, 629, 334-105, 5))
#pygame.draw.rect(windowSurface, BLACK, (255, 628, 5, 722-628))
#pygame.draw.rect(windowSurface, BLACK, (181, 487, 5, 627-487))   #15
#pygame.draw.rect(windowSurface, BLACK, (179, 488, 477-179, 5))
#pygame.draw.rect(windowSurface, BLACK, (255, 533, 5, 581-533))
#pygame.draw.rect(windowSurface, BLACK, (255, 580, 334-255, 5))   #18
#pygame.draw.rect(windowSurface, BLACK, (331, 581, 5, 627-581))
#pygame.draw.rect(windowSurface, BLACK, (327, 534, 408-327, 5))
#pygame.draw.rect(windowSurface, BLACK, (404, 533, 5, 188))   #21
#pygame.draw.rect(windowSurface, BLACK, (478, 442, 5, 95))  
#pygame.draw.rect(windowSurface, BLACK, (478, 672, 5, 48))
#pygame.draw.rect(windowSurface, BLACK, (476, 766, 301, 5))   #24
#pygame.draw.rect(windowSurface, BLACK, (476, 720, 80, 5))
#pygame.draw.rect(windowSurface, BLACK, (552, 719, 5, 47))
#pygame.draw.rect(windowSurface, BLACK, (405, 627, 300, 5))   #27
#pygame.draw.rect(windowSurface, BLACK, (476, 580, 300, 5))
#pygame.draw.rect(windowSurface, BLACK, (552, 487, 5, 94))
#pygame.draw.rect(windowSurface, BLACK, (552, 671, 5, 3))   #30
#pygame.draw.rect(windowSurface, BLACK, (627, 443, 5, 48))
#pygame.draw.rect(windowSurface, BLACK, (627, 671, 5, 50))
#pygame.draw.rect(windowSurface, BLACK, (702, 487, 5, 49))   #33
#pygame.draw.rect(windowSurface, BLACK, (701, 671, 5, 50))
#pygame.draw.rect(windowSurface, BLACK, (553, 534, 150, 5)) 
#pygame.draw.rect(windowSurface, BLACK, (553, 673, 75, 5))   #36
#pygame.draw.rect(windowSurface ,BLUE ,(702, 673,  74 , 5))

pygame.display.update()



while True:
    linee = [lineQ, lineW, lineE, lineR, lineT, lineY, lineU, lineI, lineO, lineP, lineA, lineS, lineD, lineF, lineG, lineH, lineJ, lineK, lineL, lineZ, lineX, lineC, lineV, lineB, lineN, lineM, lineQQ, lineWW, lineEE, lineRR, lineTT, lineYY, lineUU, lineII, lineOO, linePP, lineAA] #metti tutte le linee
    moveLeft = moveRight = moveUp = moveDown = False
    playerRect.topleft = (WINDOWWIDTH -447, WINDOWHEIGHT - 395)
    legnaRect.topleft = (WINDOWWIDTH -387.5, WINDOWHEIGHT - 38)
    labirintoRect.topleft = (WINDOWWIDTH -770, WINDOWHEIGHT - 358)
    #musica
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
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
        if moveRight and playerRect.right < WINDOWWIDTH:
            playerRect.move_ip(PLAYERMOVERATE, 0)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * PLAYERMOVERATE)
        if moveDown and playerRect.bottom < WINDOWHEIGHT:
            playerRect.move_ip(0, PLAYERMOVERATE)
            
        windowSurface.blit(backgroundStretchedImage, windowSurfaceRectangle)
        windowSurface.blit(playerImage, playerRect)
        windowSurface.blit(legnaImage, legnaRect)
        windowSurface.blit(labirintoImage, labirintoRect)
        
        
        #quando il giocatore tocca la legna il gioco è finito    
       # if playerRect.colliderect(legnaRect) or  #tocca una linea:
        #    break
        
    #if #tocca linea:
     #   drawText('GAME OVER', font, windowSurface, 325
               #  , (WINDOWHEIGHT / 3))
      #  drawText('Premi un tasto per rigiocare.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
        #pygame.display.update() #aggiorno la schermata 
        #aspettaPremaTasto()
   # else: 
      #  break

#drawText('BRAVO!', font, windowSurface, 350, (WINDOWHEIGHT / 3))
#drawText('Hai trovato la legna!', font, windowSurface, 140, (WINDOWHEIGHT / 3) + 50)





pygame.display.update()