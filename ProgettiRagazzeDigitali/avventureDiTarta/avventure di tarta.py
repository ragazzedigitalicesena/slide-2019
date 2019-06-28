import pygame, random, sys, time
from pygame.locals import *


pygame.init()

#window
WINDOWWIDTH = 1600
WINDOWHEIGHT = 900
LIGHTBLUE = (0, 154, 205)
WHITE = (255, 255, 0)



# Set up the window.
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('benvenuti su LE AVVENTURE DI TARTA!')


#player
PLAYER_IMAGE = pygame.image.load('tartaq.png')
playerStretchedImage = pygame.transform.scale(PLAYER_IMAGE, (200, 150))
playerRect = pygame.Rect(0, 400, 200, 150)

#player 2
PLAYER_IMAGE2 = pygame.image.load('tarta_campagna_level2.png')
player2StretchedImage = pygame.transform.scale(PLAYER_IMAGE2, (200, 150))
player2Rect = pygame.Rect(0, 400, 200, 150)

#player 3
PLAYER_IMAGE3 = pygame.image.load('tarta_campagna.png')
player3StretchedImage = pygame.transform.scale(PLAYER_IMAGE3, (200, 150))
player3Rect = pygame.Rect(0, 400, 200, 150)

#player4
PLAYER_IMAGE4 = pygame.image.load('finish_tarta.png')
player4StretchedImage = pygame.transform.scale(PLAYER_IMAGE4, (400, 350))
player4Rect = pygame.Rect(650, 300, 400, 350)


#arrivo
FLAG_IMAGE = pygame.image.load('arrivo.png')
flagStretchedImage = pygame.transform.scale(FLAG_IMAGE, (200, 150))
flagRect = pygame.Rect(1320, 300, 200, 150)

#arrivo2
SPIGA_IMAGE = pygame.image.load('spiga_di_grano.png')
spigaStretchedImage = pygame.transform.scale(SPIGA_IMAGE, (200, 150))
spigaRect = pygame.Rect(1320, 650, 200, 150)

#arrivo 3
BOTTINO_IMAGE = pygame.image.load('bottino_level_2.png')
bottinoStretchedImage = pygame.transform.scale(BOTTINO_IMAGE, (200, 150))
bottinoRect = pygame.Rect(1400, 0, 200, 150)

#background
BACKGROUND_IMAGE = pygame.image.load("benvenuta_tarta.jpg")
BACKGROUND_IMAGE2 = pygame.image.load("tarta_mare_level_1.jpg")
BACKGROUND_IMAGE3 = pygame.image.load("tarta_campagna_level_2.jpg")
BACKGROUND_IMAGE4 = pygame.image.load("galassia_level_3.jpg")
BACKGROUND_IMAGE5 = pygame.image.load("sfondo_finale_tarta.jpg")

windowSurfaceRectangle = windowSurface.get_rect()
backgroundStretchedImage = pygame.transform.scale(BACKGROUND_IMAGE, (WINDOWWIDTH, WINDOWHEIGHT))
windowSurfaceRectangle2 = windowSurface.get_rect()
backgroundStretchedImage2 = pygame.transform.scale(BACKGROUND_IMAGE2,(WINDOWWIDTH, WINDOWHEIGHT))
windowSurfaceRectangle3 = windowSurface.get_rect()
backgroundStretchedImage3 = pygame.transform.scale(BACKGROUND_IMAGE3,(WINDOWWIDTH, WINDOWHEIGHT))
windowSurfaceRectangle4 = windowSurface.get_rect()
backgroundStretchedImage4 = pygame.transform.scale(BACKGROUND_IMAGE4,(WINDOWWIDTH, WINDOWHEIGHT))
windowSurfaceRectangle5 = windowSurface.get_rect()
backgroundStretchedImage5 = pygame.transform.scale(BACKGROUND_IMAGE5,(WINDOWWIDTH, WINDOWHEIGHT))



