import random, sys, pygame, time
from pygame.locals import *

WINDOWWIDTH = 900
WINDOWHEIGHT = 900

NINFEALENGTH = 50


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ALTROAZZURRO = (100,155,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN=(101,67,33)
SABBIA=(218,189,171)

PESCIWINNER = 10

FPS = 60
PESCEMINSIZE = 40
PESCEMAXSIZE = 70
PESCEMINSPEED = 1
PESCEMAXSPEED = 4
ADDNEWPESCERATE = 30
PLAYERMOVERATEPESCI = 3 # di quanto si muove il giocatore (tieni un valore basso)

X_POSITION = 400
Y_POSITION = 850
PLAYER_WIDTH = 20
PLAYER_HEIGHT = 20
player = pygame . Rect ( X_POSITION , Y_POSITION , PLAYER_WIDTH , PLAYER_HEIGHT )

def terminate():
    pygame.quit()
    sys.exit()

def aspettaPremaTasto():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # Pressing ESC quits.
                    terminate()
                return
            
def drawTextPesci(text, font, surface, x, y):
    textobj = font.render(text, 1, ALTROAZZURRO)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)  
    
def pescaPesci(playerRect, pesceLista, pesciScore):
    for b in pesceLista:
        if playerRect.colliderect(b['rect']):
            pesceLista.remove(b)
            pesciScore = pesciScore + 1
    scoreText= 'Score: ' + str(pesciScore)
    drawTextPesci(scoreText, font, windowSurface, 10, 0)
    return pesciScore

def colpireOstacolo(playerRect, ostacoli):
    for o in ostacoli:
        if playerRect.colliderect(o):
            return True
    return False



pygame.init()
mainClock = pygame.time.Clock()

windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
backgroundImage = pygame.image.load('fondale.jpg')
backgroundStretchedImage = pygame.transform.scale(backgroundImage,(WINDOWWIDTH, WINDOWHEIGHT))
windowSurfaceRectangle = windowSurface.get_rect()

ostacoloAImage = pygame.image.load('ninfeedef.png')
ostacoloAStretchedImage = pygame.transform.scale(ostacoloAImage, (NINFEALENGTH, NINFEALENGTH))
ostacoloARect = ostacoloAStretchedImage.get_rect()

ostacoloBImage = pygame.image.load('ninfeedef.png')
ostacoloBStretchedImage = pygame.transform.scale(ostacoloBImage, (NINFEALENGTH, NINFEALENGTH))
ostacoloBRect = ostacoloBStretchedImage.get_rect()

ostacoloCImage = pygame.image.load('ninfeedef.png')
ostacoloCStretchedImage = pygame.transform.scale(ostacoloCImage, (NINFEALENGTH, NINFEALENGTH))
ostacoloCRect = ostacoloCStretchedImage.get_rect()

ostacoloDImage = pygame.image.load('ninfeedef.png')
ostacoloDStretchedImage = pygame.transform.scale(ostacoloDImage, (NINFEALENGTH, NINFEALENGTH))
ostacoloDRect = ostacoloDStretchedImage.get_rect()

ostacoloEImage = pygame.image.load('ninfeedef.png')
ostacoloEStretchedImage = pygame.transform.scale(ostacoloEImage, (NINFEALENGTH, NINFEALENGTH))
ostacoloERect = ostacoloEStretchedImage.get_rect()

ostacoloFImage = pygame.image.load('ninfeedef.png')
ostacoloFStretchedImage = pygame.transform.scale(ostacoloFImage, (NINFEALENGTH, NINFEALENGTH))
ostacoloFRect = ostacoloFStretchedImage.get_rect()

ostacoloGImage = pygame.image.load('ninfeedef.png')
ostacoloGStretchedImage = pygame.transform.scale(ostacoloGImage, (NINFEALENGTH, NINFEALENGTH))
ostacoloGRect = ostacoloGStretchedImage.get_rect()

ostacoloHImage = pygame.image.load('ninfeedef.png')
ostacoloHStretchedImage = pygame.transform.scale(ostacoloHImage, (NINFEALENGTH, NINFEALENGTH))
ostacoloHRect = ostacoloHStretchedImage.get_rect()

ostacoloIImage = pygame.image.load('ninfeedef.png')
ostacoloIStretchedImage = pygame.transform.scale(ostacoloIImage, (NINFEALENGTH, NINFEALENGTH))
ostacoloIRect = ostacoloIStretchedImage.get_rect()

ostacoloJImage = pygame.image.load('ninfeedef.png')
ostacoloJStretchedImage = pygame.transform.scale(ostacoloJImage, (NINFEALENGTH, NINFEALENGTH))
ostacoloJRect = ostacoloJStretchedImage.get_rect()

ostacoloKImage = pygame.image.load('ninfeedef.png')
ostacoloKStretchedImage = pygame.transform.scale(ostacoloKImage, (NINFEALENGTH, NINFEALENGTH))
ostacoloKRect = ostacoloKStretchedImage.get_rect()

