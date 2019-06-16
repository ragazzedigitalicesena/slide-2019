import pygame, sys, random
from pygame.locals import *

pygame.init()

mainClock = pygame.time.Clock()
startTime = pygame.time.get_ticks()

WINDOW_HEIGHT = 800
WINDOW_WIDTH = 900
windowSurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('Input')

X_POSITION = 0
Y_POSITION = 0
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

foodSize = 20

# windowSurface.fill(WHITE)
windowSurfaceRectangle = windowSurface.get_rect()
backgroundImage = pygame.image.load('background.png')
backgroundStretchedImage = pygame.transform.scale(backgroundImage, (WINDOW_WIDTH, WINDOW_HEIGHT))

player = pygame.Rect(X_POSITION, Y_POSITION, PLAYER_WIDTH, PLAYER_HEIGHT)
food = pygame.Rect(random.randint(0, WINDOW_WIDTH - foodSize), random.randint(0, WINDOW_HEIGHT - foodSize), foodSize, foodSize)

playerImage = pygame.image.load('pacman.png')
playerStretchedImage = pygame.transform.scale(playerImage, (PLAYER_WIDTH, PLAYER_HEIGHT))

foodImage = pygame.image.load('pizza.png')
foodStretchedImage = pygame.transform.scale(foodImage, (foodSize, foodSize))

print("food x:", food.x, "food y", food.y)

pygame.display.update()

MOVE_SPEED = 6

moveLeft = False
moveRight = False
moveUp = False
moveDown = False

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
        if event.type == MOUSEMOTION:
            print(event.pos[0], event.pos[1])
        if event.type == MOUSEBUTTONUP:
            foodSize = foodSize + 5
            food = pygame.Rect(food.x, food.y, foodSize, foodSize)
            foodStretchedImage = pygame.transform.scale(foodImage, (foodSize, foodSize))
            # Aumentiamo di 5 la dimensione di'food'
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                print('Hai premuto il tasto sinistro del mouse')
            elif event.button == 3:
                print('Hai premuto il tasto destro del mouse')
            else:
                print("Hai premuto il tasto", event.button)


    if moveDown and player.bottom < WINDOW_HEIGHT:
        player.top = player.top + MOVE_SPEED
        print("moving down", player.top, player.bottom, player.right, player.left)
    if moveUp and player.top > 0:
        player.top = player.top - MOVE_SPEED
        print("moving up", player.top, player.bottom, player.right, player.left)
    if moveLeft and player.left > 0:
        player.left = player.left - MOVE_SPEED
        print("moving left", player.top, player.bottom, player.right, player.left)
    if moveRight and player.right < WINDOW_WIDTH:
        player.right = player.right + MOVE_SPEED
        print("moving right", player.top, player.bottom, player.right, player.left)

#    windowSurface.fill(WHITE)
    windowSurface.blit(backgroundStretchedImage, windowSurfaceRectangle)

    windowSurface.blit(playerStretchedImage, player)
    windowSurface.blit(foodStretchedImage, food)
#    pygame.draw.rect(windowSurface , BLACK, player)
#    pygame.draw.rect(windowSurface, GREEN, food)

    if player.colliderect(food):
        # Faccio qualcosa.
        pygame.draw.rect(windowSurface, RED, food)

    pygame.display.update()

    mainClock.tick(40)
    elapsedTime = pygame.time.get_ticks()
    print('Tempo trascorso:', int(((elapsedTime - startTime)/1000)), " secondi")