#text
basicFont1 = pygame.font.SysFont("timesnewroman", 80)
basicFont2 = pygame.font.SysFont("timesnewroman", 80)
text1 = basicFont1.render('Benvenuti su', True, WHITE)
text2 = basicFont2.render('LE AVVENTURE DI TARTA!', True, WHITE)
textRect1 = text1.get_rect()
textRect1.centerx = windowSurface.get_rect().centerx
textRect1.centery = 300
textRect2 = text2.get_rect()
textRect2.centerx = windowSurface.get_rect().centerx
textRect2.centery = 400 

#movement
moveLeft = False
moveRight = False
moveUp = False
moveDown = False
MOVE_SPEED = 6


def terminate():
    pygame.quit()
    sys.exit()
    
    
def waitForPlayerToPressMouseButton():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT : #x dalla finestra
                terminate()
            if event.type == MOUSEBUTTONMDOWN:
                return event.pos
                
#funzione da richiamare per aspettare che l utente prema un pulsante
def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT: #x dalla finestra
                terminate()
        if event.type == KEYDOWN:
            if event.type == K_ESCAPE: # tasto esc dalla tastiera
                terminate()
            return # esco dalla funzione

def collideObstacole():
   collide1 = playerRect.colliderect(ostacolo1Rect)
   collide2 = playerRect.colliderect(ostacolo2Rect)
   collide3 = playerRect.colliderect(ostacolo3Rect)
   collide4 = playerRect.colliderect(ostacolo4Rect)
   return collide1 or collide2 or collide3 or collide4
   
                    
windowSurface.blit(backgroundStretchedImage, windowSurfaceRectangle)
windowSurface.blit(text1, textRect1)
windowSurface.blit(text2, textRect2)
pygame.display.update()

waitForPlayerToPressKey()

#ostacoli level 1 
ostacolo1Image = pygame.image.load("ostacolo_mare_1.png")
ostacolo1Rect = pygame.Rect(300, 300, 60, 60)
ostacolo1StretchedImage = pygame.transform.scale(ostacolo1Image, (60, 60))

ostacolo2Image = pygame.image.load("ostacolo_mare_2.png")
ostacolo2Rect = pygame.Rect(650, 550, 60, 60)
ostacolo2StretchedImage = pygame.transform.scale(ostacolo2Image,  (60, 60))

ostacolo3Image = pygame.image.load("ostacolo_mare_3.png")
ostacolo3Rect = pygame.Rect(925, 170, 60, 60)
ostacolo3StretchedImage = pygame.transform.scale(ostacolo3Image, (60, 60))

ostacolo4Image = pygame.image.load("ostacolo_mare_4.png")
ostacolo4Rect = pygame.Rect(1200, 500, 60, 60)
ostacolo4StretchedImage = pygame.transform.scale(ostacolo4Image, (60, 60))

#ostacoli level 3
ost1Image = pygame.image.load("ost_1.png")
ost1Rect = pygame.Rect(300, 550, 120, 120)
ost1StretchedImage = pygame.transform.scale(ost1Image,  (120, 120))

ost2Image = pygame.image.load("ost_2.png")
ost2Rect = pygame.Rect(400, 100, 120, 120)
ost2StretchedImage = pygame.transform.scale(ost2Image,  (120, 120))

ost3Image = pygame.image.load("ost_3.png")
ost3Rect = pygame.Rect(725, 450, 120, 120)
ost3StretchedImage = pygame.transform.scale(ost3Image, (120, 120))

ost4Image = pygame.image.load("ost_4.png")
ost4Rect = pygame.Rect(900, 120, 120, 120)
ost4StretchedImage = pygame.transform.scale(ost4Image, (120, 120))

ost5Image = pygame.image.load("ost_5.png")
ost5Rect = pygame.Rect(1150, 675, 120, 120)
ost5StretchedImage = pygame.transform.scale(ost5Image, (120, 120))

ost6Image = pygame.image.load("ost_6.png")
ost6Rect = pygame.Rect(1300, 300, 120, 120)
ost6StretchedImage = pygame.transform.scale(ost6Image, (120, 120))

#ostacoli level 2
albero1Image = pygame.image.load("albero1.png")
albero1Rect = pygame.Rect(200, 500, 120, 120)
albero1StretchedImage = pygame.transform.scale(albero1Image,  (120, 120))

