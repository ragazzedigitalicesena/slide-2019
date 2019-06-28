import pygame, sys 
from pygame.locals import *
pygame.init()

import random

basicFont = pygame . font . SysFont ( None , 48)

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255 , 0 , 0)
GREEN = (100, 225 , 0)
BLUE = (0 , 0 , 255)
YELLOW = (225,225,0)
LIME = (75,255,75)
TURCHESE = (0,128,228)
ARANCIO = (255,122,0)
MARRONE = (155,85,0)
CIANO = (0,225.225)
GIALLINO = (255,155,255)
ROSA = (255,155,255)
VERDESCOURO = (10,100,20)
ALTROAZZURRO = (100,155,255)
ROSAPASTELLO = (255,196,208)
BLUPETROLIO = (5,145,180)
VERDEPETROLIO = (0,128,128)
ROSA2 = (255,226,238)
VIOLA = (150,5,175)


WINDOW_WIDTH = 1300
WINDOW_HEIGHT = 800
windowSurface = pygame . display . set_mode (( WINDOW_WIDTH , WINDOW_HEIGHT ) , 0 , 32)
pygame . display . set_caption (' ')


X_POSITION = 300
Y_POSITION = 100
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
player = pygame . Rect ( X_POSITION , Y_POSITION , PLAYER_WIDTH , PLAYER_HEIGHT )


foodSize = 20
food = pygame.Rect (random.randint(0, WINDOW_WIDTH - foodSize), random.randint(0,  WINDOW_HEIGHT - foodSize), foodSize, foodSize)
print ( food .x , food . y )

water = pygame.Rect(random.randint(0, WINDOW_WIDTH - foodSize), random.randint(0,  WINDOW_HEIGHT - foodSize), foodSize, foodSize)

moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVE_SPEED = 6
MOVE_SLOW = 1

startTime = pygame . time . get_ticks ()


backgroundImage = pygame . image . load ('background.png ')
playerImage = pygame . image . load ('pacman.png ')
foodImage = pygame . image . load ('pizza.png ')

backgroundStretchedImage = pygame . transform . scale ( backgroundImage , ( WINDOW_WIDTH , WINDOW_HEIGHT ) )
playerStretchedImage = pygame . transform . scale ( playerImage , ( PLAYER_WIDTH , PLAYER_HEIGHT ) )
foodStretchedImage = pygame . transform . scale ( foodImage , ( foodSize , foodSize ) )

windowSurfaceRectangle=windowSurface.get_rect()


while True:
    for event in pygame . event . get () :
        if event . type == QUIT:
            pygame.quit()
            sys.exit()
        if event . type == KEYDOWN :
            if event . key == K_LEFT or event.key==K_1:
                moveRight = False
                moveLeft = True
            if event . key == K_RIGHT or event.key==K_3:
                moveLeft = False
                moveRight = True
            if event . key == K_UP or event.key==K_5:
                moveDown = False
                moveUp = True
            if event . key == K_DOWN or event.key==K_2:
                moveUp = False
                moveDown = True
        if event . type == KEYUP :
            if event . key == K_ESCAPE or event.key==K_q:
                pygame . quit ()
                sys . exit ()
            if event . key == K_LEFT :
                moveLeft = False
            if event . key == K_RIGHT :
                moveRight = False
            if event . key == K_UP :
                moveUp = False
            if event . key == K_DOWN :
                moveDown = False
        if event . type == MOUSEMOTION :
            print ( event . pos [0] , event . pos [1])
        if event . type == MOUSEBUTTONUP :
            foodSize=foodSize+5
            food=pygame.Rect(food.x, food.y, foodSize, foodSize)
            foodStretchedImage=pygame.transform.scale(foodImage,(foodSize, foodSize))
        if event . type == MOUSEBUTTONDOWN :    
            if event . button == 1:
                print ('Hai premuto il tasto sinistro del mouse ')
            elif event . button == 3:
                print ('Hai premuto il tasto destro del mouse ')
            else :
                print ("Hai premuto il tasto ", event . button )


    if moveDown and player . bottom < WINDOW_HEIGHT :
        player . top = player . top + MOVE_SPEED
        print ('moving down', player.top,player.bottom, player.right, player.left)
    if moveUp and player . top > 0:
        player . top = player . top - MOVE_SPEED
        print ('moving up', player.top,player.bottom, player.right, player.left)
    if moveLeft and player.left>0:
        player . left  = player.left - MOVE_SPEED
        print ('moving left', player.top,player.bottom, player.right, player.left)
    if moveRight and player.right<WINDOW_WIDTH:
        player . right = player.right + MOVE_SPEED
        print ('moving right', player.top,player.bottom, player.right, player.left)

    
    water.left = water.left + MOVE_SLOW
    
    #windowSurface . fill( BLACK ) 
    #pygame . draw . rect ( windowSurface , ROSA2 , player )
    #pygame . draw . rect ( windowSurface , LIME , food )
    pygame.draw.rect(windowSurface, ARANCIO, water) 
    if player.colliderect(food) :
        pygame.draw.rect(windowSurface , RED , food )
    
    windowSurface.blit(backgroundStretchedImage,windowSurfaceRectangle)
    windowSurface.blit(playerStretchedImage,player)
    windowSurface.blit(foodStretchedImage,food)
    
    mainClock = pygame . time . Clock ()
    mainClock . tick (20)


    
    elapsedTime = pygame . time . get_ticks ()
    print ('Tempo trascorso :', int ((( elapsedTime - startTime ) /10) ) )


    pygame . display . update ()