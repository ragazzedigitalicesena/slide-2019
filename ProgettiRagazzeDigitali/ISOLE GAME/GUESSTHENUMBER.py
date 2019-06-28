import pygame,sys, random, time
import pygame_textinput
from pygame.locals import *

pygame.init()

WINDOW_HEIGHT= 800
WINDOW_WIDTH = 900
windowSurface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT),0,32)
windowSurfaceRectangle = windowSurface.get_rect()
backgroundImage = pygame.image.load('fuoco.png')
backgroundStretchedImage = pygame.transform.scale(backgroundImage, (WINDOW_WIDTH, WINDOW_HEIGHT))
windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect())
pygame.display.update()                                                         

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


BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: 
                    terminate()
                return
def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, BLACK)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

font = pygame.font.SysFont(None, 48)
pygame.mixer.music.load('vulcano2.wav')


pygame.mixer.music.play(-1, 0.0)
drawText('GUESS THE NUMBER', font, windowSurface, (WINDOW_WIDTH / 3), (WINDOW_HEIGHT / 3))
drawText('Press a key to start.', font, windowSurface, (WINDOW_WIDTH / 3), (WINDOW_HEIGHT / 3) + 50)
pygame.display.update()
waitForPlayerToPressKey()

windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect())
pygame.display.update()
y=150
y1=100
guessesTaken = 0
myName = textInput(10,10)
print (myName)
number = random.randint( 1,50)
drawText('Well,' + myName + ', I am thinking of a number between 1 and 50.', font, windowSurface,0, 50)
for guessesTaken in range(6):
  drawText('take a guess', font, windowSurface, 0, 100)
  guess = textInput(0,y)
  guess = int(guess)
  if guess < number:
       drawText('your guess is too low.', font, windowSurface, 0, y1+100)
  if guess > number:
        drawText('your guess is too high.', font, windowSurface, 0, y1+100)
  if guess == number:
        break
  y= y+100
  y1=y1+100
if guess == number:
   guessesTaken = str(guessesTaken+1)
   windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect())
   drawText('Good job,' + myName + '! You guessed my number in' + guessesTaken + ' guesses !', font, windowSurface, 0, 250)
   pygame.display.update()
#   pygame.mixer.music.stop()
   time.sleep(2)
if guess != number:
    number = str( number )
    windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect())
    drawText('That\'s too bad. the number i was thinking of was' + number + '.', font, windowSurface, 0, 250)
    pygame.mixer.music.stop()
    pygame.display.update()
    gameOverSound.play()
    time.sleep(5)
    gameOverSound.stop()
    
pygame.quit()
sys.exit()


