import pygame , sys, random, time
from pygame.locals import *
import pygame_textinput

pygame.init()


pygame.mixer.music.load('pirates.mp3')
pygame.mixer.music.play(-1, 0.0)

WINDOWWIDTH = 1100
WINDOWHEIGHT = 800
TEXTCOLOR = (255, 255, 255)
BACKGROUNDCOLOR = (255, 255, 255)
FPS = 40

BADDIESIZE = 50
GOODIESIZE = 20
BADDIESPEED = 3
GOODIESPEED = 4
ADDNEWBADDIERATE = 4
ADDNEWGOODIERATE = 4
PLAYERMOVERATE = 5
MOVE_SPEED = 2

#pygame.mixer.music.load('background.mid') 

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

            
def drawText (text , font , surface , x, y) :
    textobj = font.render(text , 1, TEXTCOLOR )
    textrect = textobj.get_rect ()
    textrect.topleft = ( x, y )
    surface.blit ( textobj, textrect )
    
    
    
    


#def gioco 2
#def printIntro():
#    drawText ('Scegli una buca e inizia a scavare.', font , windowSurface ,( WINDOWWIDTH / 7) , ( WINDOWHEIGHT / 15))

#def playerChoice():
#   for event in pygame.event.get () :
#     if event.type == MOUSEBUTTONDOWN:
#        
#        xRect = pygame.Rect(350, 440, 10,10)
#        if xRect.collidepoint(pygame.mouse.get_pos()):
#            return True
#        else:
#            return False
#
#def printChoice(choice):
#    print('Guarda! Hai toccato una cosa con la tua pala!')
#    
#friendlyC = 2
#        

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

GOODIESIZE = 55
BADDIESIZE = 90

goodies = []
baddies = []

ADDNEWGOODIERATE = 15
ADDNEWBADDIERATE = 15

for i in range(65):
    goodieRect = pygame.Rect(random.randint(0, WINDOWWIDTH), random.randint(-1000, 0), GOODIESIZE, GOODIESIZE)
    goodies.append(goodieRect)
for h in range(45):
    baddieRect =  pygame.Rect (random.randint(0,WINDOWWIDTH),  random.randint(-1000, 0), BADDIESIZE, BADDIESIZE)
    baddies.append(baddieRect)
    
backgroundImage = pygame.image.load ('oceanoconisole.jpg')
#sfondo inizio
windowSurface.fill ( BACKGROUNDCOLOR )

backgroundImage = pygame.image.load ('oceanoconisole.jpg')
backgroundStretchedImage = pygame.transform.scale (backgroundImage, (WINDOWWIDTH, WINDOWHEIGHT))
windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect() )

baddieStretchedImage = pygame.transform.scale (baddieImage, (BADDIESIZE, BADDIESIZE))

goodieStretchedImage = pygame.transform.scale (goodieImage, (GOODIESIZE, GOODIESIZE))

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
backgroundImage = pygame.image.load ('spiaggia2.jpg')
backgroundStretchedImage = pygame.transform.scale (backgroundImage, (WINDOWWIDTH, WINDOWHEIGHT))
windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect() )

#inizio primo gioco

level1 = True
level2 = True

#nuovo inizio partita
while level2:
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
    while level1:
      
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
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_LEFT or event.key == K_a:
                    moveLeft = False
                if event.key == K_RIGHT or event.key == K_d:
                    moveRight = False
                    
        # Move the player around.
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
        if moveRight and playerRect.right < WINDOWWIDTH:
            playerRect.move_ip(PLAYERMOVERATE, 0)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * PLAYERMOVERATE)
        if moveDown and playerRect.bottom < WINDOWHEIGHT:
            playerRect.move_ip(0, PLAYERMOVERATE)
        
        
         #print('x:', playerRect.x, 'y:', playerRect.y)
       
        if score <= maxScore:
            for g in goodies:
                g.top = g.top + random.randint(1, GOODIESPEED)
                if playerRect.colliderect(g):
                    goodies.remove(g)
                    score += 25
                    
            for b in baddies:
                b.top = b.top + random.randint(1, BADDIESPEED)
                if playerRect.colliderect(b):
                    baddies.remove(b)
                    score -= 5
        else:
            level1 = False
            time.sleep(1)  
            

        windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect() )

        
        drawText('Score: %s' % (score), font, windowSurface, 10, 0)


        windowSurface.blit( playerStretchedimage , playerRect )
    
    
        for g in goodies:
            windowSurface.blit( goodieStretchedImage , g )
            
        for b in baddies:
            windowSurface.blit( baddieStretchedImage , b )
            
        pygame.display.update ()
        
        
        
        
