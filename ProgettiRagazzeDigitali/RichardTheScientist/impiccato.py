import pygame, sys, random
from pygame.locals import *
import pygame_textinput

def terminate():
    pygame.quit()
    sys.exit()
            

pygame.init()
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 1000
WHITE=(255,255,255)
BLACK=(0,0,0)
font= pygame.font.SysFont(None, 48)
fontSmall=pygame.font.SysFont(None, 25)

correctAnswer = ['Sei un chimico provetto!', 'Ti piace la chimica eh?'] 
wrongAnswer = ['Questa è un\'ironia che non mi piace', 'Errare humanum est, perseverare diabolicum.', 'Sono seriamente preoccupato per l\' esito di questo quiz.']   
nCorrectAnswer=random.randint(0,len(correctAnswer)-1)
nWrongAnswer=random.randint(0, len(wrongAnswer)-1)

mainClock = pygame.time.Clock()
windowSurface=pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('NOME DEL GIOCO')
pygame.mouse.set_visible(True)

backgroundImage=pygame.image.load('schermata_iniziale.jpg')
backgroundStrechedImage=pygame.transform.scale(backgroundImage, (WINDOW_WIDTH, WINDOW_HEIGHT))
windowSurfaceRectangle=windowSurface.get_rect()

hangman1=pygame.image.load('impiccato1.png')
hangman2=pygame.image.load('impiccato2.png')
hangman3=pygame.image.load('impiccato3.png')
hangman4=pygame.image.load('impiccato4.png')
hangman5=pygame.image.load('impiccato5.png')
hangman6=pygame.image.load('impiccato6.png')
hangman7=pygame.image.load('impiccato7.png')
hangman8=pygame.image.load('impiccato8.png')
hangman9=pygame.image.load('impiccato9.png')
hangman10=pygame.image.load('impiccato10.png')


X_POSITION = 0
Y_POSITION = WINDOW_HEIGHT/3
windowSurface.blit(backgroundStrechedImage, windowSurfaceRectangle)
HANGMAN_PICS=[hangman1, hangman2, hangman3, hangman4, hangman5, hangman6, hangman7, hangman8, hangman9, hangman10]
hangmanRectangle= pygame.Rect(150,150,450, 700)
     
correctLetters = []
missedLetters = []
words = ['amminoacil tRNA sintetasi', 'drosophila melanogaster', 'neurospora crassa', 'metionina', 'dissociazione', 'apparato di golgi', 'reticolo endoplasmatico', 'fenilchetonuria', 'praseodimio']


def inputDaPygame():
    textinput = pygame_textinput.TextInput()
    clock = pygame.time.Clock()
    
    inputInserito = True
    
    while inputInserito:
    
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
    
        # Feed it with events every frame
#        textinput.update(events)
        # Blit its surface onto the screen
        windowSurface.blit(textinput.get_surface(), (10, 10))
    
        pygame.display.update()
        clock.tick(30)
        
        if textinput.update(events):
            inputInserito = False
            return textinput.get_text()
    

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, WHITE)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)   
    
def getGuess(alreadyGuessed):
    while True:       
        introduzione='Inserisci una lettera.'
        drawText(introduzione,  font, windowSurface, 0,0)
        pygame.display.update()           
     
        guess = inputDaPygame()
        print(guess)
    
        guess = guess.lower()
        if len(guess) == 1 or guess not in alreadyGuessed or guess in 'abcdefghijklmnopqrstuvwxyz':
            return guess
#        drawText('Inserisci una sola lettera.', font, windowSurface, 0,0)
#        pygame.display.update()
#    elif guess in alreadyGuessed:
#        drawText('Hai già scelto questa lettera. Prova ancora.', font, windowSurface, 0,0)
#        pygame.display.update()
#    elif guess not in 'abcdefghijklmnopqrstuvwxyz':
#        drawText('Inserisci una lettera.', font, windowSurface, 0,0)
#        pygame.display.update()

#    else:
        
def getRandomWord(wordList):
    wordIndex = random.randint(0, len(words) - 1) 
    return words[wordIndex]


def displayBoard(missedLetters, correctLetters, secretWord):

    numberOfMissedLetters = len(missedLetters)
    
    windowSurface.blit(HANGMAN_PICS[numberOfMissedLetters], hangmanRectangle)
    drawText('Lettere sbagliate: ' , font, windowSurface, 650, WINDOW_HEIGHT/3 + 100)
    xPosition = 900
    for letters in missedLetters:
        drawText( letters, font, windowSurface, xPosition, WINDOW_HEIGHT/3 + 100)
        xPosition += 30
   
    guessedLetters = []
    for i in range(len(secretWord)) :
        if secretWord[i] in correctLetters:
            guessedLetters.append(secretWord[i])
        else:
            guessedLetters.append('_')
    guessedLettersStr=str(guessedLetters)
    drawText(guessedLettersStr, fontSmall, windowSurface, 650, WINDOW_HEIGHT/3 )
 
secretWord = getRandomWord(words)
 
gameIsDone = False
 
play = True
windowSurface.blit(backgroundStrechedImage, windowSurfaceRectangle)

pygame.display.update()
while play:
    for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
    displayBoard(missedLetters, correctLetters, secretWord)
    guess = getGuess(missedLetters + correctLetters)
    pygame.display.update()           

    
    if guess in secretWord:
        correctLetters.append(guess)
    else:
        missedLetters.append(guess)
 

    foundAllLetters = True
    for j in range(len(secretWord)):
        if secretWord[j] not in correctLetters:
            foundAllLetters = False
            break
        if foundAllLetters:
            drawText(correctAnswer[nCorrectAnswer] + ' la parola corretta è ' + secretWord, font,windowSurface, windowSurface.get_rect().centerx, 1000)
            gameIsDone = True
        else:
            missedLetters.append[guess]
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            drawText('Hai finito i tentativi!\n Dopo ' + str(len(missedLetters)) + ' lettere sbagliate e ' + str(len(correctLetters)) + ' corrette, la parola era "' + secretWord + '"', font,windowSurface, windowSurface.get_rect().centerx, 1000)
            gameIsDone = True
 
pygame.display.update()           
 