ostacoloLImage = pygame.image.load('ninfeedef.png')
ostacoloLStretchedImage = pygame.transform.scale(ostacoloLImage, (NINFEALENGTH, NINFEALENGTH))
ostacoloLRect = ostacoloLStretchedImage.get_rect()

ostacoloMImage = pygame.image.load('ninfeedef.png')
ostacoloMStretchedImage = pygame.transform.scale(ostacoloMImage, (NINFEALENGTH, NINFEALENGTH))
ostacoloMRect = ostacoloMStretchedImage.get_rect()

ostacoloNImage = pygame.image.load('ninfeedef.png')
ostacoloNStretchedImage = pygame.transform.scale(ostacoloNImage, (NINFEALENGTH, NINFEALENGTH))
ostacoloNRect = ostacoloNStretchedImage.get_rect()

ostacoloOImage = pygame.image.load('ninfeedef.png')
ostacoloOStretchedImage = pygame.transform.scale(ostacoloOImage, (NINFEALENGTH, NINFEALENGTH))
ostacoloORect = ostacoloOStretchedImage.get_rect()

ostacoloPImage = pygame.image.load('ninfeedef.png')
ostacoloPStretchedImage = pygame.transform.scale(ostacoloPImage, (NINFEALENGTH, NINFEALENGTH))
ostacoloPRect = ostacoloPStretchedImage.get_rect()

pygame.display.set_caption('Into the wood')   #titoletto della finestra (in alto)
pygame.mouse.set_visible(False) #prendi ilmouse e quando è sulla finestra nascondilo
font = pygame.font.SysFont(None, 48)
gameOverSound = pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('river.mp3')

playerImage = pygame.image.load('boscaiolo2.png')
playerRect = playerImage.get_rect()
pesceImage = pygame.image.load('pesce.png')
pesceRect = pesceImage.get_rect()


drawTextPesci('PESCA 10 PESCI PER LA CENA!', font, windowSurface, 100, 100) 
drawTextPesci('FAI ATTENZIONE A EVITARE LE NINFEE.', font, windowSurface, 100, 150) # vedi funzione sopra (stampa il testo)
drawTextPesci('PREMI UN TASTO PER PARTIRE.', font, windowSurface, 155, 700)
drawTextPesci('Per muoverti potrai usare le freccette ', font, windowSurface, 132, 350)
drawTextPesci('o i seguenti tasti: a per andare a sinistra,', font, windowSurface, 112, 380)
drawTextPesci('s per scendere, d per andare a destra, w per salire.', font, windowSurface, 50, 410)

pygame.display.update()

aspettaPremaTasto()


ostacoloA = pygame.draw.rect(windowSurface, BROWN, (40, 327, 50, 50))
ostacoloB = pygame.draw.rect(windowSurface, BROWN, (300, 83, 50, 50))
ostacoloC = pygame.draw.rect(windowSurface, BROWN, (589, 764, 50, 50))
ostacoloD = pygame.draw.rect(windowSurface, BROWN, (130, 439, 50, 50))
ostacoloE = pygame.draw.rect(windowSurface, BROWN, (456, 13, 50, 50))
ostacoloF = pygame.draw.rect(windowSurface, BROWN, (89, 216, 50, 50))
ostacoloG = pygame.draw.rect(windowSurface, BROWN, (19, 605, 50, 50))
ostacoloH = pygame.draw.rect(windowSurface, BROWN, (244, 518, 50, 50))
ostacoloI = pygame.draw.rect(windowSurface, BROWN, (670, 650, 50, 50))
ostacoloJ = pygame.draw.rect(windowSurface, BROWN, (815, 478, 50, 50))
ostacoloK = pygame.draw.rect(windowSurface, BROWN, (610, 128, 50, 50))
ostacoloL = pygame.draw.rect(windowSurface, BROWN, (552, 388, 50, 50))
ostacoloM = pygame.draw.rect(windowSurface, BROWN, (488, 176, 50, 50))
ostacoloN = pygame.draw.rect(windowSurface, BROWN, (327, 340, 50, 50))
ostacoloO = pygame.draw.rect(windowSurface, BROWN, (733, 721, 50, 50))
ostacoloP = pygame.draw.rect(windowSurface, BROWN, (612, 290, 50, 50))

