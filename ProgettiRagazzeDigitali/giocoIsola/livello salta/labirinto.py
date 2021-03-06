
import pygame,sys
from pygame.locals import*
pygame.init()
BLUE=(0,0,255)
GREEN=(0,255,0)

WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800
windowSurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)

BACKGROUNDCOLOR=(255,190,24)
TEXTCOLOR=(0,0,0)
font = pygame . font . SysFont ( None , 48)

def waitForPlayerToPressKey () :
    while True :
        for event in pygame . event . get () :
            if event . type == QUIT :
                terminate ()
            if event . type == KEYDOWN :
                if event . key == K_ESCAPE :
                    terminate ()
                return

def playerWin(playerRect, fish):
    for f in fish:
        if playerRect.colliderect(f['rect']):
            return True
    return False

windowSurface.fill( BACKGROUNDCOLOR )

def drawText ( text , font , surface , x , y ) :
    textobj = font . render ( text , 1 , TEXTCOLOR )
    textrect = textobj . get_rect ()
    textrect.topleft = (x , y )
    surface.blit( textobj , textrect )

drawText ('Sei all\'ultimo livello,', font , windowSurface,( WINDOW_WIDTH / 3) , ( WINDOW_HEIGHT / 3) )
drawText ('per completarlo arriva', font,windowSurface , ( WINDOW_WIDTH / 3) - 30,( WINDOW_HEIGHT / 3) + 50)
drawText ('all\'aereo e scappa dall\'isola ', font,windowSurface , ( WINDOW_WIDTH / 3) - 60,( WINDOW_HEIGHT / 3) + 100)
drawText ('PREMI UN TASTO PER GIOCARE ', font,windowSurface , ( WINDOW_WIDTH / 3) - 90,( WINDOW_HEIGHT / 3) + 150)

pygame . display . update ()
waitForPlayerToPressKey ()

X_POSITION = 0
Y_POSITION = 0
PLAYER_WIDTH =25
PLAYER_HEIGHT = 30
PLAYERMOVERATE = 5
MOVE_SPEED0=9

WALLWIDTH = 30
WALLHEIGHT = 30

mainClock = pygame.time.Clock()

XPLANE_POSITION = 730
YPLANE_POSITION = 730
PLANE_WIDTH = 100
PLANE_HEIGHT = 80

LINE_DEPTH = 4

BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255)
   

def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # Pressing ESC quits.
                    terminate()
                return
            
def waitForPlayerToPressKeyExit():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                terminate()
                return
 

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
    
def checkCollision(player, rect):
    return player.colliderect(rect)
    
windowSurfaceRectangle = windowSurface.get_rect()

pygame.mixer.music.load('aladdin3.mp3')

player = pygame.Rect(X_POSITION, Y_POSITION, PLAYER_WIDTH, PLAYER_HEIGHT) 
plane = pygame.Rect(XPLANE_POSITION, YPLANE_POSITION, PLANE_WIDTH, PLANE_HEIGHT)



backgroundImage = pygame.image.load('deserto.jpg')
backgroundStretchedImage = pygame.transform.scale(backgroundImage, (WINDOW_WIDTH, WINDOW_HEIGHT))
windowSurface.blit(backgroundStretchedImage,backgroundStretchedImage.get_rect())

playerImage = pygame.image.load('esploratore4.png')
playerStretchedImage = pygame.transform.scale(playerImage, (PLAYER_WIDTH, PLAYER_HEIGHT))
windowSurface.blit(playerStretchedImage,player)

planeImage = pygame.image.load('plane3.png')
planeStretchedImage = pygame.transform.scale(planeImage, (PLANE_WIDTH, PLANE_HEIGHT))
windowSurface.blit(planeStretchedImage,planeStretchedImage.get_rect())

playerRect = playerStretchedImage.get_rect()
planeRect=planeStretchedImage.get_rect()


