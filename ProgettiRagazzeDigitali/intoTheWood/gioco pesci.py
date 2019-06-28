import pygame, sys, random, time
from pygame.locals import *


WINDOW_WIDTH = 900
WINDOW_HEIGHT = 900
BLACK = (0, 0, 0)
WHITE= (255, 255, 255)
ALTROAZZURRO = (100,155,255)
FPS = 60
PESCEMINSIZE = 20
PESCEMAXSIZE = 70
PESCEMINSPEED = 1
PESCEMAXSPEED = 4
ADDNEWPESCERATE = 20
PLAYERMOVERATE = 2

X_POSITION = 400
Y_POSITION = 850
PLAYER_WIDTH = 20
PLAYER_HEIGHT = 20
player = pygame . Rect ( X_POSITION , Y_POSITION , PLAYER_WIDTH , PLAYER_HEIGHT )

pesceSize=random.randint(PESCEMINSIZE, PESCEMAXSIZE)
pesceSpeed=random.randint(PESCEMINSPEED, PESCEMAXSPEED)


font = pygame.font.SysFont(None, 80)
fontTitolo = pygame.font.SysFont(None, 110)
numeroPesci = 0

def terminate():
    pygame.quit()
    sys.exit()

def premiBottone():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # Pressing ESC quits.
                    terminate()
                return
            
def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, BLACK)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)  
            
def pescaPesci(playerRect, pesceLista):
    for b in pesceLista:
        if playerRect.colliderect(b['rect']):
            numeroPesci+=1
            return numeroPesci
           # return True
         #   drawText('Pesci: '+ numeroPesci +1, font, windowSurface, 0,0)
    #return False
    
pygame.init()
mainClock = pygame.time.Clock()

windowSurface = pygame . display . set_mode (( WINDOW_WIDTH , WINDOW_HEIGHT ) , 0 , 32)
pygame.display.set_caption('Pesci')
pygame.mouse.set_visible(False)

#pesce = pygame.Rect(random.randint(0, WINDOW_WIDTH - pesceSize), random.randint(0,  WINDOW_HEIGHT - pesceSize), pesceSize, pesceSize)

#musiche
gameOverSound = pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('river.mp3')

#imposta immagini del giocatore e dei pesci
playerImage = pygame . image . load ('bosca3.png')
playerRect = playerImage.get_rect()
pesceImage = pygame . image . load ('pesce.png')
pesceRect = pesceImage.get_rect()

playerStretchedImage = pygame . transform . scale ( playerImage , ( PLAYER_WIDTH , PLAYER_HEIGHT ) )
pesceStretchedImage = pygame . transform . scale ( pesceImage , ( pesceSize , pesceSize ) )

windowSurfaceRectangle=windowSurface.get_rect()

windowSurface.fill(ALTROAZZURRO)
drawText('Fiume', fontTitolo , windowSurface, (WINDOW_WIDTH / 3 -180), (WINDOW_HEIGHT / 3 ))
drawText('Premi un tasto per iniziare.', font, windowSurface, (WINDOW_WIDTH / 3 -200 ) , (WINDOW_HEIGHT / 3 +100) )
premiBottone()

while True:
    # Set up the start of the game.
    pesceLista = []
    numeroPesci = 0
    playerRect.topleft = (WINDOW_WIDTH / 2 - 37.5, WINDOW_HEIGHT - 85)
    moveLeft = moveRight = moveUp = moveDown = False
    pesciAddCounter = 0
    pygame.mixer.music.play(-1, 0.0)

    while True: # The game loop runs while the game part is playing.
         # Increase score
        pesciAddCounter +=1

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
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
                    
        if pesciAddCounter == ADDNEWPESCERATE:
            pesciAddCounter = 0
            pesceSize = random.randint(PESCEMINSIZE, PESCEMAXSIZE)
            newPesce = {'rect': pygame.Rect(random.randint(0, WINDOW_WIDTH - pesceSize), 0 - pesceSize, pesceSize, pesceSize),
                        'speed': random.randint(PESCEMINSPEED, PESCEMAXSPEED),
                        'surface':pygame.transform.scale(pesceImage, (pesceSize, pesceSize))}
            pesceLista.append(newPesce)
            
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
        if moveRight and playerRect.right < WINDOW_WIDTH:
            playerRect.move_ip(PLAYERMOVERATE, 0)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * PLAYERMOVERATE)
        if moveDown and playerRect.bottom < WINDOW_HEIGHT:
            playerRect.move_ip(0, PLAYERMOVERATE)
        
        for b in pesceLista:
                b['rect'].move_ip(0, b['speed'])
                
        for b in pesceLista:
            if b['rect'].top > WINDOW_WIDTH:
                pesceLista.remove(b)
            
        backgroundImage = pygame.image.load('fondale.jpg')
        backgroundStretchedImage = pygame . transform . scale ( backgroundImage , ( WINDOW_WIDTH , WINDOW_HEIGHT ) )
        windowSurface.blit(backgroundStretchedImage, windowSurfaceRectangle)
        
        
         
        windowSurface.blit(playerImage, playerRect)
        
        # Draw each pesce.
        for b in pesceLista:
            windowSurface.blit(b['surface'], b['rect'])
            
        
        
        if numeroPesci==10:
            break
        
        pescaPesci(playerRect, pesceLista)

        
        drawText('Pesci: %s' % (numeroPesci), font, windowSurface, 10, 0)
        pygame.display.update()
        
        
        mainClock.tick(FPS)

    # Stop the game and show the "Game Over" screen.
    pygame.mixer.music.stop()
    gameOverSound.play()

    drawText('GAME OVER', font, windowSurface, (WINDOW_WIDTH / 3), (WINDOW_HEIGHT / 3))
    drawText('Press a key to play again.', font, windowSurface, (WINDOW_WIDTH / 3) - 80, (WINDOW_HEIGHT / 3) + 50)
    pygame.display.update()
    premiBottone()
    
    gameOverSound.stop()
