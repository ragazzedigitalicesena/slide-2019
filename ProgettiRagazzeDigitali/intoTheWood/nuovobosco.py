
import random, sys, pygame, time
from pygame.locals import *

WINDOWWIDTH = 900
WINDOWHEIGHT = 900
TEXTCOLOR = (0, 0, 0)
BACKGROUNDCOLOR = (100,155,255)
    #frame al secondo
FPS = 60
PESCEMINSIZE = 20
PESCEMAXSIZE = 70
PESCEMINSPEED = 1
PESCEMAXSPEED = 4
ADDNEWPESCERATE = 20
PLAYERMOVERATE = 2 # di quanto si muove il giocatore (tieni un valore basso)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ALTROAZZURRO = (100,155,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN=(101,67,33)
SABBIA=(218,189,171)

pesceSize=random.randint(PESCEMINSIZE, PESCEMAXSIZE)
pesceSpeed=random.randint(PESCEMINSPEED, PESCEMAXSPEED)

SCOREWINNER = 10
score=0
def terminate():
    pygame.quit()
    sys.exit()
    
def aspettaPremaTasto():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # tato ESC 
                    terminate()
                return
            
def toccarePesci(playerRect, listaPesci):
    for b in listaPesci: #per ogni pesce dentro la lista
        if playerRect.colliderect(b['rect']): # se l'area che occupa il giocatore è la stessa di un pesce ..
#        b rect modo per prendere l'area che il cattivo sta usando 
            score+=1
            return score


def drawText(text, font, surface, x, y):
    textobj = font.render(text, True, SABBIA, BLACK) #crea il testo
    textrect = textobj.get_rect() #gli dà un rettangolo
    textrect.topleft = (x, y) #lo posiziona
    surface.blit(textobj, textrect)

def vittoria():
    drawText('sei riuscito a pescare abbastanza pesce per la cena!', font, windowSurface, 140, (WINDOWHEIGHT / 3) + 50)
    
    
    
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

backgroundImage = pygame.image.load('fondale.jpg')
backgroundStretchedImage = pygame.transform.scale(backgroundImage,(WINDOWWIDTH, WINDOWHEIGHT))
windowSurfaceRectangle = windowSurface.get_rect()

pygame.display.set_caption('FISHH')   #titoletto della finestra (in alto)
pygame.mouse.set_visible(False) #prendi ilmouse e quando è sulla finestra nascondilo
# Set up the fonts.
font = pygame.font.SysFont(None, 48)

gameOverSound = pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('river.mp3')

playerImage = pygame . image . load ('bosca3.png')
playerRect = playerImage.get_rect()
pesceImage = pygame . image . load ('pesce.png')
pesceRect = pesceImage.get_rect()

drawText('PESCA 10 PESCI PER LA CENA! FAI ATTENZIONE AGLI OSTACOLI!!', font, windowSurface, 80, 100)  # vedi funzione sopra (stampa il testo)
drawText('PREMI UN TASTO PER PARTIRE.', font, windowSurface, 155, 700)
drawText('Per muoverti potrai usare le frecciette ', font, windowSurface, 132, 350)
drawText('o i seguenti tasti: a per andare a sinistra,', font, windowSurface, 112, 380)
drawText('s per scendere, d per andare a destra, w per salire.', font, windowSurface, 50, 410)

pygame.display.update()

aspettaPremaTasto()

