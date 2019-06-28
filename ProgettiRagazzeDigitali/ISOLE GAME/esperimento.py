# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 22:53:17 2019

@author: Camilla
"""

import pygame, random, sys
from pygame.locals import *
import time
import pygame_textinput

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
#pygame.mouse.set_visible(False)

# Set up the fonts.
#variabile globale che definisce il font di default per tutto il gioco
font2 = pygame.font.SysFont(None, 78)
font = pygame.font.SysFont(None, 48)

base=pygame.image.load('bakground.png')
baseStretchedImage=pygame.transform.scale(base,(WINDOWWIDTH, WINDOWHEIGHT))
windowSurface.blit(baseStretchedImage,windowSurfaceRectangle)
drawText('THE DUCK GAME', font2, windowSurface, (WINDOWWIDTH /3)-50, (WINDOWHEIGHT /3)-50 )
pygame.mixer.music.load('sfondoiniziale2.wav')
pygame.display.update()
waitForPlayerToPressKey()
windowSurface.blit(baseStretchedImage,windowSurfaceRectangle)
drawText('TIRO IL DADO...', font2, windowSurface, (WINDOWWIDTH /3)-40, (WINDOWHEIGHT /3)-40 )
pygame.display.update()
numero = 7
waitForPlayerToPressKey()
while True:
#    dado = random.randint(1,6)
#    numero = numero + dado
    while numero <9:
        condizione =True
        if numero==1:
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
            pygame.mixer.music.play(-1, 0.0)
    #il punteggio massimo è 0
    #è una variabile che dice qual è il punteggio massimo che il giocatore ha fatto su tutte le partite
            topScore = 600
            while condizione:
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
    #            pygame.mixer.music.play(-1, 0.0)
                pygame.display.update()
                
            #inizia un altro ciclo qunado sto giocando e i cattivi iniziano a scendere
            #codice che mi dice cosa fare quando il giocatore preme queest tasti
                while condizione: # The game loop runs while the game part is playing.
                    score += 1 # Increase score.
                    if score== topScore:
                        windowSurface.blit(sfondoStretchedImage,windowSurfaceRectangle)
                        drawText('YOU WIN!', font, windowSurface, (WINDOWWIDTH / 3)-10, (WINDOWHEIGHT / 3)+30)
                        drawText('NOW', font, windowSurface, (WINDOWWIDTH / 3)+30, (WINDOWHEIGHT / 3)+60)
                        drawText('YOU CAN CONTINUE', font, windowSurface, (WINDOWWIDTH / 3) -80 , (WINDOWHEIGHT / 3)+90)
                        drawText('YOUR GAME', font, windowSurface, (WINDOWWIDTH / 3) -20, (WINDOWHEIGHT / 3) +120)
                        drawText('ROLL THE DIE AGAIN!', font, windowSurface, (WINDOWWIDTH / 3) -100, (WINDOWHEIGHT / 3) +150)
                        pygame.display.update()
                        waitForPlayerToPressKey()
                        dado = random.randint(1,6)
                        numero = numero + dado
                        condizione = False
#                        terminate()
            
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
                        numero=1
                        condizione=False
                        pygame.display.update()
                        waitForPlayerToPressKey()
#                        terminate()
                    #scatta ogni 60 milllisecondi
                    mainClock.tick(FPS)
            #dado = random.randint(1,6)
            #numero = numero + dado                    
            
                # Stop the game and show the "Game Over" screen.
                #stoppo la  musica e riproduco quella della sconfitta
                pygame.mixer.music.stop()
                gameOverSound.play()
                gameOverSound.stop()
                
                
        if numero==2:
            pygame.mixer.music.load('grandcanyon2.wav')
            pygame.mixer.music.play(-1, 0.0)
            sfondo4=pygame.image.load('arida2.jpg')
            sfondoStretchedImage4= pygame.transform.scale(sfondo4, (WINDOWWIDTH, WINDOWHEIGHT))
            windowSurface.blit(sfondoStretchedImage4,windowSurfaceRectangle)
            pygame.display.update()
            #funzione che stampa il testo con il font definito alla riga 84
            drawText('STOP FOR ', font, windowSurface, (WINDOWWIDTH / 3)+10, (WINDOWHEIGHT / 3)+60)
            drawText('A WHILE!', font, windowSurface, (WINDOWWIDTH / 3)+10, (WINDOWHEIGHT / 3)+90)
            pygame.display.update()
            time.sleep(10)
            numero = 5
            #aspetta che il giocatore prema un tasto per iniziare il gioco o per usicre
#            waitForPlayerToPressKey()
#            terminate()
            
        if numero == 3:
            CATTIVOMINSIZE = 100
            CATTIVOMAXSIZE = 200
            BUONOMINSIZE = 100
            BUONOMAXSIZE = 150
            
            #veloctà con cui vengono aggiunti i mostriciattoli che scendono 
            MAX_CATTIVI = 10
            
            removeCattivo = 0
            removeBuono = 0
            cattivoCounter = 0
            buonoCounter = 0
            score = 0
            SCORE = 10
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
            mainClock = pygame.time.Clock()
            cattivi = []
            buoni = []
            
            while True: 
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
                            numero = 2
#                            terminate()
                            gameOverSound.stop()
                            condizione=False
            
            if score >= SCORE:
        #        waitForPlayerToPressKey()
                drawText('YOU WIN!', font, windowSurface, (WINDOWWIDTH / 4), (WINDOWHEIGHT / 4))
                dado = random.randint(1,6)
                numero = 2
                condizione = False
                pygame.display.update()
                waitForPlayerToPressKey()
#                terminate()
                
                
        if numero ==4:
            sfondo2=pygame.image.load('montagna.jpg')
            labirintoStretchedImage=pygame.image.load('labirinto1.gif')
            labirinto=pygame.transform.scale(labirintoStretchedImage, (WINDOWWIDTH, WINDOWHEIGHT))
            sfondoStretchedImage2=pygame.transform.scale(sfondo2,(WINDOWWIDTH, WINDOWHEIGHT))
            playerStretchedImage2 = pygame.image.load('Koda.png')
            playerImage2= pygame.transform.scale(playerStretchedImage2,(60, 60))
            mieleStretchedImage= pygame.image.load('miele.png')
            mieleImage= pygame.transform.scale(mieleStretchedImage, (70, 70))
            PLAYERMOVERATE= 1
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
#                    sound.play()
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
                        drawText('ROLL THE DIE AGAIN!', font, windowSurface, (WINDOWWIDTH / 3) -100, (WINDOWHEIGHT / 3) +150)
                        dado = random.randint(1,6)
                        pygame.display.update()
                        waitForPlayerToPressKey()
                        condizione = False
                        numero=5
#                        terminate()
                        
                mainClock.tick(FPS)
                
        if numero==5:
            backgroundImage5 = pygame.image.load('fuoco.png')
            backgroundStretchedImage5 = pygame.transform.scale(backgroundImage5, (WINDOWWIDTH, WINDOWHEIGHT))
            windowSurface.blit(backgroundStretchedImage5, backgroundStretchedImage5.get_rect())
            pygame.mixer.music.load('vulcano2.wav')
            pygame.mixer.music.play(-1, 0.0)
            gameOverSound = pygame.mixer.Sound('gameover3.wav')
            drawText('FIFTH CHALLENGE: ', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
            drawText('GUESS THE NUMBER!', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3) + 50)
            drawText('Write your name: ', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3)+100)
            pygame.display.update()
            waitForPlayerToPressKey()
            
            windowSurface.blit(backgroundStretchedImage5, backgroundStretchedImage5.get_rect())
            pygame.display.update()
            y=200
            y1=150
            guessesTaken = 0
            myName = textInput(300,300)
            print (myName)
            windowSurface.blit(backgroundStretchedImage5, backgroundStretchedImage5.get_rect())
            pygame.display.update()
            number = random.randint( 1,50)
            drawText('Well, ' + myName + ', I am thinking of a', font, windowSurface, 0, 50)
            drawText('number between 1 and 50', font, windowSurface, 0, 100)
            for guessesTaken in range(6):
                drawText('Take a guess', font, windowSurface, 0, 150)
                guess = textInput(0,y)
                guess = int(guess)
                if guess < number:
                    drawText('Your guess is too low.', font, windowSurface, 0, y1+100)
                if guess > number:
                    drawText('Your guess is too high.', font, windowSurface, 0, y1+100)
                if guess == number:
                    break
                y= y+100
                y1=y1+100
            if guess == number:
                guessesTaken = str(guessesTaken+1)
                windowSurface.blit(backgroundStretchedImage5, backgroundStretchedImage5.get_rect())
                drawText('Good job,' + myName + '! You ', font, windowSurface, 0, 250)
                drawText('guessed my number in ' + guessesTaken + ' guesses !', font, windowSurface, 0, 300)
                pygame.display.update()
                pygame.mixer.music.stop()
                time.sleep(2)
            if guess != number:
                number = str( number )
                windowSurface.blit(backgroundStretchedImage5, backgroundStretchedImage5.get_rect())
                drawText('That\'s too bad. The number I ', font, windowSurface, 0, 250)
                drawText('was thinking of was ' + number + '.', font, windowSurface, 0, 300)
                pygame.mixer.music.stop()
                pygame.display.update()
                gameOverSound.play()
                time.sleep(5)
                numero = 2
                gameOverSound.stop()
                    
#            pygame.quit()
#            sys.exit()
    
                        
                        
        if numero==6:
            pygame.mixer.music.load('oasi3.wav')
            sfondo6=pygame.image.load('oasi4.jpg')
            sfondoStretchedImage6=pygame.transform.scale(sfondo6,(WINDOWWIDTH, WINDOWHEIGHT))
            windowSurface.blit(sfondoStretchedImage6,windowSurfaceRectangle)
            pygame.mixer.music.play(-1, 0.0)
            pygame.display.update()
            #funzione che stampa il testo con il font definito alla riga 84
            drawText('GO TO', font, windowSurface, (WINDOWWIDTH / 3)+50, (WINDOWHEIGHT / 3)+60)
            drawText('ISLAND 5!', font, windowSurface, (WINDOWWIDTH / 3)+20, (WINDOWHEIGHT / 3)+90)
            pygame.display.update()
#            time.sleep(10)
            #aspetta che il giocatore prema un tasto per iniziare il gioco o per usicre
            waitForPlayerToPressKey()
            numero = 5
#            terminate()
            
    
        if numero==7:
            backgroundImage7 = pygame.image.load('foresta.jpg')
            backgroundStretchedImage7 = pygame.transform.scale(backgroundImage7, (WINDOWWIDTH, WINDOWHEIGHT))
            windowSurface.blit(backgroundStretchedImage7, backgroundStretchedImage7.get_rect())
            font = pygame.font.SysFont(None, 48)
            gameOverSound = pygame.mixer.Sound('gameover2.wav')
            pygame.mixer.music.load('foresta2.wav')
            pygame.mixer.music.play(-1, 0.0)
            drawText('LAST CHALLENGE!', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
            pygame.display.update()
            waitForPlayerToPressKey()
            
            windowSurface.blit(backgroundStretchedImage7, backgroundStretchedImage7.get_rect())
            pygame.display.update()
            
            y=350
            y1=100
            guessesTaken = 0
            drawText('First question ', font, windowSurface,0, 50)
            #for guessesTaken in range(1):
            drawText(''' The most you take them, the most you let them behind.''', font, windowSurface, 0, 100)
            drawText(''' Which are?''', font, windowSurface, 0, y1+50)
            drawText('''a. apples''', font, windowSurface, 0, y1+100)
            drawText('''b. time''', font, windowSurface, 0, y1+150)
            drawText('''c. steps ''', font, windowSurface, 0, y1+200)
            guess = textInput(0,y)
            guess = str(guess)
            if guess != 'c' :
                print('a')
                windowSurface.blit(backgroundStretchedImage7, backgroundStretchedImage7.get_rect())
                drawText('No, that is not true', font, windowSurface, 0, y1+100)
                pygame.display.update()
                time.sleep(2)
                numero=6
                pygame.mixer.music.stop()
#                pygame.display.update()
                gameOverSound.play()
                gameOverSound.stop()
                dado = random.randint(1,6)
                numero = 2
                condizione = False
               
            if guess == 'c':
                windowSurface.blit(backgroundStretchedImage7, backgroundStretchedImage7.get_rect())
                drawText('Yes, you are right', font, windowSurface, 0, y1+100)
                pygame.display.update()
                time.sleep(3)
                windowSurface.blit(backgroundStretchedImage7, backgroundStretchedImage7.get_rect())
                pygame.mixer.music.load('foresta2.wav')
                pygame.mixer.music.play(-1, 0.0)
                drawText('Second question ', font, windowSurface,0, 50)
                #for guessesTaken in range(1):
                drawText(''' David\'s father has three sons:''', font, windowSurface, 0, 100)
                drawText('''Brian, Liam and...''', font, windowSurface, 0, y1+50)
                drawText('''a. Luis''', font, windowSurface, 0, y1+100)
                drawText('''b. David''', font, windowSurface, 0, y1+150)
                drawText('''c. Gabriel ''', font, windowSurface, 0, y1+200)
                guess = textInput(0,y)
                guess = str(guess)
            
                if guess != 'b' :
                    windowSurface.blit(backgroundStretchedImage7, backgroundStretchedImage7.get_rect())
                    drawText('No, that is not true', font, windowSurface, 0, y1+100)
                    pygame.display.update()
                    pygame.mixer.music.stop()
                    time.sleep(2)
                    numero=6
                    pygame.display.update()
                    gameOverSound.play()
                    gameOverSound.stop()
                    dado = random.randint(1,6)
                    numero = 2
                    condizione = False
    #                pygame.quit()
    #                sys.exit()
                if guess== 'b':
                    windowSurface.blit(backgroundStretchedImage7, backgroundStretchedImage7.get_rect())
                    drawText('Yes, you are right', font, windowSurface, 0, y1+100)
                    pygame.display.update()
                    time.sleep(3)
                    windowSurface.blit(backgroundStretchedImage7, backgroundStretchedImage7.get_rect())
                    pygame.mixer.music.load('foresta2.wav')
                    pygame.mixer.music.play(-1, 0.0)
                    drawText('Third question ', font, windowSurface,0, 50)
                    #for guessesTaken in range(1):
                    drawText('''What belongs to you, but''', font, windowSurface, 0, 100)
                    drawText(''' other people use it more than you do?''', font, windowSurface, 0, y1+50)
                    drawText('''a. Your name''', font, windowSurface, 0, y1+100)
                    drawText('''b. Your hair''', font, windowSurface, 0, y1+150)
                    drawText('''c. Clothes ''', font, windowSurface, 0, y1+200)
                    guess = textInput(0,y)
                    guess = str(guess)
            
                    if guess != 'a' :
                        windowSurface.blit(backgroundStretchedImage7, backgroundStretchedImage7.get_rect())
                        drawText('No, that is not true', font, windowSurface, 0, y1+100)
                        pygame.display.update()
                        time.sleep(2)
                        numero=6
                        pygame.mixer.music.stop()
                        pygame.display.update()
                        gameOverSound.play()
                        gameOverSound.stop()
                        dado = random.randint(1,6)
                        numero = 2
                        condizione = False
                        #pygame.quit()
                        #sys.exit()
                    if guess== 'a':
                        windowSurface.blit(backgroundStretchedImage7, backgroundStretchedImage7.get_rect())
                        drawText('Yes, you are right', font, windowSurface, 0, y1+100)
                        pygame.display.update()
                        time.sleep(3)
                        condizione=False
                        numero = 8
        if numero == 8:
            backgroundfinale = pygame.image.load('tesorofinale.jpg')
            backgroundStretchedfinale = pygame.transform.scale(backgroundfinale, (WINDOWWIDTH, WINDOWHEIGHT))
            windowSurface.blit(backgroundStretchedfinale, backgroundStretchedfinale.get_rect())              
                        
        
                    
                
              
            
            
            