albero2Image = pygame.image.load("albero2.png")
albero2Rect = pygame.Rect(900, 120, 120, 120)
albero2StretchedImage = pygame.transform.scale(albero2Image,  (120, 120))

albero3Image = pygame.image.load("albero3.png")
albero3Rect = pygame.Rect(725, 350, 120, 120)
albero3StretchedImage = pygame.transform.scale(albero3Image, (120, 120))

albero4Image = pygame.image.load("albero4.png")
albero4Rect = pygame.Rect(400, 100, 120, 120)
albero4StretchedImage = pygame.transform.scale(albero4Image, (120, 120))

albero5Image = pygame.image.load("albero5.png")
albero5Rect = pygame.Rect(1150, 675, 120, 120)
albero5StretchedImage = pygame.transform.scale(albero5Image, (120, 120))

albero6Image = pygame.image.load("albero6.png")
albero6Rect = pygame.Rect(1300, 300, 120, 120)
albero6StretchedImage = pygame.transform.scale(albero6Image, (120, 120))



#tarta level 1  
level1 = True
while level1:
    print("Dentro while")
    
    for event in pygame.event.get():
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
                pygame.quit ()
                sys.exit ()
            if event.key == K_LEFT:
                moveLeft = False
            if event.key == K_RIGHT: 
                moveRight = False
            if event.key == K_UP:
                moveUp = False
                
            if event.key == K_DOWN:
                moveDown = False
        if event.type == MOUSEMOTION:
            print ( event.pos[0], event.pos[1])


    if moveDown and playerRect.bottom < WINDOWHEIGHT:
        playerRect.bottom = playerRect.bottom + MOVE_SPEED
    if moveUp and playerRect.top > 0 and not playerRect.colliderect(ostacolo1Rect)and not playerRect.colliderect(ostacolo2Rect)and not playerRect.colliderect(ostacolo3Rect)and not playerRect.colliderect(ostacolo4Rect):
        playerRect.top = playerRect.top-MOVE_SPEED
    if moveLeft and playerRect.left > 0:
        playerRect.left = playerRect.left - MOVE_SPEED
    if moveRight and playerRect.right < WINDOWWIDTH and not playerRect.colliderect(ostacolo1Rect)and not playerRect.colliderect(ostacolo2Rect)and not playerRect.colliderect(ostacolo3Rect)and not playerRect.colliderect(ostacolo4Rect):
        playerRect.right = playerRect.right + MOVE_SPEED
        
    if playerRect.colliderect(flagRect):
        level1 = False
        
    
    
    #SFONDO
    windowSurface.blit(backgroundStretchedImage2, windowSurfaceRectangle)
    
    
    windowSurface.blit(ostacolo1StretchedImage, ostacolo1Rect)
    windowSurface.blit(ostacolo2StretchedImage, ostacolo2Rect)
    windowSurface.blit(ostacolo3StretchedImage, ostacolo3Rect)
    windowSurface.blit(ostacolo4StretchedImage, ostacolo4Rect)
    
    windowSurface.blit(flagStretchedImage, flagRect)
    
    #giocatore
    windowSurface.blit(PLAYER_IMAGE, playerRect)
    pygame.display.update()
   
 
