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
    
def colpireLabirinto(playerRect, line):
    for b in line: #per ogni roccia dentro la lista
        if playerRect.colliderect(b['rect']): # se l'area che occupa il giocatore è la stessa di un cattivo ..
#        b rect modo per prendere l'area che il cattivo sta usando 
            return True
    return False

def colpireLegna(playerRect, legna):
    if playerRect : # tocca la legna
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

windowSurface.blit(backgroundStretchedImage, windowSurfaceRectangle)

#immagine labirinto
labirintoImage = pygame.image.load('ultimoLabi.png')
labirintoStretchedImage = pygame.transform.scale(labirintoImage,(800, 300))
labirintoRect = labirintoImage.get_rect()
labirintoRect.topleft = (WINDOWWIDTH -770, WINDOWHEIGHT - 358)
windowSurface.blit(labirintoImage, labirintoRect)

#immagini giocatore e legna
playerImage = pygame.image.load('boscaioloDefinitivoForse.png')
playerRect = playerImage.get_rect()
playerRect.topleft = (WINDOWWIDTH -447, WINDOWHEIGHT - 395)
windowSurface.blit(playerImage, playerRect)

legnaImage = pygame.image.load('legna.png')
legnaRect = legnaImage.get_rect()
legnaRect.topleft = (WINDOWWIDTH -387.5, WINDOWHEIGHT - 38)
windowSurface.blit(legnaImage, legnaRect)


gameOverSound = pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('game of t.mp3')                     #CAMBIA LA MUSICAAA


pygame . draw . line ( windowSurface , BLACK , (30 , 444), (335, 444) , 5)    # OKK
pygame . draw . line ( windowSurface , BLACK , (34 , 443), (34 , 768) , 9)    # OKK
pygame . draw . line ( windowSurface , BLACK , (30 , 675), (185, 675) , 5)    # OKK 3
pygame . draw . line ( windowSurface , BLACK , (34 , 766), (408, 766) , 5)    # OKK
pygame . draw . line ( windowSurface , BLACK , (327, 675), (405, 675) , 5)    # OKK
pygame . draw . line ( windowSurface , BLACK , (329, 673), (329, 765) , 9)    # OKK 6
pygame . draw . line ( windowSurface , BLACK , (400, 444), (778, 444) , 5)    # OKK
pygame . draw . line ( windowSurface , BLACK , (774, 442), (774, 766) , 9)    # OKK
pygame . draw . line ( windowSurface , BLACK , (105, 720), (186, 720) , 5)    # OKK 9
pygame . draw . line ( windowSurface , BLACK , (182, 719), (182, 766) , 9)    # OKK

#pygame . draw . line ( windowSurface , BLACK , (108, 442), (108, 491) , 9)    # OKK
#pygame . draw . line ( windowSurface , BLACK , (108, 533), (108, 628) , 9)    # OKK 12
#pygame . draw . line ( windowSurface , BLACK , (105, 629), (334, 629) , 5)    # OKK
#pygame . draw . line ( windowSurface , BLACK , (255, 628), (255, 722) , 9)    # OKK
#pygame . draw . line ( windowSurface , BLACK , (181, 487), (181, 627) , 9)    # OKK 15
#pygame . draw . line ( windowSurface , BLACK , (179, 488), (477, 488) , 5)    # OKK
#pygame . draw . line ( windowSurface , BLACK , (255, 533), (255, 581) , 9)    # OKK
#pygame . draw . line ( windowSurface , BLACK , (255, 580), (334, 580) , 5)    # OKK 18
#pygame . draw . line ( windowSurface , BLACK , (331, 581), (331, 627) , 9)    # OKK
#pygame . draw . line ( windowSurface , BLACK , (327, 534), (408, 534) , 5)    # OKK
#pygame . draw . line ( windowSurface , BLACK , (404, 533), (404, 721) , 9)    # OKK 21

pygame.draw.rect(windowSurface, RED, (108, 442, 9, 491-442))
pygame.draw.rect(windowSurface, BLACK, (108, 533, 9, 628-533))
pygame.draw.rect(windowSurface, BLACK, (105, 629, 334-105, 5))
pygame.draw.rect(windowSurface, BLACK, (255, 628, 9, 722-628))
pygame.draw.rect(windowSurface, BLACK, (181, 487, 9, 627-487))
pygame.draw.rect(windowSurface, BLACK, (179, 488, 477-179, 5))
pygame.draw.rect(windowSurface, BLACK, (255, 533, 9, 581-533))
pygame.draw.rect(windowSurface, BLACK, (255, 580, 334-255, 5))
pygame.draw.rect(windowSurface, BLACK, (331, 581, 9, 627-581))
pygame.draw.rect(windowSurface, BLACK, (327, 534, 408-327, 5))
pygame.draw.rect(windowSurface, BLACK, (404, 533, 9, 721-533))





pygame . draw . line ( windowSurface , BLACK , (478, 442), (478, 537) , 9)    # OKK
pygame . draw . line ( windowSurface , BLACK , (478, 672), (478, 720) , 9)    # OKK
pygame . draw . line ( windowSurface , BLACK , (476, 766), (777, 766) , 5)    # OKK 24
pygame . draw . line ( windowSurface , BLACK , (476, 720), (556, 720) , 5)    # OKK
pygame . draw . line ( windowSurface , BLACK , (552, 719), (552, 766) , 9)    # OKK
pygame . draw . line ( windowSurface , BLACK , (405, 627), (705, 627) , 5)    # OKK 27
pygame . draw . line ( windowSurface , BLACK , (476, 580), (776, 580) , 5)    # OKK 
pygame . draw . line ( windowSurface , BLACK , (552, 487), (552, 581) , 9)    # OKK 
pygame . draw . line ( windowSurface , BLACK , (552, 671), (552, 674) , 9)    # OKK 30
pygame . draw . line ( windowSurface , BLACK , (627, 443), (627, 491) , 9)    # OKK
pygame . draw . line ( windowSurface , BLACK , (627, 671), (627, 721) , 9)    # OKK
pygame . draw . line ( windowSurface , BLACK , (702, 487), (702, 536) , 9)    # OKK 33
pygame . draw . line ( windowSurface , BLACK , (701, 671), (701, 721) , 9)    # OKK
pygame . draw . line ( windowSurface , BLACK , (553, 534), (703, 534) , 5)    # OKK
pygame . draw . line ( windowSurface , BLACK , (553, 673), (629, 673) , 5)    # OKK 36
pygame . draw . line ( windowSurface , BLACK , (702, 673), (776, 673) , 5)    # OKK

pygame.display.update()



while True:
    moveLeft = moveRight = moveUp = moveDown = False
    #posizionare il giocatore all'inzio del labirinto
    #posizionare la legna alla fine del labirinto
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