#fine primo livello

    backgroundImage = pygame.image.load ('secondogioco.png')
    backgroundStretchedImage = pygame.transform.scale (backgroundImage, (WINDOWWIDTH, WINDOWHEIGHT))
    windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect() )
    pygame.display.update ()
    waitForPlayerToPressKey ()
    
    backgroundImage = pygame.image.load ('jackparla3.jpg')
    backgroundStretchedImage = pygame.transform.scale (backgroundImage, (WINDOWWIDTH, WINDOWHEIGHT))
    windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect() )
    pygame.display.update ()
    waitForPlayerToPressKey () 
    
    backgroundImage = pygame.image.load ('sceltasecondogioco.jpg')
    backgroundStretchedImage = pygame.transform.scale (backgroundImage, (WINDOWWIDTH, WINDOWHEIGHT))
    windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect() )
    pygame.display.update ()
    #waitForPlayerToPressKey () 
#secondo gioco

    playAgain = 'si'
    pos = (0,0)
    backgroundImage = pygame.image.load ('sceltasecondogiocofail1.jpg')
    backgroundStretchedImage1 = pygame.transform.scale (backgroundImage, (WINDOWWIDTH, WINDOWHEIGHT))
   
    backgroundImage = pygame.image.load ('sceltasecondogiocoforziere.jpg')
    backgroundStretchedImage2 = pygame.transform.scale (backgroundImage, (WINDOWWIDTH, WINDOWHEIGHT))
    
    backgroundImage = pygame.image.load ('sceltasecondogiocofail3.jpg')
    backgroundStretchedImage3 = pygame.transform.scale (backgroundImage, (WINDOWWIDTH, WINDOWHEIGHT))
   

    while playAgain == 'si':
        
        x1Rect = pygame.Rect(300, 400, 100, 100)
        x2Rect = pygame.Rect(600, 400, 100, 100)
        x3Rect = pygame.Rect(900, 600, 100, 100)
        
        print('a')
        for event in pygame.event.get () :
            if event.type == MOUSEBUTTONDOWN:
               pos = pygame.mouse.get_pos()
               print(pos)
               if x1Rect.collidepoint(pos):
                   windowSurface.blit(backgroundStretchedImage1, backgroundStretchedImage.get_rect() )
                    
               if x2Rect.collidepoint(pos): 
                    windowSurface.blit(backgroundStretchedImage2, backgroundStretchedImage.get_rect() )
                    pygame.display.update ()
                    playAgain = 'no'
                    level2 = False
                    
               if x3Rect.collidepoint(pos):
                    windowSurface.blit(backgroundStretchedImage3, backgroundStretchedImage.get_rect() )
                    
        pygame.display.update ()
        time.sleep(2)                    
        
        
     #gioco3  
    backgroundImage = pygame.image.load ('terzogioco.png')
    backgroundStretchedImage = pygame.transform.scale (backgroundImage, (WINDOWWIDTH, WINDOWHEIGHT))
    windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect() )
    pygame.display.update ()
    waitForPlayerToPressKey ()
    backgroundImage = pygame.image.load ('jackparla4.jpg')
    backgroundStretchedImage = pygame.transform.scale (backgroundImage, (WINDOWWIDTH, WINDOWHEIGHT))
    windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect() )
    pygame.display.update ()
    waitForPlayerToPressKey ()
            
#terzo gioco 
pygame.mixer.music.stop()
pygame.mixer.music.load('impiccato.mp3')
pygame.mixer.music.play(-1, 0.0)
isolaDeserta1 = pygame.image.load('isole-deserte 1.jpg')
isolaDeserta2 = pygame.image.load('isole-deserte 2.jpg')
isolaDeserta3 = pygame.image.load('isole-deserte 3.jpg')
isolaDeserta4 = pygame.image.load('isole-deserte 4.jpg')
isolaDeserta5 = pygame.image.load('isole-deserte 5.jpg')
isolaDeserta6 = pygame.image.load('isole-deserte 6.jpg')
isolaDeserta7 = pygame.image.load('isole-deserte 7.jpg')

isolaDeserta1Stretched1 = pygame.transform.scale(isolaDeserta1, (WINDOWWIDTH, WINDOWHEIGHT))
isolaDeserta1Stretched2 = pygame.transform.scale(isolaDeserta2, (WINDOWWIDTH, WINDOWHEIGHT))
isolaDeserta1Stretched3 = pygame.transform.scale(isolaDeserta3, (WINDOWWIDTH, WINDOWHEIGHT))
isolaDeserta1Stretched4 = pygame.transform.scale(isolaDeserta4, (WINDOWWIDTH, WINDOWHEIGHT))
isolaDeserta1Stretched5 = pygame.transform.scale(isolaDeserta5, (WINDOWWIDTH, WINDOWHEIGHT))
isolaDeserta1Stretched6 = pygame.transform.scale(isolaDeserta6, (WINDOWWIDTH, WINDOWHEIGHT))
isolaDeserta1Stretched7 = pygame.transform.scale(isolaDeserta7, (WINDOWWIDTH, WINDOWHEIGHT))