#movement level 2
moveLeft = False
moveRight = False
moveUp = False
moveDown = False 

  
#level 2
level2 = True
while level2:
    print("Dentro while 2")
    
    for event in pygame.event.get():
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
                pygame.quit ()
                sys.exit ()
            if event.key == K_LEFT:
                moveLeft = False
            if event.key == K_RIGHT: 
                moveRight = False
            if event.key == K_UP:
                moveUp = False
                
            if event.key == K_DOWN:
                moveDown = False
        if event.type == MOUSEMOTION:
            print ( event.pos[0], event.pos[1])
            
    if moveDown and player2Rect.bottom < WINDOWHEIGHT:
        player2Rect.bottom = player2Rect.bottom + MOVE_SPEED
    if moveUp and player2Rect.top > 0 and not player2Rect.colliderect(albero1Rect) and not player2Rect.colliderect(albero2Rect)and not player2Rect.colliderect(albero3Rect)and not player2Rect.colliderect(albero4Rect) and not player2Rect.colliderect(albero5Rect)and not player2Rect.colliderect(albero6Rect):
        player2Rect.top = player2Rect.top - MOVE_SPEED
    if moveLeft and player2Rect.left > 0:
        player2Rect.left = player2Rect.left - MOVE_SPEED
    if moveRight and player2Rect.right < WINDOWWIDTH and not player2Rect.colliderect(albero1Rect)and not player2Rect.colliderect(albero2Rect)and not player2Rect.colliderect(albero3Rect)and not player2Rect.colliderect(albero4Rect) and not player2Rect.colliderect(albero5Rect)and not player2Rect.colliderect(albero6Rect):
        player2Rect.right = player2Rect.right + MOVE_SPEED
        
    if player2Rect.colliderect(spigaRect):
        level2 = False

    
     #SFONDO
    windowSurface.blit(backgroundStretchedImage3, windowSurfaceRectangle)
    
    windowSurface.blit(albero1StretchedImage, albero1Rect)
    windowSurface.blit(albero2StretchedImage, albero2Rect)
    windowSurface.blit(albero3StretchedImage, albero3Rect)
    windowSurface.blit(albero4StretchedImage, albero4Rect)
    windowSurface.blit(albero5StretchedImage, albero5Rect)
    windowSurface.blit(albero6StretchedImage, albero6Rect)
    
    windowSurface.blit(spigaStretchedImage, spigaRect)
    
     #giocatore
    windowSurface.blit(player2StretchedImage, player2Rect)
    pygame.display.update()
 
    
    
#level 3
level3 = True
while level3:
    print("Dentro while")
    
    for event in pygame.event.get():
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
                pygame.quit ()
                sys.exit ()
            if event.key == K_LEFT:
                moveLeft = False
            if event.key == K_RIGHT: 
                moveRight = False
            if event.key == K_UP:
                moveUp = False
                
            if event.key == K_DOWN:
                moveDown = False
        if event.type == MOUSEMOTION:
            print ( event.pos[0], event.pos[1])
            
    if moveDown and player3Rect.bottom < WINDOWHEIGHT:
        player3Rect.bottom = player3Rect.bottom + MOVE_SPEED
    if moveUp and player3Rect.top > 0 and not player3Rect.colliderect(ost1Rect)and not player3Rect.colliderect(ost2Rect)and not player3Rect.colliderect(ost3Rect)and not player3Rect.colliderect(ost4Rect) and not player3Rect.colliderect(ost5Rect)and not player3Rect.colliderect(ost6Rect):
        player3Rect.top = player3Rect.top - MOVE_SPEED
    if moveLeft and player3Rect.left > 0:
        player3Rect.left = player3Rect.left - MOVE_SPEED
    if moveRight and player3Rect.right < WINDOWWIDTH and not player3Rect.colliderect(ost1Rect)and not player3Rect.colliderect(ost2Rect)and not player3Rect.colliderect(ost3Rect)and not player3Rect.colliderect(ost4Rect) and not player3Rect.colliderect(ost5Rect)and not player3Rect.colliderect(ost6Rect):
        player3Rect.right = player3Rect.right + MOVE_SPEED
        
    if player3Rect.colliderect(bottinoRect):
        level3 = False

    
     #SFONDO
    windowSurface.blit(backgroundStretchedImage4, windowSurfaceRectangle)
    
    windowSurface.blit(ost1StretchedImage, ost1Rect)
    windowSurface.blit(ost2StretchedImage, ost2Rect)
    windowSurface.blit(ost3StretchedImage, ost3Rect)
    windowSurface.blit(ost4StretchedImage, ost4Rect)
    windowSurface.blit(ost5StretchedImage, ost5Rect)
    windowSurface.blit(ost6StretchedImage, ost6Rect)
    
    windowSurface.blit(bottinoStretchedImage, bottinoRect)
    
    #giocatore
    windowSurface.blit(player3StretchedImage, player3Rect)
    pygame.display.update()

#finish
while True:
   print("Dentro while")
   
   windowSurface.blit(backgroundStretchedImage5, windowSurfaceRectangle)
   

   windowSurface.blit(PLAYER_IMAGE4, player4Rect)
   pygame.display.update() 
   
   
   
   
   
   
   
   
   
   
   
   
