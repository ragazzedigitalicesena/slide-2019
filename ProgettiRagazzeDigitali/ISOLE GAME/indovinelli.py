import pygame,sys, random, time
import pygame_textinput
from pygame.locals import *
pygame.init()
WINDOW_HEIGHT= 800
WINDOW_WIDTH = 900
windowSurface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT),0,32)
windowSurfaceRectangle = windowSurface.get_rect()
backgroundImage = pygame.image.load('foresta.jpg')
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
gameOverSound = pygame.mixer.Sound('gameover2.wav')
pygame.mixer.music.load('foresta2.wav')
pygame.mixer.music.play(-1, 0.0)
drawText('QUIZ ', font, windowSurface, (WINDOW_WIDTH / 3), (WINDOW_HEIGHT / 3))
pygame.display.update()
waitForPlayerToPressKey()

windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect())
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
#  guess = int(guess)
if guess != 'c' :
    windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect())
    drawText('No, that is not true', font, windowSurface, 0, y1+100)
    pygame.mixer.music.stop()
    pygame.display.update()
    gameOverSound.play()
    gameOverSound.stop()
    pygame.quit()
    sys.exit()
if guess == 'c':
    windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect())
    drawText('Yes, you are right', font, windowSurface, 0, y1+100)
    pygame.display.update()
    time.sleep(3)
windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect())
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
#  guess = int(guess)

if guess != 'b' :
    windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect())
    drawText('No, that is not true', font, windowSurface, 0, y1+100)
    pygame.mixer.music.stop()
    pygame.display.update()
    gameOverSound.play()
    gameOverSound.stop()
    pygame.quit()
    sys.exit()
if guess == 'b':
    windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect())
    drawText('Yes, you are right', font, windowSurface, 0, y1+100)
    pygame.display.update()
    time.sleep(3)
windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect())
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
#guess = int(guess)

if guess != 'a' :
    windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect())
    drawText('No, that is not true', font, windowSurface, 0, y1+100)
    pygame.mixer.music.stop()
    pygame.display.update()
    gameOverSound.play()
    gameOverSound.stop()
#    pygame.quit()
#    sys.exit()
if guess == 'a':
    windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect())
    drawText('Yes, you are right', font, windowSurface, 0, y1+100)
    pygame.display.update()
    time.sleep(3)
pygame.quit()
sys.exit()

  



