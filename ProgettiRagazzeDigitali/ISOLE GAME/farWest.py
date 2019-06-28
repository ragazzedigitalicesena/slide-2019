# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 09:02:44 2019

@author: scr.033
"""

#Far West
import random, pygame, sys, time
from pygame.locals import *

WINDOWHEIGHT = 600
WINDOWWIDTH = 600

#indica il frame per secondo, cioè una singola schermata
FPS = 60
#dimensioni diverse dei mostriciattoli verdi che scendono
CATTIVOMINSIZE = 100
CATTIVOMAXSIZE = 200
BUONOMINSIZE = 100
BUONOMAXSIZE = 150


#veloctà con cui vengono aggiunti i mostriciattoli che scendono 
NEWCATTIVO = 200000
NEWBUONO = 200000
REMOVECATTIVO = 500000
REMOVEBUONO = 500000


MAX_CATTIVI = 10

removeCattivo = 0
removeBuono = 0
cattivoCounter = 0
buonoCounter = 0
score = 0
SCORE = 10
#velocità con cui si sposta il giocatore
PLAYERMOVERATE = 5

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PURPLE = (128,0,128)
YELLOW = (255,255,0)
FUCSIA = (255,0,255)
AQUA = (0,255,255)
AQUAMARINE = (127,255,212)
BLUEVIOLET = (138,43,226)
LIGHTPINK = (255,182,193)
SALMON = (250,128,114)
ROYALBLUE = (65,105,225)
LILLA = (204,153,255)

#funzione che fa uscire dal gioco
def terminate():
    pygame.quit()
    sys.exit()

#funzione che sospende o fa aspettare il gioco che l'utente prema un tasto
def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
#l'utente preme un tasto
            #se preme un tasto qualsiasi l'utente comincia a giocare
            if event.type == KEYDOWN:
                #se l'utente preme ESC l'utente esce dal gioco
                if event.key == K_ESCAPE: 
                    terminate()
                return
    
def drawText(text, font, surface, x, y):
    #crea  il testo 
    textobj = font.render(text, 1, BLACK)
    #ci dà il rettangolo
    textrect = textobj.get_rect()
    #sposta il rettangolo in alto a sinistra nel posto dove ci ha detto l'utente
    textrect.topleft = (x, y)
    #disegna la scritta all'interno del triangolo
    surface.blit(textobj, textrect)

def mouseHasHitBuono(mouse, buoni):
    #se il rettangolo del giocatore o l'area occupata si scontra allora dimmi che il giocatore sta toccando un cattivo = TRUE; altrimenti =FALSE
    for b in buoni:
     #.collidirect ci dice quando il giocatore si scontra con i cattivi
     #(b[rect])= b è una scatola con molte informazioni dentro e di questa scatola  vogliamo conoscere solo il rect 
        if muose.colliderect(b):
            #se voglio contare quante volte il giocatore entra i contatto con i cattivi faccio o una print che ogni volta stampa il numero dei cattivi oppure creuna variabile globale che li conta
            return True
    return False

pygame.init()
#modo per gestire la velocità del gioco
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT),0,32)
#Titolo finestra
pygame.display.set_caption('The Far West')

pygame.mouse.set_cursor(*pygame.cursors.diamond)



windowSurfaceRectangle = windowSurface.get_rect()
backgroundImage = pygame.image.load('gameBackround.jpg')
introImage = pygame.image.load('intro.jpg')
backgroundStretchedImage = pygame.transform.scale(backgroundImage,(WINDOWWIDTH,WINDOWHEIGHT))
introStretchedImage = pygame.transform.scale(introImage,(WINDOWWIDTH,WINDOWHEIGHT))
windowSurface.blit(introStretchedImage,windowSurfaceRectangle)
pygame.display.update()

font = pygame.font.SysFont('Berlin Sans FB Demi', 48)
drawText('The Far West', font, windowSurface, (WINDOWWIDTH / 4), (WINDOWHEIGHT / 4))

drawText('Press a key to start.', font, windowSurface, (WINDOWWIDTH / 4) - 30, (WINDOWHEIGHT / 4) + 50)

pygame.display.update()

waitForPlayerToPressKey()
pygame.display.update()
windowSurface.blit(backgroundStretchedImage,windowSurfaceRectangle)
pygame.display.update()

cattivoImage = pygame.image.load('sam.png')
buonoImage = pygame.image.load('coccoloso.png')
boomImage = pygame.image.load('boom.png')

pygame.mixer.music.load('deserto2.mp3')
gameOverSound = pygame.mixer.Sound('gameover2.wav')

#cattivi = []
#for i in range(10):
#    CATTIVOSIZE = random.randint(CATTIVOMINSIZE, CATTIVOMAXSIZE)
#    cattivi.append(pygame.Rect(random.randint(0, WINDOWWIDTH - CATTIVOSIZE), random.randint(0, WINDOWHEIGHT - CATTIVOSIZE), CATTIVOSIZE, CATTIVOSIZE))
#new_cattivi = cattivi
#for cattivo in cattivi:
#    cattivoStretchedImage = pygame.transform.scale(cattivoImage,(CATTIVOSIZE,CATTIVOSIZE))
#new_cattivi = []


#while True:
#    cattivoCounter += 1
#    if cattivoCounter >= NEWCATTIVO:
#        # Add new cattivo.
#        cattivoCounter = 0
#        cattivi.append(pygame.Rect(random.randint(0, WINDOWWIDTH - CATTIVOSIZE), random.randint(0, WINDOWHEIGHT - CATTIVOSIZE), CATTIVOSIZE, CATTIVOSIZE))
#        for i in range(len(cattivi)):
#            for cattivo in cattivi:
#                windowSurface.blit(cattivoStretchedImage ,cattivo)
#        pygame.display.update()
#        waitForPlayerToPressKey()
#        terminate()
#cattivo = pygame.Rect(0,0,100,100)
#cattivoRectangle = cattivo.get_ret()
#cattivoImage = pygame.image.load('sam.png')
mainClock = pygame.time.Clock()
cattivi = []
buoni = []

while True:
#    cattivoCounter += 1
#    buonoCounter += 1
#    removeCattivo += 1
#    removeBuono += 1
    
#    if len(cattivi) == MAX_CATTIVI:
#                new_cattivi = cattivi
#                for c in range(0, random.randint(0, len(new_cattivi))):
#                    if len(new_cattivi) != 0:
#                        new_cattivi.remove(new_cattivi[0])
#                        cattivi = new_cattivi
#                        print(len(cattivi))
#            pygame.time.wait(20)
#            
#            mainClock.tick(40)
#        
#            new_cattivi = cattivi
#            for cattivo in new_cattivi:
#                if len(cattivi) == MAX_CATTIVI:
#                    cattivi.remove(cattivo)
#                    print(len(cattivi))
#                    new_cattivi = []
        
    pygame.mixer.music.play(-1, 0.0)        
        
    if True:
        cattivoCounter = 0
        CATTIVOSIZE = random.randint(CATTIVOMINSIZE, CATTIVOMAXSIZE)
        posCattivo1 = random.randint(0, WINDOWWIDTH - CATTIVOSIZE)
        posCattivo2 = random.randint(0, WINDOWHEIGHT - CATTIVOSIZE)
        cattivo = pygame.Rect(posCattivo1, posCattivo2, CATTIVOSIZE, CATTIVOSIZE)
        cattivoStretchedImage = pygame.transform.scale(cattivoImage,(CATTIVOSIZE,CATTIVOSIZE))
        cattivi.append(cattivo)
#        windowSurface.blit(cattivoStretchedImage ,cattivo)
        time.sleep(1)
#        cattivi.remove(cattivoStretchedImage)
        for c in cattivi:
            windowSurface.blit(backgroundStretchedImage,windowSurfaceRectangle)
            windowSurface.blit(cattivoStretchedImage ,c)
        pygame.display.update()
        
#    if True:
#        removeCattivo = 0
#        cattivi.remove(cattivo)
#        windowSurface.blit(backgroundStretchedImage,windowSurfaceRectangle)
#        pygame.display.update()
    
    if True:
        buonoCounter = 0
        BUONOSIZE = random.randint(BUONOMINSIZE, BUONOMAXSIZE)
        posBuono1 = random.randint(0, WINDOWWIDTH - BUONOSIZE)
        posBuono2 = random.randint(0, WINDOWHEIGHT - BUONOSIZE)
        buono = pygame.Rect(posBuono1, posBuono2, BUONOSIZE, BUONOSIZE)
        buoni.append(buono)
        buonoStretchedImage = pygame.transform.scale(buonoImage,(BUONOSIZE,BUONOSIZE))
        windowSurface.blit(buonoStretchedImage ,buono)
        pygame.display.update()
    
#    if removeBuono == REMOVEBUONO:
#        removeBuono = 0
#        windowSurface.blit(backgroundStretchedImage,windowSurfaceRectangle)

#        pygame.display.update()

    for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
    #l'utente preme un tasto
            #se preme un tasto qualsiasi l'utente comincia a giocare
            if event.type == KEYDOWN:
                #se l'utente preme ESC l'utente esce dal gioco
                if event.key == K_ESCAPE: 
                    terminate()
            if event.type == MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                mouse = pygame.Rect(pos,(10,10))
                print(pos)
#                tuplaCattivo = (posCattivo1, posCattivo2)
#                mouseCattivo = pygame.Rect(pos, tuplaCattivo)
#                tuplaBuono = (posBuono1, posBuono2)
#                mouseBuono = pygame.Rect(pos, tuplaBuono)
                for c in cattivi:
                    if mouse.colliderect(c):
                        print('True')
                        cattivi.remove(c)
                        boomStretchedImage = pygame.transform.scale(boomImage,(CATTIVOSIZE,CATTIVOSIZE))
                        windowSurface.blit(boomStretchedImage, c)
                        score += 1
                        pygame.display.update()
                    else:
                        print('False')
                
                if mouse.colliderect(buono):
                    pygame.mixer.music.stop()
                    NEWCATTIVO = -1
                    NEWBUONO = -1
                    waitForPlayerToPressKey()
                    gameOverSound.play()
                    drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 4), (WINDOWHEIGHT / 4))
                    pygame.display.update()
                    print('Scema')
                    waitForPlayerToPressKey()
                    terminate()
                    gameOverSound.stop()
    
    if score >= SCORE:
#        waitForPlayerToPressKey()
        drawText('YOU WIN!', font, windowSurface, (WINDOWWIDTH / 4), (WINDOWHEIGHT / 4))
        pygame.display.update()
        waitForPlayerToPressKey()
        terminate()
#                    score -= 1
                    
                

#    new_cattivi = cattivi
#    for cattivo in new_cattivi:
#        if cattivoCounter == NEWCATTIVO/2:
#            cattivi.remove(cattivo)
#    new_cattivi = cattivi






