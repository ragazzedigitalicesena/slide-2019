import pygame, random, sys
from pygame.locals import *

WINDOWWIDTH = 600
WINDOWHEIGHT = 600
TEXTCOLOR = (0, 0, 0)
BACKGROUNDCOLOR = (255, 255, 255)
FPS = 20     #frame al secondo
BADDIEMINSIZE = 10
BADDIEMAXSIZE = 40
BADDIEMINSPEED = 1
BADDIEMAXSPEED = 8
ADDNEWBADDIERATE = 6
PLAYERMOVERATE = 5 #di quanto si muove il giocatore (tieni un valore basso)

#per uscire dal gioco
def terminate():
    pygame.quit()
    sys.exit()
#aspetto che l'utente prema un pulsante
def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # tato ESC 
                    terminate()
                return

#baddies è una lista  
def playerHasHitBaddie(playerRect, baddies):
    for b in baddies: #per ogni cattivo dentro la lista
        if playerRect.colliderect(b['rect']): # se l'area che occupa il giocatore è la stessa di un cattivo ..
#        b rect modo per prendere l'area che il cattivo sta usando 
            return True
    return False        # se non tocca mai i cattivi restituisco hai vinto 

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR) #crea il testo
    textrect = textobj.get_rect() #gli dà un rettangolo
    textrect.topleft = (x, y) #lo posiziona
    surface.blit(textobj, textrect) #lo disegna dove gli abbiamo detto

# Set up pygame, the window, and the mouse cursor.
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Dodger')   #titoletto della finestra (in alto)
pygame.mouse.set_visible(False) #prendi ilmouse e quando è sulla finestra nascondilo

# Set up the fonts.
font = pygame.font.SysFont(None, 48)

# Set up sounds. 1 creo una variabile che salva la musica che voglio riprodurre ad un certo punto del gioco
gameOverSound = pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('background.mid')   # carica questa musica

# Set up images.
playerImage = pygame.image.load('player.png')
playerRect = playerImage.get_rect()
baddieImage = pygame.image.load('baddie.png')

# Show the "Start" screen.
windowSurface.fill(BACKGROUNDCOLOR)
drawText('Dodger', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))  # vedi funzione sopra (stampa il testo)
drawText('Press a key to start.', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3) + 50)
pygame.display.update()
waitForPlayerToPressKey() # richiamo funzione (aspetto che il giocatore prema un pulsante )

topScore = 0     # visualizza il punteggio piu alto di tutte le partite giocate 
while True: # ogni volta che l'utente ricomincia a giocare
    # Set up the start of the game.
    baddies = [] #lista
    score = 0 #punteggio singola partita
    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)  #giocatore al centro nella parte inferiore
    moveLeft = moveRight = moveUp = moveDown = False # mi servono per dire di spostare il personaggio 
    reverseCheat = slowCheat = False # cattivi al contrario o piu lentamente
    baddieAddCounter = 0  # aggiunge un nuovo cattivo quanto baddieadd arriva a 6 
    pygame.mixer.music.play(-1, 0.0)   # parte la  musica (in secondi)
    

    while True: # The game loop runs while the game part is playing.
        score += 1 #  il punteggio aumenta ad ogni ciclo
#  codice che dice a python cosa fare quando il giocatore preme i tasti 
        for event in pygame.event.get(): # ogni vlta che succede qualcosa 
            if event.type == QUIT: # se clicca la x 
                terminate()

            if event.type == KEYDOWN: #se il giocatore preme un tasto
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

            if event.type == KEYUP: # se il giocatore rilascia un tasto 
                if event.key == K_z:
                    reverseCheat = False      #(vedi riga 92)
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

            if event.type == MOUSEMOTION:
                # If the mouse moves, move the player where to the cursor.
                playerRect.centerx = event.pos[0]
                playerRect.centery = event.pos[1]
        # Add new baddies at the top of the screen, if needed.
        # aggiungere nuovi cattivi (se non vanno piano e non vanno al contrario)
        if not reverseCheat and not slowCheat:
            baddieAddCounter += 1
        if baddieAddCounter == ADDNEWBADDIERATE:
            baddieAddCounter = 0
            baddieSize = random.randint(BADDIEMINSIZE, BADDIEMAXSIZE)  # dimensione random
            newBaddie = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - baddieSize), 0 - baddieSize, baddieSize, baddieSize), #
                        'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                        'surface':pygame.transform.scale(baddieImage, (baddieSize, baddieSize)),
                        }

            baddies.append(newBaddie)

        # Move the player around.
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
        if moveRight and playerRect.right < WINDOWWIDTH:
            playerRect.move_ip(PLAYERMOVERATE, 0)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * PLAYERMOVERATE)
        if moveDown and playerRect.bottom < WINDOWHEIGHT:
            playerRect.move_ip(0, PLAYERMOVERATE)

        # Move the baddies down. per tutti i cattivi nella lista
        for b in baddies:
            if not reverseCheat and not slowCheat:
                b['rect'].move_ip(0, b['speed'])
            elif reverseCheat:
                b['rect'].move_ip(0, -5) # vado verso l'alto per salire uso le aktezze negative
            elif slowCheat:
                b['rect'].move_ip(0, 1)

        # Delete baddies that have fallen past the bottom.
        for b in baddies[:]:     # quando un cattivo esce dalla finestra 
            if b['rect'].top > WINDOWHEIGHT:
                baddies.remove(b)   # rimuovo dalla lista

        # sfondo
        windowSurface.fill(BACKGROUNDCOLOR)

        # Draw the score and top score.
        scoreText= 'Score: ',score
        topScoreText= 'top score', topScore          
        drawText(scoreText, font, windowSurface, 10, 0)  # 10 e 0 = posizione 
        drawText(topScoreText, font, windowSurface, 10, 40)

        # Draw the player's rectangle. disegno il giocatore b
        windowSurface.blit(playerImage, playerRect)

        # Draw each baddie. per ogni cattivo in lista disegno quel cattivo 
        for b in baddies:
            windowSurface.blit(b['surface'], b['rect'])

        pygame.display.update()

        # Check if any of the baddies have hit the player.
        if playerHasHitBaddie(playerRect, baddies):
            if score > topScore:
                topScore = score # set new top score
            break

        mainClock.tick(FPS)

    # Stop the game and show the "Game Over" screen.
    pygame.mixer.music.stop()
    gameOverSound.play() # musica di sconfitta

    drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
    drawText('Press a key to play again.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
    pygame.display.update() #aggiorno la schermata 
    waitForPlayerToPressKey()

    gameOverSound.stop()
