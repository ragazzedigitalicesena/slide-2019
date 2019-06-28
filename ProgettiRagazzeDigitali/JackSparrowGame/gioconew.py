import pygame , sys, random
from pygame.locals import *

WINDOWWIDTH = 1100
WINDOWHEIGHT = 800
TEXTCOLOR = (255, 255, 255)
BACKGROUNDCOLOR = (255, 255, 255)
FPS = 60

BADDIESIZE = 20
GOODIESIZE = 20
BADDIESPEED = 3
GOODIESPEED = 5
ADDNEWBADDIERATE = 6
ADDNEWGOODIERATE = 6
PLAYERMOVERATE = 5
MOVE_SPEED = 5

def terminate ():
    pygame.quit ()
    sys.exit ()

def waitForPlayerToPressKey ():
    while True :
        for event in pygame.event.get ():
            if event.type == QUIT :
                terminate ()
            if event.type == KEYDOWN :
                if event.key == K_ESCAPE :
                    terminate ()
                return

def playerHasHitBaddie ( playerRect , baddies ) :
    for b in baddies :
        if playerRect.colliderect (b ['rect '] ) :
            return True
    return False

def playerHasHitGoodie ( playerRect, goodies ) :
    for g in goodies:
        if playerRect.colliderect (g ['score += 1'] ) :
            return True
    return True
            
def drawText (text , font , surface , x, y) :
    textobj = font.render (text , 1, TEXTCOLOR )
    textrect = textobj.get_rect ()
    textrect.topleft = ( x, y )
    surface.blit ( textobj, textrect )
    
pygame.init ()
mainClock = pygame.time.Clock ()
windowSurface = pygame.display.set_mode (( WINDOWWIDTH , WINDOWHEIGHT ))
pygame.display.set_caption ('FINDING THE TREASURE')
pygame.mouse.set_visible ( True )


font = pygame.font.SysFont ('harrington' , 70)

X_POSITION = 0
Y_POSITION = 0
PLAYER_WIDTH = 200
PLAYER_HEIGHT = 200

playerRect = pygame.Rect(X_POSITION, Y_POSITION, PLAYER_WIDTH , PLAYER_HEIGHT)
playerImage = pygame.image.load ('JackSparrow.png')
playerStretchedimage =  pygame.transform.scale (playerImage, (150, 200))

baddieImage = pygame.image.load ('avvoltoio.png')
goodieImage = pygame.image.load ('moneta.png')

mainClock = pygame.time.Clock()

GOODIE_WIDTH = 55
GOODIE_HEIGHT = 60

GOODIE_WIDTH = 55
GOODIE_HEIGHT = 60

BADDIE_WIDTH = 60
BADDIE_HEIGHT = 70

goodies = []
baddies = []

MAX_GOODIES = 25
MAX_BADDIES = 20

for i in range(MAX_GOODIES):
    goodieRect = pygame.Rect(random.randint(0, WINDOWWIDTH), 0, GOODIE_WIDTH, GOODIE_HEIGHT)
    goodies.append(goodieRect)
for h in range(MAX_BADDIES):
    baddieRect =  pygame.Rect (random.randint(0,WINDOWWIDTH), 0, BADDIE_WIDTH, BADDIE_HEIGHT)
    baddies.append(baddieRect)
    
backgroundImage = pygame.image.load ('oceanoconisole.jpg')
#sfondo inizio
windowSurface.fill ( BACKGROUNDCOLOR )

backgroundImage = pygame.image.load ('oceanoconisole.jpg')
backgroundStretchedImage = pygame.transform.scale (backgroundImage, (WINDOWWIDTH, WINDOWHEIGHT))
windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect() )

baddieStretchedImage = pygame.transform.scale (baddieImage, (60, 70))

goodieStretchedImage = pygame.transform.scale (goodieImage, (GOODIE_WIDTH, GOODIE_HEIGHT))

drawText ('FINDING THE TREASURE', font , windowSurface ,( WINDOWWIDTH / 7) , ( WINDOWHEIGHT / 15))
pygame.display.update ()
waitForPlayerToPressKey ()
backgroundImage = pygame.image.load ('primogioco.png')
backgroundStretchedImage = pygame.transform.scale (backgroundImage, (WINDOWWIDTH, WINDOWHEIGHT))
windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect() )
pygame.display.update ()
waitForPlayerToPressKey ()
backgroundImage = pygame.image.load ('jackparla2.jpg')
backgroundStretchedImage = pygame.transform.scale (backgroundImage, (WINDOWWIDTH, WINDOWHEIGHT))
windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect() )
pygame.display.update ()
waitForPlayerToPressKey ()
             
#inizio primo gioco

topScore = 0
#nuovo inizio partita
while True:
    # Set up the start of the game.
    score = 0
    maxScore = 500
    playerRect.bottomleft = (WINDOWHEIGHT, 800)
