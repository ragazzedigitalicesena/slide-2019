import pygame, sys, random
from pygame.locals import *

pygame.init()

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
windowSurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('Hello world!')

# Set up the colors.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up fonts.
basicFont = pygame.font.SysFont(None, 48)

# Set up the text.
text = basicFont.render('Hello world!', True, WHITE, BLUE)
mainClock = pygame.time.Clock()

textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# Draw the white background onto the surface.

# Draw the text onto the surface.
windowSurface.blit(text, textRect)

# Draw the window onto the screen.
pygame.display.update()

X_POSITION = 300
Y_POSITION = 100
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
foodSize = 20
player = pygame.Rect(X_POSITION , Y_POSITION, PLAYER_WIDTH, PLAYER_HEIGHT)
pygame.draw.rect(windowSurface , BLACK , player)

windowSurface.fill(WHITE)
pygame.display.update()

moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVE_SPEED = 6

food = pygame.Rect(random.randint(0, WINDOW_WIDTH - foodSize), random.randint(0, WINDOW_HEIGHT - foodSize), foodSize, foodSize)

# Run the game loop.
while True:
    # Check for events.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # Change the keyboard variables.
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
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
            if event.key == K_UP or event.key == K_w:
                moveUp = False
            if event.key == K_DOWN or event.key == K_s:
                moveDown = False
            if event.key == K_x:
                player.top = random.randint(0, WINDOW_HEIGHT - player.height)
                player.left = random.randint(0, WINDOW_WIDTH - player.width)

        if event.type == MOUSEBUTTONUP:
            foodSize = foodSize + 5
            food = pygame.Rect(food.x, food.y, foodSize, foodSize)
        if event.type == MOUSEMOTION:
            print(event.pos[0], event.pos[1])
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                print('Hai premuto il tasto sinistro del mouse')
            elif event.button == 3: # elif significa else if. Sarebbe 'se, altrimenti se, altrimenti'
                print('Hai premuto il tasto destro del mouse')
            else:
                print('Il tasto premuto è il', event.button)

    windowSurface.fill(WHITE)
    pygame.draw.rect(windowSurface, BLACK, player)
    pygame.draw.rect(windowSurface, GREEN, food)

    # Move the player.
    if moveDown and player.bottom < WINDOW_HEIGHT:
        player.top += MOVE_SPEED
        print("moving down", player.top, player.bottom, player.right, player.left)
    if moveUp and player.top > 0:
        player.top -= MOVE_SPEED
        print("moving up", player.top, player.bottom, player.right, player.left)
    if moveLeft and player.left > 0:
        player.left -= MOVE_SPEED
        print("moving left", player.top, player.bottom, player.right, player.left)
    if moveRight and player.right < WINDOW_WIDTH:
        print("moving right", player.top, player.bottom, player.right, player.left)
        player.right += MOVE_SPEED

    if player.colliderect(food):
        pygame.draw.rect(windowSurface, RED, food)

    pygame.display.update()
    mainClock.tick (40)
