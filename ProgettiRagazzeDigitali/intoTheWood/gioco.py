import pygame, sys, random, time
from pygame.locals import *
pygame.init()

#colori
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255 , 0 , 0)
GREEN = (80, 180 , 70)
BLUE = (0 , 0 , 255)
YELLOW = (225,225,0)
TURCHESE = (0,128,228)
ARANCIO = (255,122,0)
BROWN=(101,67,33)
SABBIA=(218,189,171)
CIANO = (0,225.225)
GIALLINO = (255,155,255)
ROSA = (255,155,255)
VERDESCOURO = (10,100,20)
ALTROAZZURRO = (100,155,255)
ROSAPASTELLO = (255,196,208)
BLUPETROLIO = (5,145,180)
VERDEPETROLIO = (0,128,128)
VIOLA = (150,5,175)

#variabili globali
WINDOWWIDTH = 800
WINDOWHEIGHT = 800

#variabili costanti pesci
PESCIWINNER = 10
FPSPESCI = 60
PESCEMINSIZE = 40
PESCEMAXSIZE = 70
PESCEMINSPEED = 1
PESCEMAXSPEED = 4
ADDNEWPESCERATE = 30
PLAYERMOVERATEPESCI = 3
X_POSITION = 400
Y_POSITION = 850
PLAYER_WIDTH = 20
PLAYER_HEIGHT = 20
NINFEALENGTH = 50

#variabili costanti foresta
FPSLABI = 10
PLAYERMOVERATELABI = 6

#variabili costanti montagna
FPSMONTI = 20
ROCCEMINSIZE = 15
ROCCEMAXSIZE = 55
ROCCEMINSPEED = 1
ROCCEMAXSPEED = 8
ADDNEWROCCIARATE = 6
PLAYERMOVERATEMONTI = 5
SCOREWINNER = 500

#def
def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, BLACK)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
    
def terminate():
    pygame.quit()
    sys.exit()
    
def aspettaPremaTasto():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                return

#def fiume
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

def drawTextPesci(text, font, surface, x, y):
    textobj = font.render(text, 1, ALTROAZZURRO)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

#def foresta
def drawTextLabi(text, font, surface, x, y):
    textobj = font.render(text, 1, GREEN) 
    textrect = textobj.get_rect() 
    textrect.topleft = (x, y) 
    surface.blit(textobj, textrect) 
    
def colpireLabirinto(playerRect, linee):
#    for l in linee: 
#        if playerRect.colliderect(l):
#            return True
    return False

def colpireLegna(playerRect, legnaRect):
    if playerRect.colliderect(legnaRect):
        drawText('Bravo hai raccolto la legna!', font, windowSurface, (WINDOWWIDTH / 3) - 130, (WINDOWHEIGHT / 3) + 80)
        return True
    
    
#def montagna
def colpireRoccia(playerRect, rocce):
    for b in rocce:
        if playerRect.colliderect(b['rect']):
            return True
    return False

def drawTextMonti(text, font, surface, x, y):
    textobj = font.render(text, True, SABBIA)
    textrect = textobj.get_rect() 
    textrect.topleft = (x, y) 
    surface.blit(textobj, textrect)

#impostazioni generali
pygame.display.set_caption('Into the wood') 
pygame.mouse.set_visible(False) 
font = pygame.font.SysFont(None, 48)
mainClock = pygame.time.Clock()
gameOverSound = pygame.mixer.Sound('gameover.wav')