def drawLabirinto():
    pygame.draw.line(windowSurface,BLACK,(40 , 0),(40 , 40),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(0 , 80),(80 , 80),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(40 , 40),(120 , 40),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(120 , 40),(120 , 120),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(80 , 80),(80 , 160),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(120 , 120),(160 , 120),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(80 , 160),(210 , 160),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(200 , 120),(250 , 120),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(210 , 160),(210 , 190),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(250 , 120),(250 , 220),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(210 , 230),(210 , 260),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(250 , 220),(450 , 220),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(490 , 220),(560 , 220),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(210 , 260),(290 , 260),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(290 , 260),(290 , 420),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(330 , 260),(520 , 260),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(330 , 260),(330 , 420),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(520 , 260),(520 , 300),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(560 , 220),(560 , 340),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(560 , 340),(390 , 340),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(520 , 300),(350 , 300),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(390 , 340),(390 , 380),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(390 , 420),(390 , 460),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(350 , 300),(350 , 420),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(350 , 460),(350 , 500),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(390 , 460),(470 , 460),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(470 , 460),(470 , 540),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(350 , 500),(430 , 500),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(430 , 500),(210 , 500),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(470 , 540),(250 , 540),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(210 , 500),(210 , 620),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(250 , 540),(250 , 580),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(250 , 580),(500 , 580),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(210 , 620),(540 , 620),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(540 , 620),(540 , 540),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(500 , 580),(500 , 500),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(500 , 500),(660 , 500),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(540 , 540),(620 , 540),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(660 , 500),(660 , 700),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(620 , 540),(620 , 660),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(620 , 660),(480 , 660),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(660 , 700),(520 , 700),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(520 , 700),(520 , 740),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(480 , 660),(480 , 780),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(520 , 740),(800 , 740),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(480 , 780),(760 , 780),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(800 , 740),(800 , 800),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(760 , 780),(760 , 800),LINE_DEPTH)

    pygame.draw.line(windowSurface,BLACK,(160 , 120),(160 , 40),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(200 , 120),(200 , 80),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(160 , 40),(320 , 40),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(200 , 80),(280 , 80),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(320 , 40),(320 , 120),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(280 , 80),(280 , 160),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(280 , 160),(450 , 160),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(320 , 120),(450 , 120),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(490 , 120),(640 , 120),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(490 , 160),(600 , 160),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(600 , 160),(600 , 380),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(600 , 380),(390 , 380),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(640 , 120),(640 , 420),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(640 , 420),(390 , 420),LINE_DEPTH)


    pygame.draw.line(windowSurface,BLACK,(450 , 120),(450 , 40),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(490 , 120),(490 , 80),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(450 , 40),(720 , 40),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(490 , 80),(680 , 80),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(720 , 40),(720 , 740),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(680 , 80),(680 , 740),LINE_DEPTH)

    pygame.draw.line(windowSurface,BLACK,(450 , 160),(450 , 220),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(490 , 160),(490 , 220),LINE_DEPTH)

    pygame.draw.line(windowSurface,BLACK,(60 , 80),(60 , 190),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(60 , 190),(210 , 190),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(60 , 230),(60 , 480),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(20 , 80),(20 , 520),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(20 , 520),(60 , 520),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(100 , 520),(140 , 520),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(60 , 480),(140 , 480),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(140 , 480),(140 , 420),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(140 , 420),(350 , 420),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(180 , 460),(350 , 460),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(180 , 460),(180 , 660),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(140 , 520),(140 , 700),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(180 , 660),(300 , 660),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(140 , 700),(340 , 700),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(300 , 660),(300 , 620),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(340 , 700),(340 , 620),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(60 , 230),(210 , 230),LINE_DEPTH)

    pygame.draw.line(windowSurface,BLACK,(60 , 520),(60 , 780),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(100 , 520),(100 , 740),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(100 , 740),(480 , 740),LINE_DEPTH)
    pygame.draw.line(windowSurface,BLACK,(60 , 780),(480 , 780),LINE_DEPTH)


pygame.display.update()

moveLeft = moveRight = moveUp = moveDown = False
#waitForPlayerToPressKey()
pygame.mixer.music.play(-1, 0.0)
level3 = True
while level3:
    

    playerRect.topleft = (X_POSITION, Y_POSITION)
    planeRect.topleft = (XPLANE_POSITION, YPLANE_POSITION)
  
    windowSurface.blit(backgroundStretchedImage, windowSurfaceRectangle)
    drawLabirinto()

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

    if moveDown and player.bottom < WINDOW_HEIGHT and (windowSurface.get_at(player.bottomright) != BLACK and windowSurface.get_at(player.bottomleft) != BLACK):
        player.top = player.top + PLAYERMOVERATE
        print(windowSurface.get_at(player.bottomright), windowSurface.get_at(player.bottomleft))
    if moveUp and player.top > 0 and (windowSurface.get_at(player.topright) != BLACK and windowSurface.get_at(player.topleft) != BLACK):
        player.top = player.top - PLAYERMOVERATE
    if moveLeft and player.left > 0 and (windowSurface.get_at(player.bottomleft) != BLACK and windowSurface.get_at(player.topleft) != BLACK):
        player.left = player.left - PLAYERMOVERATE
    if moveRight and player.right < WINDOW_WIDTH and (windowSurface.get_at((player.bottomright)) != BLACK and windowSurface.get_at((player.topright)) != BLACK):
        player.right = player.right + PLAYERMOVERATE


    windowSurface.blit(playerStretchedImage, player)
    windowSurface.blit(planeStretchedImage, planeRect)

    
    
    if player.colliderect(planeRect):
        level3 = False
        
    pygame.display.update()
    mainClock.tick(20)
pygame.mixer.music.stop()
windowSurface . fill ( GREEN )
drawText ('Hai vinto', font , windowSurface ,( WINDOW_WIDTH / 3)+10 , ( WINDOW_HEIGHT / 3)+30 )
drawText ('sei riuscito a raggiungere l\'aereo,', font ,windowSurface , ( WINDOW_WIDTH / 3) -150 ,( WINDOW_HEIGHT / 3) + 60)
drawText (' adesso puoi scappare dall\'isola.', font ,windowSurface , ( WINDOW_WIDTH / 3) -150 ,( WINDOW_HEIGHT / 3) + 90)
waitForPlayerToPressKey ()
pygame . display . update ()