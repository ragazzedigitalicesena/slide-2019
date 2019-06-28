import pygame, sys, random
from pygame.locals import *

pygame.init()

mainClock = pygame.time.Clock()
startTime = pygame.time.get_ticks()

WINDOW_HEIGHT = 800
WINDOW_WIDTH = 900
windowSurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)

X_POSITION = 15
Y_POSITION = 15
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
LINE_DEPTH = 4

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
MOVE_SPEED = 5

moveLeft = False
moveRight = False
moveUp = False
moveDown = False

# windowSurface.fill(WHITE)
windowSurfaceRectangle = windowSurface.get_rect()
backgroundImage = pygame.image.load('background.png')
backgroundStretchedImage = pygame.transform.scale(backgroundImage, (WINDOW_WIDTH, WINDOW_HEIGHT))

player = pygame.Rect(X_POSITION, Y_POSITION, PLAYER_WIDTH, PLAYER_HEIGHT)
playerImage = pygame.image.load('pacman.png')
playerStretchedImage = pygame.transform.scale(playerImage, (PLAYER_WIDTH, PLAYER_HEIGHT))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT:
                moveLeft = False
                moveRight = True
            if event.key == K_UP:
                moveDown = False
                moveUp = True
            if event.key == K_DOWN:
                moveUp = False
                moveDown = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT:
                moveLeft = False
            if event.key == K_RIGHT:
                moveRight = False
            if event.key == K_UP:
                moveUp = False
            if event.key == K_DOWN:
                moveDown = False

    if moveDown and player.bottom < WINDOW_HEIGHT and windowSurface.get_at((player.x, player.bottom + LINE_DEPTH)) != BLACK:
        player.top = player.top + MOVE_SPEED
        print(player.x, player.y)
    if moveUp and player.top > 0 and windowSurface.get_at((player.x, player.y - LINE_DEPTH)) != BLACK:
        player.top = player.top - MOVE_SPEED
        print(player.x, player.y)
    if moveLeft and player.left > 0 and windowSurface.get_at((player.x - LINE_DEPTH, player.y)) != BLACK:
        player.left = player.left - MOVE_SPEED
        print(player.x, player.y)
    if moveRight and player.right < WINDOW_WIDTH and windowSurface.get_at((player.right + LINE_DEPTH, player.y)) != BLACK:
        player.right = player.right + MOVE_SPEED
        print(player.x, player.y)

    windowSurface.blit(backgroundStretchedImage, windowSurfaceRectangle)
    windowSurface.blit(playerStretchedImage, player)

    X_COORDINATES = [(10, 10), (10, 10), (100, 100), (100, 100), (100, 400), (10, 500), (400, 100), (500, 10)]
    Y_COORDINATES = [(10, 500), (500, 10), (100, 400), (400, 100), (400, 400), (500,  500), (400, 400), (500, 500)]

    if len(X_COORDINATES) == len(Y_COORDINATES):
        for i in range(len(X_COORDINATES)):
            pygame.draw.line(windowSurface, BLACK, X_COORDINATES[i], Y_COORDINATES[i], LINE_DEPTH)

    # pygame.draw.line(windowSurface, BLACK,(10 , 10), (10, 500), LINE_DEPTH)
    # pygame.draw.line(windowSurface, BLACK,(10 , 10), (500, 10), LINE_DEPTH)
    #
    # pygame.draw.line(windowSurface, BLACK,(100 , 100), (100, 400), LINE_DEPTH)
    # pygame.draw.line(windowSurface, BLACK,(100 , 100), (400, 100), LINE_DEPTH)
    #
    # pygame.draw.line(windowSurface, BLACK, (100, 400), (400, 400), LINE_DEPTH)
    # pygame.draw.line(windowSurface, BLACK, (10, 500), (500, 500), LINE_DEPTH)
    #
    # pygame.draw.line(windowSurface, BLACK, (400, 100), (400, 400), LINE_DEPTH)
    # pygame.draw.line(windowSurface, BLACK, (500 , 10), (500, 500), LINE_DEPTH)

    pygame.display.update()

    mainClock.tick(40)
