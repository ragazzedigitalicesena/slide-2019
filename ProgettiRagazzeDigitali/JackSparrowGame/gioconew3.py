#import pygame , sys, random, time
#rom pygame.locals import *
#
#WINDOWWIDTH = 1100
#WINDOWHEIGHT = 800
#TEXTCOLOR = (255, 255, 255)
#BACKGROUNDCOLOR = (255, 255, 255)
#FPS = 60
#
#BADDIESIZE = 50
#GOODIESIZE = 20
#BADDIESPEED = 3
#GOODIESPEED = 5
#ADDNEWBADDIERATE = 6
#ADDNEWGOODIERATE = 6
#PLAYERMOVERATE = 5
#MOVE_SPEED = 3
#
#def terminate ():
#    pygame.quit ()
#    sys.exit ()
#
#def waitForPlayerToPressKey ():
#    while True :
#        for event in pygame.event.get ():
#            if event.type == QUIT :
#                terminate ()
#            if event.type == KEYDOWN :
#                if event.key == K_ESCAPE :
#                    terminate ()
#                return
#
#            
#def drawText (text , font , surface , x, y) :
#    textobj = font.render(text , 1, TEXTCOLOR )
#    textrect = textobj.get_rect ()
#    textrect.topleft = ( x, y )
#    surface.blit ( textobj, textrect )
#    
#
##def gioco 2
##def printIntro():
##    drawText ('Scegli una buca e inizia a scavare.', font , windowSurface ,( WINDOWWIDTH / 7) , ( WINDOWHEIGHT / 15))
#
##def playerChoice():
##   for event in pygame.event.get () :
##     if event.type == MOUSEBUTTONDOWN:
##        
##        xRect = pygame.Rect(350, 440, 10,10)
##        if xRect.collidepoint(pygame.mouse.get_pos()):
##            return True
##        else:
##            return False
##
##def printChoice(choice):
##    print('Guarda! Hai toccato una cosa con la tua pala!')
##    
##friendlyC = 2
##        
#
#pygame.init ()
#mainClock = pygame.time.Clock ()
#windowSurface = pygame.display.set_mode (( WINDOWWIDTH , WINDOWHEIGHT ))
#pygame.display.set_caption ('FINDING THE TREASURE')
#pygame.mouse.set_visible ( True )
#
#
#font = pygame.font.SysFont ('harrington' , 70)
#
#X_POSITION = 0
#Y_POSITION = 0
#PLAYER_WIDTH = 200
#PLAYER_HEIGHT = 200
#
#playerRect = pygame.Rect(X_POSITION, Y_POSITION, PLAYER_WIDTH , PLAYER_HEIGHT)
#playerImage = pygame.image.load ('JackSparrow.png')
#playerStretchedimage =  pygame.transform.scale (playerImage, (150, 200))
#
#baddieImage = pygame.image.load ('avvoltoio.png')
#goodieImage = pygame.image.load ('moneta.png')
#
#mainClock = pygame.time.Clock()
#
#GOODIESIZE = 55
#BADDIESIZE = 70
#
#goodies = []
#baddies = []
#
#ADDNEWGOODIERATE = 20
#ADDNEWBADDIERATE = 20
#
#for i in range(30):
#    goodieRect = pygame.Rect(random.randint(0, WINDOWWIDTH), 0, GOODIESIZE, GOODIESIZE)
#    goodies.append(goodieRect)
#for h in range(5):
#    baddieRect =  pygame.Rect (random.randint(0,WINDOWWIDTH), 0, BADDIESIZE, BADDIESIZE)
#    baddies.append(baddieRect)
#    
#backgroundImage = pygame.image.load ('oceanoconisole.jpg')
##sfondo inizio
#windowSurface.fill ( BACKGROUNDCOLOR )
#
#backgroundImage = pygame.image.load ('oceanoconisole.jpg')
#backgroundStretchedImage = pygame.transform.scale (backgroundImage, (WINDOWWIDTH, WINDOWHEIGHT))
#windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect() )
#
#baddieStretchedImage = pygame.transform.scale (baddieImage, (BADDIESIZE, BADDIESIZE))
#
#goodieStretchedImage = pygame.transform.scale (goodieImage, (GOODIESIZE, GOODIESIZE))
#
#drawText ('FINDING THE TREASURE', font , windowSurface ,( WINDOWWIDTH / 7) , ( WINDOWHEIGHT / 15))
#pygame.display.update ()
#waitForPlayerToPressKey ()
#backgroundImage = pygame.image.load ('primogioco.png')
#backgroundStretchedImage = pygame.transform.scale (backgroundImage, (WINDOWWIDTH, WINDOWHEIGHT))
#windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect() )
#pygame.display.update ()
#waitForPlayerToPressKey ()
#backgroundImage = pygame.image.load ('jackparla2.jpg')
#backgroundStretchedImage = pygame.transform.scale (backgroundImage, (WINDOWWIDTH, WINDOWHEIGHT))
#windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect() )
#pygame.display.update ()
#waitForPlayerToPressKey ()
#backgroundImage = pygame.image.load ('spiaggia2.jpg')
#backgroundStretchedImage = pygame.transform.scale (backgroundImage, (WINDOWWIDTH, WINDOWHEIGHT))
#windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect() )
#
##inizio primo gioco
#
#level1 = True
#
##nuovo inizio partita
#while True:
#    # Set up the start of the game.
#    score = 0
#    maxScore = 25
#    playerRect.bottomleft = (WINDOWHEIGHT, 800)
##    playerRect.topleft = ( WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
#    moveLeft = moveRight = moveUp = moveDown = False
#    baddieAddCounter = 0
#    goodieAddCounter = 0
##==============================================================================
##     for b in baddies:
##         windowSurface.blit(b['surface'], b['rect'])
##     for g in goodies:
##         windowSurface.blit(g['surface'], g['rect'])
##     # pygame.mixer.music.play (-1, 0.0) 
##==============================================================================
#
#    #svolgimento partita
#    while level1:
#      
#        for event in pygame.event.get () :
#            if event.type == QUIT:
#                terminate ()
#            if event.type == KEYDOWN:    
#                if event.key == K_LEFT or event.key == K_a :
#                        moveRight = False
#                        moveLeft = True
#                if event.key == K_RIGHT or event.key == K_d:
#                        moveLeft = False
#                        moveRight = True
#            if event.type == KEYUP:
#                if event.key == K_ESCAPE:
#                    pygame.quit()
#                    sys.exit()
#                if event.key == K_LEFT or event.key == K_a:
#                    moveLeft = False
#                if event.key == K_RIGHT or event.key == K_d:
#                    moveRight = False
#                    
#        # Move the player around.
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
#         #print('x:', playerRect.x, 'y:', playerRect.y)
#       
#        if score <= maxScore:
#            for g in goodies:
#                g.top = g.top + random.randint(1, MOVE_SPEED)
#                if playerRect.colliderect(g):
#                    goodies.remove(g)
#                    score += 25
#                    
#            for b in baddies:
#                b.top = b.top + random.randint(1, MOVE_SPEED)
#                if playerRect.colliderect(b):
#                    baddies.remove(b)
#                    score -= 10
#        else:
#            level1 = False
#            
#
#        windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect() )
#
#        
#        drawText('Score: %s' % (score), font, windowSurface, 10, 0)
#
#
#        windowSurface.blit( playerStretchedimage , playerRect )
#    
#    
#        for g in goodies:
#            windowSurface.blit( goodieStretchedImage , g )
#            
#        for b in baddies:
#            windowSurface.blit( baddieStretchedImage , b )
#            
#        pygame.display.update ()
#        
#        
#        
#        
##fine primo livello  
#    backgroundImage = pygame.image.load ('secondogioco.png')
#    backgroundStretchedImage = pygame.transform.scale (backgroundImage, (WINDOWWIDTH, WINDOWHEIGHT))
#    windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect() )
#    pygame.display.update ()
#    waitForPlayerToPressKey ()
#    
#    backgroundImage = pygame.image.load ('jackparla3.jpg')
#    backgroundStretchedImage = pygame.transform.scale (backgroundImage, (WINDOWWIDTH, WINDOWHEIGHT))
#    windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect() )
#    pygame.display.update ()
#    waitForPlayerToPressKey () 
#    
#    backgroundImage = pygame.image.load ('sceltasecondogioco.jpg')
#    backgroundStretchedImage = pygame.transform.scale (backgroundImage, (WINDOWWIDTH, WINDOWHEIGHT))
#    windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect() )
#    pygame.display.update ()
#   # waitForPlayerToPressKey () 
##secondo gioco
#
#    playAgain = 'si'
#    pos = (0,0)
#    backgroundImage = pygame.image.load ('sceltasecondogiocofail1.jpg')
#    backgroundStretchedImage1 = pygame.transform.scale (backgroundImage, (WINDOWWIDTH, WINDOWHEIGHT))
#   
#    backgroundImage = pygame.image.load ('sceltasecondogiocoforziere.jpg')
#    backgroundStretchedImage2 = pygame.transform.scale (backgroundImage, (WINDOWWIDTH, WINDOWHEIGHT))
#    
#    backgroundImage = pygame.image.load ('sceltasecondogiocofail3.jpg')
#    backgroundStretchedImage3 = pygame.transform.scale (backgroundImage, (WINDOWWIDTH, WINDOWHEIGHT))
#   
#
#    while playAgain == 'si':
#        
#        x1Rect = pygame.Rect(324, 436, 20, 20)
#        x2Rect = pygame.Rect(643, 461, 20, 20)
#        x3Rect = pygame.Rect(1000, 615, 20, 20)
#       
#        for event in pygame.event.get () :
#            if event.type == MOUSEBUTTONDOWN:
#               pos = pygame.mouse.get_pos()
#               print(pos)
#               if x1Rect.collidepoint(pos):
#                   windowSurface.blit(backgroundStretchedImage1, backgroundStretchedImage.get_rect() )
#                    
#               if x2Rect.collidepoint(pos):
#                    windowSurface.blit(backgroundStretchedImage2, backgroundStretchedImage.get_rect() )
#                    playAgain = 'no'
#                    waitForPlayerToPressKey ()
#               if x3Rect.collidepoint(pos):
#                    windowSurface.blit(backgroundStretchedImage3, backgroundStretchedImage.get_rect() )
#                    
#        pygame.display.update ()
#       # time.sleep(5)                    
#        
#        
#     #gioco3  
#    backgroundImage = pygame.image.load ('terzogioco.png')
#    backgroundStretchedImage = pygame.transform.scale (backgroundImage, (WINDOWWIDTH, WINDOWHEIGHT))
#    windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect() )
#    pygame.display.update ()
#    waitForPlayerToPressKey ()
#    backgroundImage = pygame.image.load ('jackparla4.jpg')
#    backgroundStretchedImage = pygame.transform.scale (backgroundImage, (WINDOWWIDTH, WINDOWHEIGHT))
#    windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect() )
#    pygame.display.update ()
#    waitForPlayerToPressKey ()
#            
#            
            