#topScore = 0     # visualizza il punteggio piu alto di tutte le partite giocate 
#while True: # ogni volta che l'utente ricomincia a giocare
#    # Set up the start of the game.
#    listaPesci= [] #lista
#    score = 0 #punteggio singola partita
#    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 66)  #giocatore al centro nella parte inferiore
#    moveLeft = moveRight = moveUp = moveDown = False # mi servono per dire di spostare il personaggio 
#    pesciAddCounter = 0  # aggiunge un nuovo cattivo quanto rocciaaddrate arriva a 6 
#    pygame.mixer.music.play(-1, 0.0)   # parte la  musica (in secondi)
#    
#    
#    while True: # The game loop runs while the game part is playing.
#    
##  codice che dice a python cosa fare quando il giocatore preme i tasti 
#        for event in pygame.event.get(): # ogni vlta che succede qualcosa 
#            if event.type == QUIT: # se clicca la x 
#                terminate()
#
#            if event.type == KEYDOWN: #se il giocatore preme un tasto
#                if event.key == K_LEFT or event.key == K_a:
#                    moveRight = False
#                    moveLeft = True
#                if event.key == K_RIGHT or event.key == K_d:
#                    moveLeft = False
#                    moveRight = True
#                if event.key == K_UP or event.key == K_w:
#                    moveDown = False
#                    moveUp = True
#                if event.key == K_DOWN or event.key == K_s:
#                    moveUp = False
#                    moveDown = True
#
#            if event.type == KEYUP: # se il giocatore rilascia un tasto
#                if event.key == K_ESCAPE:
#                        terminate()
#                if event.key == K_LEFT or event.key == K_a:
#                    moveLeft = False
#                if event.key == K_RIGHT or event.key == K_d:
#                    moveRight = False
#                if event.key == K_UP or event.key == K_w:
#                    moveUp = False
#                if event.key == K_DOWN or event.key == K_s:
#                    moveDown = False
#
#        pesciAddCounter += 1
#        if pesciAddCounter == ADDNEWPESCERATE:
#            pesciAddCounter = 0
#            pesceSize = random.randint(PESCEMINSIZE, PESCEMAXSIZE)  # dimensione random
#            newPesce = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - pesceSize), 0 - pesceSize, pesceSize, pesceSize), #
#                        'speed': random.randint(PESCEMINSPEED, PESCEMAXSPEED),
#                        'surface':pygame.transform.scale(pesceImage, (pesceSize, pesceSize)),}
#            listaPesci.append(newPesce)
#    
#    
#        if moveLeft and playerRect.left > 0:
#            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
#        if moveRight and playerRect.right < WINDOWWIDTH:
#            playerRect.move_ip(PLAYERMOVERATE, 0)
#        if moveUp and playerRect.top > 0:
#            playerRect.move_ip(0, -1 * PLAYERMOVERATE)
#        if moveDown and playerRect.bottom < WINDOWHEIGHT:
#            playerRect.move_ip(0, PLAYERMOVERATE)
#    
#    
#        if toccarePesci(playerRect,listaPesci) or score == SCOREWINNER:
#            break
#        elif not toccarePesci(playerRect, listaPesci) and score != SCOREWINNER:
#            for b in listaPesci:
#                toccarePesci()
##                b['rect'].move_ip(0, b['speed'])
##            score += 1
#            
#        for b in listaPesci[:]:     # quando un cattivo esce dalla finestra 
#            if b['rect'].top > WINDOWHEIGHT:
#                listaPesci.remove(b)
#                
#        windowSurface.blit(backgroundStretchedImage, windowSurfaceRectangle) 
#        
#        scoreText= 'Score: ' + str(score)
#        drawText(scoreText, font, windowSurface, 10, 0)
#        
#        windowSurface.blit(playerImage, playerRect)
#        
#        for b in listaPesci:
#            windowSurface.blit(b['surface'], b['rect'])
#            
#        pygame.display.update()
#        
#        mainClock.tick(FPS)
#        
#    if toccarePesci(playerRect, listaPesci):
#        pygame.mixer.music.stop()
#        gameOverSound.play()
#        drawText('GAME OVER', font, windowSurface, 325
#                 , (WINDOWHEIGHT / 3))
#        drawText('Premi un tasto per rigiocare.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
#        pygame.display.update() #aggiorno la schermata 
#        aspettaPremaTasto()
#    else: 
#        break
#
#pygame.mixer.music.stop()
#drawText('BRAVO!', font, windowSurface, 350, (WINDOWHEIGHT / 3))
#drawText('Hai raggiunto la cima della montagna!', font, windowSurface, 140, (WINDOWHEIGHT / 3) + 50)
#
#pygame.display.update()