HANGMAN_PICS = [isolaDeserta1Stretched1,isolaDeserta1Stretched2, isolaDeserta1Stretched3, isolaDeserta1Stretched4, isolaDeserta1Stretched5, isolaDeserta1Stretched6, isolaDeserta1Stretched7]


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

def displayBoard(missedLetters, correctLetters, secretWord, text):

    playerRect = pygame.Rect(0, 0, WINDOWWIDTH , WINDOWHEIGHT)
    numberOfMissedLetters = len(missedLetters)
    windowSurface.blit(HANGMAN_PICS[numberOfMissedLetters], playerRect )
    
    #print(HANGMAN_PICS[numberOfMissedLetters])
    #print('Lettere sbagliate:  ' + missedLetters)

    guessedLetters = []
    for i in range(len(secretWord)) :
        if secretWord[i] in correctLetters:
            guessedLetters.append(secretWord[i])
        else:
            guessedLetters.append('_')
    drawText(str(guessedLetters), font, windowSurface, 100, 100) #guessedLetters
    
    pygame.display.update()
    return guessedLetters

def getGuess(alreadyGuessed):
   
    while True:
        drawText('Indovina una lettera.', font, windowSurface, 10, 0)
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            drawText('Inserisci una sola lettera.', font, windowSurface, 10, 0)
        elif guess in alreadyGuessed:
            drawText('Hai già indovinato questa lettera. Scegline una diversa.', font, windowSurface, 10, 0)
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            drawText('Per favore inserisci una lettera.', font, windowSurface, 10, 0)
        else:
            return guess
        pygame.display.update()
        
        
def inputDaPygame(screen):
    textinput = pygame_textinput.TextInput()

    clock = pygame.time.Clock()
    
    while True:
    
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
    
        # Feed it with events every frame
#        textinput.update(events)
        # Blit its surface onto the screen
        screen.blit(textinput.get_surface(), (10, 10))
    
        pygame.display.update()
        clock.tick(30)
        if textinput.update(events):
            return textinput.get_text()


color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
text = ''
done = False
input_box = pygame.Rect(100, 100, 140, 32)

gameIsDone = False

play = True

while play:
    
    displayBoard(missedLetters, correctLetters, secretWord, text)
    
 # Render the current text.
    txt_surface = font.render(text, True, color)
    # Resize the box if the text is too long.
    width = max(200, txt_surface.get_width()+10)
    input_box.w = width
    # Blit the text.
    windowSurface.blit(txt_surface, (input_box.x+5, input_box.y+5))
    # Blit the input_box rect.
    input_box.bottomleft = (0, 200)
#    pygame.draw.rect(windowSurface, color, input_box, 2)
    pygame.display.update()
    
    guess = ''
    
    #per scrivere dentro la casella di testo
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            done = True
#        if event.type == pygame.MOUSEBUTTONDOWN:
#            # If the user clicked on the input_box rect.
#            if input_box.collidepoint(event.pos):
#                # Toggle the active variable.
#                active = not active
#            else:
#                active = False
#            # Change the current color of the input box.
#            color = color_active if active else color_inactive
#        if event.type == pygame.KEYDOWN:
#            if active:
#                if event.key == pygame.K_RETURN:
#                    guess = text
#                    text = ''
#                elif event.key == pygame.K_BACKSPACE:
#                    text = text[:-1]
#                else:
#                    text += event.unicode

    guess = inputDaPygame(windowSurface)
    
    if guess != "":
        if guess in secretWord:
            correctLetters = correctLetters + guess
            parolaDaIndovinare = displayBoard(missedLetters, correctLetters, secretWord, text)
        
            #foundAllLetters = True
            
            for i in range(len(secretWord)):
                if secretWord[i] not in correctLetters:
                    foundAllLetters = False
                    break
            
        else:
            missedLetters = missedLetters + guess
    
    findAll = False
    parolaDaIndovinare = str(parolaDaIndovinare)
    
        
    if parolaDaIndovinare.find('_') == -1:
        findAll = True
        

            
    
    if findAll:
        pygame.mixer.music.stop()
        pygame.mixer.music.load('pirates2.mp3')
        pygame.mixer.music.play(-1, 0.0)
        backgroundImage = pygame.image.load ('jack.jpg')
        backgroundStretchedImage = pygame.transform.scale (backgroundImage, (WINDOWWIDTH, WINDOWHEIGHT))
        windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect() )
        pygame.display.update ()
        play = False
                
    if len(missedLetters) == len( HANGMAN_PICS ) - 1:
        backgroundImage = pygame.image.load ('jackfail1.jpg')
        backgroundStretchedImage = pygame.transform.scale (backgroundImage, (WINDOWWIDTH, WINDOWHEIGHT))
        windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect() )
        pygame.display.update ()
        play = False
            

pygame.display.update ()