pesciScore = 0
while True:
    ostacoli = [ostacoloA, ostacoloB, ostacoloC, ostacoloD, ostacoloE, ostacoloF, ostacoloG, ostacoloH, ostacoloI, ostacoloJ, ostacoloK, ostacoloL, ostacoloM, ostacoloN, ostacoloP]
    pesceLista = []
    
    playerRect.topleft = (WINDOWWIDTH / 2 - 37.5, WINDOWHEIGHT - 85)
    ostacoloARect.topleft = (40, 327)
    ostacoloBRect.topleft = (300, 83)
    ostacoloCRect.topleft = (589, 764)
    ostacoloDRect.topleft = (130, 439)
    ostacoloERect.topleft = (456, 13)
    ostacoloFRect.topleft = (89, 216)
    ostacoloGRect.topleft = (19, 605)
    ostacoloHRect.topleft = (244, 518)
    ostacoloIRect.topleft = (670, 650)
    ostacoloJRect.topleft = (815, 478)
    ostacoloKRect.topleft = (610, 128)
    ostacoloLRect.topleft = (552, 388)
    ostacoloMRect.topleft = (488, 176)
    ostacoloNRect.topleft = (327, 340)
    ostacoloORect.topleft = (733, 721)
    ostacoloPRect.topleft = (612, 290)
    
    moveLeft = moveRight = moveUp = moveDown = False
    pesciAddCounter = 0
    pygame.mixer.music.play(-1, 0.0)
    
    while True: # The game loop runs while the game part is playing.
         # Increase score
        #pesciAddCounter +=1
        for event in pygame.event.get(): # ogni volta che succede qualcosa 
            if event.type == QUIT: # se clicca la x 
                terminate()

            if event.type == KEYDOWN: #se il giocatore preme un tasto
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

            if event.type == KEYUP: # se il giocatore rilascia un tasto
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
            newPesce = {'rect': pygame.Rect(0, random.randint(0, WINDOWHEIGHT - pesceSize), pesceSize, pesceSize),
                    'speed': random.randint(PESCEMINSPEED, PESCEMAXSPEED),
                    'surface':pygame.transform.scale(pesceImage, (pesceSize, pesceSize))}
            pesceLista.append(newPesce)

        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * PLAYERMOVERATEPESCI, 0)
        if moveRight and playerRect.right < WINDOWWIDTH:
            playerRect.move_ip(PLAYERMOVERATEPESCI, 0)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * PLAYERMOVERATEPESCI)
        if moveDown and playerRect.bottom < WINDOWHEIGHT:
            playerRect.move_ip(0, PLAYERMOVERATEPESCI)
            
        
        for b in pesceLista:
            b['rect'].move_ip(b['speed'], 0)
        
        for b in pesceLista:
            if b['rect'].left > WINDOWWIDTH:
                pesceLista.remove(b)
        

        
        windowSurface.blit(backgroundStretchedImage, windowSurfaceRectangle)
        
#        ostacoloA = pygame.draw.rect(windowSurface, BROWN, (40, 327, 50, 50))
#        ostacoloB = pygame.draw.rect(windowSurface, BROWN, (300, 83, 50, 50))
#        ostacoloC = pygame.draw.rect(windowSurface, BROWN, (589, 764, 50, 50))
        
        windowSurface.blit(ostacoloAStretchedImage, ostacoloARect)
        windowSurface.blit(ostacoloBStretchedImage, ostacoloBRect)
        windowSurface.blit(ostacoloCStretchedImage, ostacoloCRect)
        windowSurface.blit(ostacoloDStretchedImage, ostacoloDRect)
        windowSurface.blit(ostacoloEStretchedImage, ostacoloERect)
        windowSurface.blit(ostacoloFStretchedImage, ostacoloFRect)
        windowSurface.blit(ostacoloGStretchedImage, ostacoloGRect)
        windowSurface.blit(ostacoloHStretchedImage, ostacoloHRect)
        windowSurface.blit(ostacoloIStretchedImage, ostacoloIRect)
        windowSurface.blit(ostacoloJStretchedImage, ostacoloJRect)
        windowSurface.blit(ostacoloKStretchedImage, ostacoloKRect)
        windowSurface.blit(ostacoloLStretchedImage, ostacoloLRect)
        windowSurface.blit(ostacoloMStretchedImage, ostacoloMRect)
        windowSurface.blit(ostacoloNStretchedImage, ostacoloNRect)
        windowSurface.blit(ostacoloOStretchedImage, ostacoloORect)
        windowSurface.blit(ostacoloPStretchedImage, ostacoloPRect)
        
        pesciScore = pescaPesci(playerRect, pesceLista, pesciScore)
        
        if pesciScore == PESCIWINNER or colpireOstacolo(playerRect, ostacoli):
            break
        else:
            pesciAddCounter +=1
        
        windowSurface.blit(playerImage, playerRect)
#        windowSurface.blit(ostacoloAImage, ostacoloARect)
#        windowSurface.blit(ostacoloBImage, ostacoloBRect)
#        windowSurface.blit(ostacoloCImage, ostacoloCRect)
        
        for b in pesceLista:
            windowSurface.blit(b['surface'], b['rect'])
            
        pygame.display.update()
    
        mainClock.tick(FPS)
        
    if colpireOstacolo(playerRect, ostacoli):
            pygame.mixer.music.stop()
            gameOverSound.play()
            drawTextPesci('GAME OVER', font, windowSurface, 325
            , (WINDOWHEIGHT / 3))
            drawTextPesci('Premi un tasto per rigiocare.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
            pesciScore = 0
            pygame.display.update() #aggiorno la schermata 
            aspettaPremaTasto()
    else: 
        break

pygame.mixer.music.stop()
drawTextPesci('BRAVO!', font, windowSurface, 350, (WINDOWHEIGHT / 3))
drawTextPesci('Hai pescato pesci a sufficienza!', font, windowSurface, 140, (WINDOWHEIGHT / 3) + 50)

pygame.display.update()








