# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 10:56:04 2019

@author: scr.039
"""

import pygame, random, sys
from pygame.locals import *
import time


#parte delle costanti (dimensioni finestra di gioco, colore del testo, colore dello sfondo )
#larghezza della finestra
WINDOWWIDTH = 600
#altezza della finestra
WINDOWHEIGHT = 600
#colore della scritta 
TEXTCOLOR = (255, 255, 255)
#colore dello sfondo
BACKGROUNDCOLOR = (255, 255, 255)
BLUE=(153, 255, 255)
BLACK=(0, 0, 0)
#indica il frame per secondo, cioè una singola schermata
FPS = 60
PLAYERMOVERATE = 5
#definisco tutte le funzioni del gioco
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
                if event.key == K_ESCAPE: #
                    terminate()
                return
def drawText(text, font, surface, x, y):
    #crea  il testo 
    textobj = font.render(text, 1, TEXTCOLOR)
    #ci dà il rettangolo
    textrect = textobj.get_rect()
    #sposta il rettangolo in alto a sinistra nel posto dove ci ha detto l'utente
    textrect.topleft = (x, y)
    #disegna la scritta all'interno del triangolo
    surface.blit(textobj, textrect)

    
    
pygame.init()
#modo per gestire la velocità del gioco
mainClock = pygame.time.Clock()
#creiamo la finestra di gioco 
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
windowSurfaceRectangle = windowSurface.get_rect()
#è il titoletto nella finestra 
pygame.display.set_caption('ISOLE GAME')
#pygame prendi il mouse e quando è sulla mia finestra nascondilo
pygame.mouse.set_visible(False)

# Set up the fonts.
#variabile globale che definisce il font di default per tutto il gioco
font = pygame.font.SysFont(None, 48)
sfondo2=pygame.image.load('montagna.jpg')
labirintoStretchedImage=pygame.image.load('labirinto1.gif')
labirinto=pygame.transform.scale(labirintoStretchedImage, (WINDOWWIDTH, WINDOWHEIGHT))
sfondoStretchedImage2=pygame.transform.scale(sfondo2,(WINDOWWIDTH, WINDOWHEIGHT))
playerStretchedImage2 = pygame.image.load('Koda.png')
playerImage2= pygame.transform.scale(playerStretchedImage2,(60, 60))
mieleStretchedImage= pygame.image.load('miele.png')
mieleImage= pygame.transform.scale(mieleStretchedImage, (70, 70))

sound= pygame.mixer.Sound('montagna.wav')
#salvo in una variabile l'immagine del giocatore
playerRect2 = playerImage2.get_rect()
mieleRect= mieleImage.get_rect()
windowSurface.blit(sfondoStretchedImage2,windowSurfaceRectangle)
pygame.display.update()
#funzione che stampa il testo con il font definito alla riga 84
drawText('FOURTH CHALLENGE:', font, windowSurface, (WINDOWWIDTH / 3)-80, (WINDOWHEIGHT / 3)+60)
drawText('ESCAPE!', font, windowSurface, (WINDOWWIDTH / 3)+10, (WINDOWHEIGHT / 3)+90)
pygame.display.update()
#aspetta che il giocatore prema un tasto per iniziare il gioco o per usicre
waitForPlayerToPressKey()

while True:
    playerRect2.topleft = (WINDOWWIDTH/2+230, WINDOWHEIGHT-60)
    mieleRect.topleft= (0,0)
    pygame.display.update()
    #dicono se ad ogni giro il giocatore s muove a destra, sinistra, alto o basso
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False
    
    while True:
        windowSurface.blit(labirinto, windowSurfaceRectangle)
        windowSurface.blit(mieleImage, mieleRect)
        sound.play()
        for event in pygame.event.get():
            #se l'utente clicca ESC termina il gioco
            if event.type == QUIT:
                terminate()
#se il giocatore preme un tasto qualsiasi

            if event.type == KEYDOWN:
                #se preme z i cattivi tornano in alto
                #se premo x modifico la variabile slowCheat
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

        if moveLeft and playerRect2.left > 0:
            playerRect2.move_ip(-1 * PLAYERMOVERATE, 0)
            #
        if moveRight and playerRect2.right < WINDOWWIDTH:
            playerRect2.move_ip(PLAYERMOVERATE, 0)

        if moveUp and playerRect2.top > 0:
            playerRect2.move_ip(0, -1 * PLAYERMOVERATE)
        if moveDown and playerRect2.bottom < WINDOWHEIGHT:
            playerRect2.move_ip(0, PLAYERMOVERATE)
        
        windowSurface.blit(playerImage2, playerRect2)
        windowSurface.blit(mieleImage, mieleRect)
        pygame.display.update()
        
        if playerRect2.colliderect(mieleRect):
            windowSurface.blit(sfondoStretchedImage2,windowSurfaceRectangle)
            pygame.display.update()
            drawText('YOU WIN!', font, windowSurface, (WINDOWWIDTH / 3)-10, (WINDOWHEIGHT / 3)+30)
            drawText('NOW', font, windowSurface, (WINDOWWIDTH / 3)+30, (WINDOWHEIGHT / 3)+60)
            drawText('YOU CAN CONTINUE', font, windowSurface, (WINDOWWIDTH / 3) -80 , (WINDOWHEIGHT / 3)+90)
            drawText('YOUR GAME', font, windowSurface, (WINDOWWIDTH / 3) -20, (WINDOWHEIGHT / 3) +120)
            pygame.display.update()
            waitForPlayerToPressKey()
            terminate()
            
           
        mainClock.tick(FPS)
           