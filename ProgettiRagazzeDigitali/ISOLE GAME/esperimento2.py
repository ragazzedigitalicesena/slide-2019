# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 23:20:56 2019

@author: Camilla
"""

import pygame, random, sys
from pygame.locals import *
import time
#import pygame_textinput

WINDOWWIDTH = 700
#altezza della finestra
WINDOWHEIGHT = 600
#colore della scritta 
TEXTCOLOR = (255, 255, 255)
#colore dello sfondo
BACKGROUNDCOLOR = (255, 255, 255)
BLUE=(153, 255, 255)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
#indica il frame per secondo, cioè una singola schermata
FPS = 60
#dimensioni diverse dei mostriciattoli verdi che scendono
BADDIEMINSIZE = 10
BADDIEMAXSIZE = 30
#velocità diverse dei mostriciattoli
BADDIEMINSPEED = 1
BADDIEMAXSPEED = 2
#velocità con cui vengono aggiunti i mostriciattoli che scendono 
ADDNEWBADDIERATE = 12
#velocità con cui si sposta il giocatore
PLAYERMOVERATE = 5

def terminate():
    pygame.quit()
    sys.exit()
    
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
#funzione che mi permette di capire se il giocatore si è scontrato con un cattivo
def playerHasHitBaddie(playerRect, baddies):
    #se il rettangolo del giocatore o l'area occupata si scontra allora dimmi che il giocatore sta toccando un cattivo = TRUE; altrimenti =FALSE
    for b in baddies:
     #.collidirect ci dice quando il giocatore si scontra con i cattivi
     #(b[rect])= b è una scatola con molte informazioni dentro e di questa scatola  vogliamo conoscere solo il rect 
        if playerRect.colliderect(b['rect']):
            #se voglio contare quante volte il giocatore entra in contatto con i cattivi faccio o una print che ogni volta stampa il numero dei cattivi oppure cre0 una variabile globale che li conta
            return True
    return False

#funzione che serve per mostrare una finestra dove verrà scritto il testo
def drawText(text, font, surface, x, y):
    #crea  il testo 
    textobj = font.render(text, 1, TEXTCOLOR)
    #ci dà il rettangolo
    textrect = textobj.get_rect()
    #sposta il rettangolo in alto a sinistra nel posto dove ci ha detto l'utente
    textrect.topleft = (x, y)
    #disegna la scritta all'interno del triangolo
    surface.blit(textobj, textrect)
#(visto che ci serviranno molte scritte è comodo stampare tutte queste variabili in una sola funzione per richiamarla in questo modo una sola volta )


def textInput(xPosition, yPosition):
    
    textinput = pygame_textinput.TextInput()  
    clock = pygame.time.Clock()
    

    while True:
        
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.quit()
    
        # Feed it with events every frame
#        textinput.update(events)
        # Blit its surface onto the screen
        windowSurface.blit(textinput.get_surface(), (xPosition, yPosition))
    
        pygame.display.update()
        clock.tick(30)
        
        if textinput.update(events):
            return textinput.get_text()


# Set up pygame, the window, and the mouse cursor.
#chiamo pygame.init() per inizializzare il gioco
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
font = pygame.font.SysFont(None, 78)

base=pygame.image.load('bakground.png')
baseStretchedImage=pygame.transform.scale(base,(WINDOWWIDTH, WINDOWHEIGHT))
windowSurface.blit(baseStretchedImage,windowSurfaceRectangle)
drawText('THE DUCK GAME', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3) )
#pygame.mixer.music.load('sfondoiniziale2.wav')
pygame.display.update()
waitForPlayerToPressKey()
windowSurface.blit(baseStretchedImage,windowSurfaceRectangle)
drawText('TIRO IL DADO...', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3) )
pygame.display.update()
dado = random.randint(1,6)
numero = 0
waitForPlayerToPressKey()
pygame.init()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
windowSurfaceRectangle = windowSurface.get_rect()
baseStretchedImage=pygame.transform.scale(base,(WINDOWWIDTH, WINDOWHEIGHT))
windowSurface.blit(baseStretchedImage,windowSurfaceRectangle)
drawText('THE DUCK GAME', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3) )
#pygame.mixer.music.load('sfondoiniziale2.wav')
pygame.display.update()
waitForPlayerToPressKey()