#titolo
windowSurface = pygame.display.set_mode(( WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
windowSurface.fill(GREEN)

drawText('INTO THE WOOD', font, windowSurface, 260, 376)

pygame.display.update()

aspettaPremaTasto()


#intro
windowSurface.fill(GREEN)

playerImage = pygame.image.load('boscaioloDefinitivoForse.png')
playerRect = playerImage.get_rect()
playerRect.topleft = (360, 544)
moveLeft = moveRight = moveUp = moveDown = False
windowSurface.blit(playerImage, playerRect)

drawText('Sei un boscaiolo.', font, windowSurface, 245, 256)
drawText('Devi raggiungere la cima della montagna', font, windowSurface, 80, 304)
drawText('dove troverai rifugio per la notte.', font, windowSurface, 140, 352)
drawText('Lungo il persorso incontrerai delle difficoltà', font, windowSurface, 40, 400)
drawText('da affrontare e dovrai procurarti risorse', font, windowSurface, 84, 448)
drawText('per sopravvivere.', font, windowSurface, 245, 496)

pygame.display.update()

aspettaPremaTasto()


#mappa
backgroundImage = pygame.image.load('sfondoCose.jpg')
backgroundStretchedImage = pygame.transform.scale(backgroundImage,(WINDOWWIDTH, WINDOWHEIGHT))
windowSurfaceRectangle = windowSurface.get_rect()
windowSurface.blit(backgroundStretchedImage, windowSurfaceRectangle)

playerImage = pygame.image.load('boscaioloDefinitivoForse.png')
playerRect = playerImage.get_rect()
playerRect.topleft = (WINDOWWIDTH - 240, WINDOWHEIGHT - 90)
moveLeft = moveRight = moveUp = moveDown = False
windowSurface.blit(playerImage, playerRect)

pygame.display.update()

aspettaPremaTasto()

drawText('Per prima cosa dovrai oltrepassare', font, windowSurface, (WINDOWWIDTH / 10) - 60, 48)
drawText('il fiume, poi procurarti della legna', font, windowSurface, (WINDOWWIDTH / 10) - 60, 96)
drawText('nella foresta e infine scalare la montagna.', font, windowSurface, (WINDOWWIDTH / 10) - 60, 144)
drawText('Buon viaggio!', font, windowSurface, (WINDOWWIDTH / 10) - 60, 192)

pygame.display.update()

aspettaPremaTasto()


#gioco del fiume
player = pygame.Rect( X_POSITION, Y_POSITION, PLAYER_WIDTH, PLAYER_HEIGHT)
playerImage = pygame.image.load('boscaioloDefinitivoForse.png')
playerRect = playerImage.get_rect()
pesceImage = pygame.image.load('pesce.png')
pesceRect = pesceImage.get_rect()

backgroundImage = pygame.image.load('sfondoCose.jpg')
backgroundStretchedImage = pygame.transform.scale(backgroundImage,(WINDOWWIDTH, WINDOWHEIGHT))
windowSurfaceRectangle = windowSurface.get_rect()
windowSurface.blit(backgroundStretchedImage, windowSurfaceRectangle)

pygame.mixer.music.load('river.mp3')

drawText('PESCA 10 PESCI PER LA CENA!', font, windowSurface, 145, 75) 
drawText('FAI ATTENZIONE A EVITARE LE NINFEE.', font, windowSurface, 90, 123)
drawText('PREMI UN TASTO PER PARTIRE.', font, windowSurface, 150, 630)
drawText('Per muoverti potrai usare le freccette ', font, windowSurface, 110, 250)
drawText('o i seguenti tasti: a per andare a sinistra,', font, windowSurface, 80, 298)
drawText('s per scendere, d per andare a destra,', font, windowSurface, 110, 346)
drawText('w per salire.', font, windowSurface, 305, 394)

playerRect.topleft = (100, 700)
moveLeft = moveRight = moveUp = moveDown = False
windowSurface.blit(playerImage, playerRect)

pygame.display.update()

aspettaPremaTasto()

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

ostacoloA = pygame.draw.rect(windowSurface, BROWN, (40, 327, 50, 50))
ostacoloB = pygame.draw.rect(windowSurface, BROWN, (300, 83, 50, 50))
ostacoloC = pygame.draw.rect(windowSurface, BROWN, (589, 764, 50, 50))
ostacoloD = pygame.draw.rect(windowSurface, BROWN, (130, 439, 50, 50))
ostacoloE = pygame.draw.rect(windowSurface, BROWN, (456, 13, 50, 50))
ostacoloF = pygame.draw.rect(windowSurface, BROWN, (89, 216, 50, 50))
ostacoloG = pygame.draw.rect(windowSurface, BROWN, (19, 605, 50, 50))
ostacoloH = pygame.draw.rect(windowSurface, BROWN, (244, 518, 50, 50))
ostacoloI = pygame.draw.rect(windowSurface, BROWN, (670, 650, 50, 50))
ostacoloJ = pygame.draw.rect(windowSurface, BROWN, (715, 478, 50, 50))
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
    ostacoloJRect.topleft = (715, 478)
    ostacoloKRect.topleft = (610, 128)
    ostacoloLRect.topleft = (552, 388)
    ostacoloMRect.topleft = (488, 176)
    ostacoloNRect.topleft = (327, 340)
    ostacoloORect.topleft = (733, 721)
    ostacoloPRect.topleft = (612, 290)
    
    moveLeft = moveRight = moveUp = moveDown = False
    pesciAddCounter = 0
    pygame.mixer.music.play(-1, 0.0)
    
    while True: 
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
        windowSurface.blit(playerImage, playerRect)
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
            pesciAddCounter+=1
        
        for b in pesceLista:
            windowSurface.blit(b['surface'], b['rect'])
            
        pygame.display.update()
    
        mainClock.tick(FPSPESCI)
        
    if colpireOstacolo(playerRect, ostacoli):
            pygame.mixer.music.stop()
            gameOverSound.play()
            drawText('GAME OVER', font, windowSurface, 325
            , (WINDOWHEIGHT / 3))
            drawText('Premi un tasto per rigiocare.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
            pesciScore = 0
            pygame.display.update() #aggiorno la schermata 
            aspettaPremaTasto()
    else: 
        break

pygame.mixer.music.stop()
drawText('BRAVO!', font, windowSurface, 333, (WINDOWHEIGHT / 3))
drawText('Hai pescato pesci a sufficienza!', font, windowSurface, 140, (WINDOWHEIGHT / 3) + 50)

pygame.display.update()

aspettaPremaTasto()

#gioco della foresta
playerImage = pygame.image.load('boscaioloDefinitivoForse.png')
playerRect = playerImage.get_rect()
legnaImage = pygame.image.load('legna 2.png')
legnaRect = legnaImage.get_rect()
labirintoImage = pygame.image.load('ultimoLabi.png')
labirintoStretchedImage = pygame.transform.scale(labirintoImage,(800, 300))
labirintoRect = labirintoImage.get_rect()

lineQ = pygame.draw.rect(windowSurface ,BLACK ,(30 , 444,  305 ,5))
lineW = pygame.draw.rect(windowSurface ,BLACK ,(34 , 444,  5 ,325))
lineE = pygame.draw.rect(windowSurface ,BLACK ,(30 , 675,  155 ,5))  
lineR = pygame.draw.rect(windowSurface ,BLACK ,(34 , 766,  374 ,5))
lineT = pygame.draw.rect(windowSurface ,BLACK ,(327, 675,  78 , 5))
lineY = pygame.draw.rect(windowSurface ,BLACK ,(329, 674,  5 , 92))   
lineU = pygame.draw.rect(windowSurface ,BLACK ,(400, 444,  378 ,5))
lineI = pygame.draw.rect(windowSurface ,BLACK ,(774, 443,  5 ,324))
lineO = pygame.draw.rect(windowSurface ,BLACK ,(105, 720,  81 , 5))
lineP = pygame.draw.rect(windowSurface ,BLACK ,(182, 720,  5 , 47))
lineA = pygame.draw.rect(windowSurface, BLACK, (108, 443, 5, 491-442))
lineS = pygame.draw.rect(windowSurface, BLACK, (108, 534, 5, 628-533))
lineD = pygame.draw.rect(windowSurface, BLACK, (105, 629, 334-105, 5))
lineF = pygame.draw.rect(windowSurface, BLACK, (255, 629, 5, 722-628))
lineG = pygame.draw.rect(windowSurface, BLACK, (181, 488, 5, 627-487))
lineH = pygame.draw.rect(windowSurface, BLACK, (179, 488, 477-179, 5))
lineJ = pygame.draw.rect(windowSurface, BLACK, (255, 534, 5, 581-533))
lineK = pygame.draw.rect(windowSurface, BLACK, (255, 580, 334-255, 5))
lineL = pygame.draw.rect(windowSurface, BLACK, (331, 582, 5, 627-581))
lineZ = pygame.draw.rect(windowSurface, BLACK, (327, 534, 408-327, 5))
lineX = pygame.draw.rect(windowSurface, BLACK, (404, 534, 5, 188))
lineC = pygame.draw.rect(windowSurface, BLACK, (478, 443, 5, 95))  
lineV = pygame.draw.rect(windowSurface, BLACK, (478, 673, 5, 48))
lineB = pygame.draw.rect(windowSurface, BLACK, (476, 766, 301, 5))
lineN = pygame.draw.rect(windowSurface, BLACK, (476, 720, 80, 5))
lineM = pygame.draw.rect(windowSurface, BLACK, (552, 720, 5, 47))
lineQQ = pygame.draw.rect(windowSurface, BLACK, (405, 627, 300, 5))
lineWW = pygame.draw.rect(windowSurface, BLACK, (476, 580, 300, 5))
lineEE = pygame.draw.rect(windowSurface, BLACK, (552, 488, 5, 94))
lineRR = pygame.draw.rect(windowSurface, BLACK, (552, 672, 5, 3))
lineTT = pygame.draw.rect(windowSurface, BLACK, (627, 444, 5, 48))
lineYY = pygame.draw.rect(windowSurface, BLACK, (627, 672, 5, 50))
lineUU = pygame.draw.rect(windowSurface, BLACK, (702, 488, 5, 49))
lineII = pygame.draw.rect(windowSurface, BLACK, (701, 672, 5, 50))
lineOO = pygame.draw.rect(windowSurface, BLACK, (553, 534, 150, 5)) 
linePP = pygame.draw.rect(windowSurface, BLACK, (553, 673, 75, 5))
lineAA = pygame.draw.rect(windowSurface ,BLACK ,(702, 673,  74 , 5))

pygame.mixer.music.load('billie.mp3')

backgroundImage = pygame.image.load('sfondoCose.jpg')
backgroundStretchedImage = pygame.transform.scale(backgroundImage,(WINDOWWIDTH, WINDOWHEIGHT))
windowSurfaceRectangle = windowSurface.get_rect()
windowSurface.blit(backgroundStretchedImage, windowSurfaceRectangle)

drawText('ATTRAVERSA IL LABIRINTO', font, windowSurface, 170, 75)
drawText('PER RACCOGLIERE LA LEGNA!', font, windowSurface, 152, 123)
drawText('PREMI UN TASTO PER PARTIRE.', font, windowSurface, 150, 680)
drawText('Per muoverti potrai usare le freccette ', font, windowSurface, 110, 250)
drawText('o i seguenti tasti: a per andare a sinistra,', font, windowSurface, 80, 298)
drawText('s per scendere, d per andare a destra,', font, windowSurface, 110, 346)
drawText('w per salire.', font, windowSurface, 305, 394)

playerRect.topleft = (350, 546)
moveLeft = moveRight = moveUp = moveDown = False
windowSurface.blit(playerImage, playerRect)

pygame.display.update()

aspettaPremaTasto()

playerImage = pygame.image.load('boscaiololab4.png')
playerRect = playerImage.get_rect()

backgroundImage = pygame.image.load('cartoon-background-of-forest-landscape-picture__k41561654.jpg')
backgroundStretchedImage = pygame.transform.scale(backgroundImage,(WINDOWWIDTH, WINDOWHEIGHT))
windowSurfaceRectangle = windowSurface.get_rect()

while True:
    linee = [lineQ, lineW, lineE, lineR, lineT, lineY, lineU, lineI, lineO, lineP, lineA, lineS, lineD, lineF, lineG, lineH, lineJ, lineK, lineL, lineZ, lineX, lineC, lineV, lineB, lineN, lineM, lineQQ, lineWW, lineEE, lineRR, lineTT, lineYY, lineUU, lineII, lineOO, linePP, lineAA]
    playerRect.topleft = (WINDOWWIDTH -447, WINDOWHEIGHT - 395)
    legnaRect.topleft = (WINDOWWIDTH -387.5, WINDOWHEIGHT - 38)
    labirintoRect.topleft = (WINDOWWIDTH -770, WINDOWHEIGHT - 358)
    moveLeft = moveRight = moveUp = moveDown = False
    pygame.mixer.music.play(-1, 0.0)
    
    while True: 
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
        
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * PLAYERMOVERATELABI, 0)
        if moveRight and playerRect.right < WINDOWWIDTH:
            playerRect.move_ip(PLAYERMOVERATELABI, 0)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * PLAYERMOVERATELABI)
        if moveDown and playerRect.bottom < WINDOWHEIGHT:
            playerRect.move_ip(0, PLAYERMOVERATELABI)
        
        windowSurface.blit(backgroundStretchedImage, windowSurfaceRectangle) 
        
        windowSurface.blit(playerImage, playerRect)
        windowSurface.blit(legnaImage, legnaRect)
        windowSurface.blit(labirintoImage, labirintoRect)
        
        if colpireLabirinto(playerRect, linee) or colpireLegna (playerRect, legnaRect):
            break 
        
        pygame.display.update()
        
        mainClock.tick(FPSLABI)
        
    if colpireLabirinto(playerRect,linee):
        pygame.mixer.music.stop()
        gameOverSound.play()
        drawText('GAME OVER', font, windowSurface, 325, (WINDOWHEIGHT/3))
        drawText('Premi un tasto per rigiocare.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
        pygame.display.update()
        aspettaPremaTasto()
    if colpireLegna(playerRect, legnaRect):
        break

pygame.mixer.music.stop()
drawText('BRAVO!', font, windowSurface, 350, (WINDOWHEIGHT / 3))
drawText('Hai trovato la legna!', font, windowSurface, 150, (WINDOWHEIGHT / 3) + 48)
pygame.display.update()

aspettaPremaTasto()


#gioco della montagna
playerImage = pygame.image.load('boscaioloDefinitivoForse.png')
playerRect = playerImage.get_rect()
rocciaImage = pygame.image.load('rocciadef.png')

pygame.mixer.music.load('game of t.mp3')

backgroundImage = pygame.image.load('sfondoCose.jpg')
backgroundStretchedImage = pygame.transform.scale(backgroundImage,(WINDOWWIDTH, WINDOWHEIGHT))
windowSurfaceRectangle = windowSurface.get_rect()
windowSurface.blit(backgroundStretchedImage, windowSurfaceRectangle)

drawText('SCALA LA MONTAGNA E EVITA LE ROCCE!', font, windowSurface, 35, 75)
drawText('(arriva a 500 punti per vincere)', font, windowSurface, 160, 123)
drawText('PREMI UN TASTO PER PARTIRE.', font, windowSurface, 150, 680)
drawText('Per muoverti potrai usare le freccette ', font, windowSurface, 110, 450)
drawText('o i seguenti tasti: a per andare a sinistra,', font, windowSurface, 80, 498)
drawText('s per scendere, d per andare a destra,', font, windowSurface, 110, 546)
drawText('w per salire.', font, windowSurface, 305, 594)

playerRect.topleft = (475, 270)
moveLeft = moveRight = moveUp = moveDown = False
windowSurface.blit(playerImage, playerRect)

pygame.display.update()

aspettaPremaTasto()

playerImage = pygame.image.load('bosca3.png')
playerRect = playerImage.get_rect()

backgroundImage = pygame.image.load('sfondomontidef.png')
backgroundStretchedImage = pygame.transform.scale(backgroundImage,(WINDOWWIDTH, WINDOWHEIGHT))
windowSurfaceRectangle = windowSurface.get_rect()

topScore = 0
while True:  
    rocce = [] 
    score = 0 
    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 66) 
    moveLeft = moveRight = moveUp = moveDown = False 
    rocciaAddCounter = 0  
    pygame.mixer.music.play(-1, 0.0)  
    
    while True:  
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

        rocciaAddCounter += 1
        if rocciaAddCounter == ADDNEWROCCIARATE:
            rocciaAddCounter = 0
            rocciaSize = random.randint(ROCCEMINSIZE, ROCCEMAXSIZE) 
            newRoccia = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - rocciaSize), 0 - rocciaSize, rocciaSize, rocciaSize), #
                        'speed': random.randint(ROCCEMINSPEED, ROCCEMAXSPEED),
                        'surface':pygame.transform.scale(rocciaImage, (rocciaSize, rocciaSize)),}
            rocce.append(newRoccia)    
    
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * PLAYERMOVERATEMONTI, 0)
        if moveRight and playerRect.right < WINDOWWIDTH:
            playerRect.move_ip(PLAYERMOVERATEMONTI, 0)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * PLAYERMOVERATEMONTI)
        if moveDown and playerRect.bottom < WINDOWHEIGHT:
            playerRect.move_ip(0, PLAYERMOVERATEMONTI)
    
    
        if colpireRoccia(playerRect, rocce) or score == SCOREWINNER:
            break
        elif not colpireRoccia(playerRect, rocce) and score != SCOREWINNER:
            for b in rocce:
                b['rect'].move_ip(0, b['speed'])
            score += 1
            
        for b in rocce[:]:     # quando un cattivo esce dalla finestra 
            if b['rect'].top > WINDOWHEIGHT:
                rocce.remove(b)
                
        windowSurface.blit(backgroundStretchedImage, windowSurfaceRectangle) 
        
        scoreTextMonti= 'Score: ' + str(score)
        drawTextMonti(scoreTextMonti, font, windowSurface, 10, 0)
        
        windowSurface.blit(playerImage, playerRect)
        
        for b in rocce:
            windowSurface.blit(b['surface'], b['rect'])
            
        pygame.display.update()
        
        mainClock.tick(FPSMONTI)
        
    if colpireRoccia(playerRect, rocce):
        pygame.mixer.music.stop()
        gameOverSound.play()
        drawText('GAME OVER', font, windowSurface, 325
                 , (WINDOWHEIGHT / 3))
        drawText('Premi un tasto per rigiocare.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
        pygame.display.update() 
        aspettaPremaTasto()
    else: 
        break

pygame.mixer.music.stop()
drawText('BRAVO!', font, windowSurface, 350, (WINDOWHEIGHT / 3))
drawText('Hai raggiunto la cima della montagna!', font, windowSurface, 140, (WINDOWHEIGHT / 3) + 48)

pygame.display.update()








































