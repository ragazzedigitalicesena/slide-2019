# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 12:12:17 2019

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
font = pygame.font.SysFont(None, 48)

# Set up sounds.
#aggiungo un file audio nel gioco 
gameOverSound = pygame.mixer.Sound('gameover3.wav')
pygame.mixer.music.load('regnodighiaccio3.wav')

# Set up images.
#aggiungo le immagini di sfondo
sfondo=pygame.image.load('ghiaccio2.jpg')
sfondoStretchedImage=pygame.transform.scale(sfondo,(WINDOWWIDTH, WINDOWHEIGHT))
playerStretchedImage = pygame.image.load('elsa.png')
playerImage= pygame.transform.scale(playerStretchedImage,(75, 75))
#salvo in una variabile l'immagine del giocatore
playerRect = playerImage.get_rect()
baddieStretchedImage = pygame.image.load('qyyy.png')
baddieImage= pygame.transform.scale(baddieStretchedImage,(50, 50))
pygame.display.update()

# Show the "Start" screen.
windowSurface.blit(sfondoStretchedImage,windowSurfaceRectangle)
pygame.display.update()
#funzione che stampa il testo con il font definito alla riga 84
drawText('FIRST CHALLENGE:', font, windowSurface, (WINDOWWIDTH / 3)-80, (WINDOWHEIGHT / 3)+60)
#posiziona nel centro della schermata la scritta
drawText('TRY TO', font, windowSurface, (WINDOWWIDTH / 3)+10, (WINDOWHEIGHT / 3) + 90)
drawText('SURVIVE!', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3) + 120)
#aggiorna la schermata di gioco
pygame.display.update()
#aspetta che il giocatore prema un tasto per iniziare il gioco o per usicre
waitForPlayerToPressKey()
windowSurface.blit(sfondoStretchedImage,windowSurfaceRectangle)
pygame.display.update()

#il punteggio massimo è 0
#è una variabile che dice qual è il punteggio massimo che il giocatore ha fatto su tutte le partite
topScore = 500
while True:
    # Set up the start of the game.
    #lista vuota
    baddies = []
    #punteggio di una singola partita
    score = 0
    #posiziono il rettangolo del giocatore, salvato nella riga, e lo metto al centro nella parte inferiore della schermata 
    playerRect.topleft = (WINDOWWIDTH/2, WINDOWHEIGHT -80)
    #dicono se ad ogni giro il giocatore s muove a destra, sinistra, alto o basso
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False
    #quando diventa 6 aggiunge un nuovo cattivo
    baddieAddCounter = 0
    #inizia a riprodurre la musica 
    #-1 e 0.0 sono due parametri il primo dice di riprodurre la musica dopo che è finita e 0,0 indica che la musica parte dall'inizio
    pygame.mixer.music.play(-1, 0.0)
    pygame.display.update()
    
#inizia un altro ciclo qunado sto giocando e i cattivi iniziano a scendere
#codice che mi dice cosa fare quando il giocatore preme queest tasti
    while True: # The game loop runs while the game part is playing.
        score += 1 # Increase score.
        if score== topScore:
            windowSurface.blit(sfondoStretchedImage,windowSurfaceRectangle)
            drawText('YOU WIN!', font, windowSurface, (WINDOWWIDTH / 3)-10, (WINDOWHEIGHT / 3)+30)
            drawText('NOW', font, windowSurface, (WINDOWWIDTH / 3)+30, (WINDOWHEIGHT / 3)+60)
            drawText('YOU CAN CONTINUE', font, windowSurface, (WINDOWWIDTH / 3) -80 , (WINDOWHEIGHT / 3)+90)
            drawText('YOUR GAME', font, windowSurface, (WINDOWWIDTH / 3) -20, (WINDOWHEIGHT / 3) +120)
            pygame.display.update()
            waitForPlayerToPressKey()
            terminate()

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

            #quando muovo il mouse non si vede ma si muove il personaggio
            if event.type == MOUSEMOTION:
                # If the mouse moves, move the player where to the cursor.
                playerRect.centerx = event.pos[0]
                playerRect.centery = event.pos[1]
                pygame.display.update()
          # Add new baddies at the top of the screen, if needed.
        #Se NON stiamo premenso Z o X allora incrementiamo la variabile baddieAddCounter ad ogni ciclo
        if not reverseCheat and not slowCheat:
            baddieAddCounter += 1
        if baddieAddCounter == ADDNEWBADDIERATE:
            baddieAddCounter = 0
           #creo un nuovo cattivo
            baddieSize = random.randint(BADDIEMINSIZE, BADDIEMAXSIZE)
            newBaddie = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - baddieSize), 0 - baddieSize, baddieSize, baddieSize),
                        'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                        'surface':pygame.transform.scale(baddieImage, (baddieSize, baddieSize)),}
            baddies.append(newBaddie)
            pygame.display.update()


#Usiamo sempre i booleani per verificare in che direzione spostare il giocatore. Per muoverlo chiamiamo una funzione move ip(x,y) in cui x e lo spostamento sull’asse orizzonatle e y su quello verticale.          
# Move the player around.
         
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
            #
        if moveRight and playerRect.right < WINDOWWIDTH:
            playerRect.move_ip(PLAYERMOVERATE, 0)

        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * PLAYERMOVERATE)
        if moveDown and playerRect.bottom < WINDOWHEIGHT:
            playerRect.move_ip(0, PLAYERMOVERATE)

        # Move the baddies down.
        #per i cattivi della lista 
        for b in baddies:
            #se non vanno al contrario e non sono lenti prendo il rettangolo del cattivo e lo sposto verso il basso per la loro velocità
            if not reverseCheat and not slowCheat:
                b['rect'].move_ip(0, b['speed'])
                #se vanno al contrario li sposto verso l'alto
            elif reverseCheat:
                b['rect'].move_ip(0, -5)
                #altrimenti se vanno piano vanno tutti alla stessa velocità e scendono una alla volta
            elif slowCheat:
                b['rect'].move_ip(0, 1)

        # Delete baddies that have fallen past the bottom.
        # per ogni cattivo
        for b in baddies[:]:
             #se il suo rettangolo è nella parte sopra della schermata posso toglierlo dalla lista 
            if b['rect'].top > WINDOWHEIGHT:
                baddies.remove(b)

        # Draw the game world on the window.
        #coloro tutto lo sfondo di bianco
        windowSurface.blit(sfondoStretchedImage,windowSurfaceRectangle)
       
        # Draw the player's rectangle.
        #disegno il giocatore
        windowSurface.blit(playerImage, playerRect)

        # Draw each baddie.
        #disego i cattivi
        for b in baddies:
            windowSurface.blit(b['surface'], b['rect'])

        #aggiorno la schermata
        pygame.display.update()

        # Check if any of the baddies have hit the player.
        #verifichiamo se il giocatore ha colito i cattivi
        if playerHasHitBaddie(playerRect, baddies):
            pygame.mixer.music.stop()
            gameOverSound.play()
            windowSurface.blit(sfondoStretchedImage,windowSurfaceRectangle)
            drawText("YOU'RE DEAD!", font, windowSurface, (WINDOWWIDTH / 3)-20, (WINDOWHEIGHT / 3)+60)
            pygame.display.update()
            waitForPlayerToPressKey()
            terminate()
        #scatta ogni 60 milllisecondi
        mainClock.tick(FPS)

    # Stop the game and show the "Game Over" screen.
    #stoppo la  musica e riproduco quella della sconfitta
    pygame.mixer.music.stop()
    gameOverSound.play()
    gameOverSound.stop()