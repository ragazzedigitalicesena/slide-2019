import pygame, sys, random 
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()

WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Input')

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

foodCounter = 0
NEWFOOD = 40
player = pygame.Rect(300, 100, 50, 50)

# Da fare - Parte 1

moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 6

while True:
    # Check for events.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:

            # Da fare - Parte 2 (da aggiungere alle righe seguenti)
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
             # Da fare - Parte 3

        # Esempio di utilizzo di pos con MOUSEMOTION e di button con MOUSEBUTTONDOWN
        if event.type == MOUSEMOTION:
            print("Positione" + str(event.pos))
        if event.type == MOUSEBUTTONDOWN:
            print("Button" + str(event.button))


        # Da fare - Parte 4

    foodCounter += 1
    if foodCounter >= NEWFOOD:
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

    windowSurface.fill(WHITE)

    if moveDown and player.bottom < WINDOWHEIGHT:
        player.top += MOVESPEED
    if moveUp and player.top > 0:
        player.top -= MOVESPEED
    # Da fare - Parte 5
    # Aggiungere il movimento verso sinistra e verso destra.
    # Ricorda che posso muovermi verso sinistra se non ho ancora raggiunto il margine sinistro della finestra,
    # quindi se player.left ...?
    # Mi posso muovere verso destra se player.right < ...?

    pygame.draw.rect(windowSurface, BLACK, player)

    new_foods = foods
    for food in new_foods:
        if player.colliderect(food):
            foods.remove(food)
    new_foods = []

    for i in range(len(foods)):
        # Da fare - 6
        # mostrare a video i rettangoli "food" presenti nella lista foods.

    pygame.display.update()
    mainClock.tick(40)

    # Da fare - Parte 7