#        time.sleep(2)
#    
#        friendlyCave = random.randint(1,2)
#        check(answer, friendlyCave)
#    
#        print('Vuoi riprovare?')
#        playAgain = input()
#terzo gioco

windowSurface = pygame . display . set_mode (( WINDOW_WIDTH ,WINDOW_HEIGHT ) , 0 , 32)

    
HANGMAN_PICS = [omino1, omino2, omino3, omino4, omino5, omino6, omino7]

import random
missedLetters = ''
correctLetters = ''
wordsString = 'survivor'
words = wordsString.split()

def drawText (text , font , surface , x, y) :
    textobj = font.render(text , 1, TEXTCOLOR )
    textrect = textobj.get_rect ()
    textrect.topleft = ( x, y )
    surface.blit ( textobj, textrect )

def getRandomWord(wordList):
    wordIndex = random.randint (0, len(words) -1)
    return wordList[wordIndex]

secretWord = getRandomWord(words)

def displayBoard(missedLetters, correctLetters, secretWord):

    numberOfMissedLetters = len(missedLetters)
    print(HANGMAN_PICS[numberOfMissedLetters])
    print('Lettere sbagliate:  ' + missedLetters)

    guessedLetters = []
    for i in range(len(secretWord)) :
        if secretWord[i] in correctLetters:
            guessedLetters.append(secretWord[i])
        else:
            guessedLetters.append('_')
    drawText(guessedLetters, None, windowSurface, 100, 100)

def getGuess(alreadyGuessed):
   
    while True:
        print('Indovina una lettera.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Inserisci una sola lettera.')
        elif guess in alreadyGuessed:
            print('Hai già indovinato questa lettera.Scegline una diversa.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Per favore inserisci una lettera.')
        else:
            return guess


print('H A N G M A N')

gameIsDone = False

play = True

while play:
    displayBoard(missedLetters, correctLetters, secretWord)


    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Bravo! Hai trovato la combinazione per aprire il tesoro! ' + secretWord + '! Il tesoro è tuo ora!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len( HANGMAN_PICS ) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('Hai finito le possibilità! ' + str(len(missedLetters)) + ' lettere sbagliate e ' + str(len(correctLetters)) + ' lettere corrette, la parola era"' + secretWord + 'survivor')
            gameIsDone = True
            

pygame.display.update ()