#    playerRect.topleft = ( WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    baddieAddCounter = 0
    goodieAddCounter = 0
#==============================================================================
#     for b in baddies:
#         windowSurface.blit(b['surface'], b['rect'])
#     for g in goodies:
#         windowSurface.blit(g['surface'], g['rect'])
#     # pygame.mixer.music.play (-1, 0.0) 
#==============================================================================

    #svolgimento partita
    while True:        
    #    if playerHasHitGoodie ( playerRect , goodies ) :
    #        score += 10
    #    while playerHasHitBaddie ( playerRect , baddies ) :
    #        break
        for event in pygame.event.get () :
            if event.type == QUIT:
                terminate ()
            if event.type == KEYDOWN:    
                if event.key == K_LEFT or event.key == K_a :
                        moveRight = False
                        moveLeft = True
                if event.key == K_RIGHT or event.key == K_d:
                        moveLeft = False
                        moveRight = True
                    
        # Move the player around.
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
        if moveRight and playerRect.right < WINDOWWIDTH:
            playerRect.move_ip(PLAYERMOVERATE, 0)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * PLAYERMOVERATE)
        if moveDown and playerRect.bottom < WINDOWHEIGHT:
            playerRect.move_ip(0, PLAYERMOVERATE)
    
 
        print('x:', playerRect.x, 'y:', playerRect.y)

        windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect() )

        windowSurface.blit(baddieStretchedImage,baddieStretchedImage.get_rect() )
        
        for g in range(random.randint(0, len(goodies))):
            goodies[g].top = goodies[g].top + MOVE_SPEED
            windowSurface.blit(goodieStretchedImage,goodies[g])
         
        for b in range (random.randint(0, len(baddies))):
            baddies[b].top = baddies[b] + MOVE_SPEED
            windowSurface.blit (baddieStretchedImage, baddies[g])
        windowSurface.blit( playerStretchedimage , playerRect )
        
        pygame.display.update ()
        mainClock.tick(40)
    
    
    
    
    
    
    
    
#    
#    
##secondo gioco    
#HANGMAN_PICS = ['''
#  +---+
#      |
#      |
#      |
#     ===''', '''
#  +---+
#  O   |
#      |
#      |
#     ===''', '''
#  +---+
#  O   |
#  |   |
#      |
#     ===''', '''
#  +---+
#  O   |
# /|   |
#      |
#     ===''', '''
#  +---+
#  O   |
# /|\  |
#      |
#     ===''', '''
#  +---+
#  O   |
# /|\  |
# /    |
#     ===''', '''
#  +---+
#  O   |
# /|\  |
# / \  |
#     ===''']
#
#import random
#missedLetters = ''
#correctLetters = ''
#wordsString = 'survivor'
#words = wordsString.split()
#
#def getRandomWord(wordList):
#    wordIndex = random.randint (0, len(words) -1)
#    return wordList[wordIndex]
#
#secretWord = getRandomWord(words)
#
#def displayBoard(missedLetters, correctLetters, secretWord):
#
#    numberOfMissedLetters = len(missedLetters)
#    print(HANGMAN_PICS[numberOfMissedLetters])
#    print('Lettere sbagliate' + missedLetters)
#
#    guessedLetters = []
#    for i in range(len(secretWord)) :
#        if secretWord[i] in correctLetters:
#            guessedLetters.append(secretWord[i])
#        else:
#            guessedLetters.append('_')
#    print(guessedLetters)
#
#def getGuess(alreadyGuessed):
#   
#    while True:
#        print('Guess a letter.')
#        guess = input()
#        guess = guess.lower()
#        if len(guess) != 1:
#            print('Please enter a single letter.')
#        elif guess in alreadyGuessed:
#            print('You have already guessed that letter. Choose again.')
#        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
#            print('Please enter a LETTER.')
#        else:
#            return guess
#
#
#print('H A N G M A N')
#
#gameIsDone = False
#
#play = True
#
#while play:
#    displayBoard(missedLetters, correctLetters, secretWord)
#
#
#    guess = getGuess(missedLetters + correctLetters)
#
#    if guess in secretWord:
#        correctLetters = correctLetters + guess
#
#        foundAllLetters = True
#        for i in range(len(secretWord)):
#            if secretWord[i] not in correctLetters:
#                foundAllLetters = False
#                break
#        if foundAllLetters:
#            print('Bravo! Hai trovato la combinazione per aprire il tesoro! ' + secretWord + '! Il tesoro è tuo ora!')
#            gameIsDone = True
#    else:
#        missedLetters = missedLetters + guess
#
#        if len(missedLetters) == len( HANGMAN_PICS ) - 1:
#            displayBoard(missedLetters, correctLetters, secretWord)
#            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
#            gameIsDone = True
#            
#playAgain = 'yes'
#if gameIsDone:
#    if playAgain():
#        missedLetters = ''
#        correctLetters = ''
#        gameIsDone = False
#pygame.display.update ()