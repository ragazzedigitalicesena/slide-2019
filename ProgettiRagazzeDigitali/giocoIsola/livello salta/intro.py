import pygame, random, sys
import time
from pygame.locals import *

BACKGROUNDCOLOR = (255,0,0)
WINDOWWIDTH = 800
WINDOWHEIGHT = 800
TEXTCOLOR = (255,255,255)

def terminate():
    pygame.quit()
    sys.exit()

def livelloUno():
    WINDOWWIDTH = 800
    WINDOWHEIGHT = 800
    TEXTCOLOR = (0, 0, 0)
    FPS = 50
    ROCKSIZE = 120
    ROCKSPEED = 8
    ADDNEWROCKRATE = 90
    PLAYERMOVERATE = 8
    PLAYERWIDTH = 110
    PLAYERHEIGHT = 130
    ADDNEWFLOWERRATE = 120
    FLOWERSIZE = 60
    BACKGROUNDCOLOR = (0,255,255)
    
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
    
    def playerHasHitRock(playerRect, rock):
        for r in rock:
            if playerRect.colliderect(r['rect']):
                return True
        return False
    
    def playerHasHitFlower(playerRect, flower):
        for f in flower:
            if playerRect.colliderect(f['rect']):
                flower.remove(f)
                return True
        return False
    
    def drawText(text, font, surface, x, y):
        textobj = font.render(text, 1, TEXTCOLOR)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)
        
    pygame.init()
    mainClock = pygame.time.Clock()
    windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Salta la roccia')
    pygame.mouse.set_visible(False)
    
    font = pygame.font.SysFont(None, 60)
    
    pygame.mixer.music.load('chuChu.mp3')
    
    windowSurface.fill(BACKGROUNDCOLOR)
    
    backgroundImage = pygame.image.load('VULCANO.jpg')
    playerImage = pygame.image.load('dora.png')
    playerStretchedImage = pygame.transform.scale(playerImage, (PLAYERWIDTH, PLAYERHEIGHT))
    playerRect = playerStretchedImage.get_rect()
    rockImage = pygame.image.load('indg.png')
    
    flowerImage = pygame.image.load('fiore.png')
    
    backgroundStretchedImage = pygame.transform.scale(backgroundImage,(WINDOWWIDTH, WINDOWHEIGHT))
    drawText('Livello 1', font, windowSurface, 300, 150)
    drawText('Per superare questo livello', font, windowSurface,110, 230)
    drawText('prendi 10 fiori ma attento agli indigeni.', font, windowSurface, 20,290)
    drawText('Premi un tasto per continuare.', font, windowSurface,120 , 400)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    
    windowSurfaceRectangle = windowSurface.get_rect()
    
    topScore = 0
    score = 0
    topFiori = 0
    win = False
    
    while not win:
        
        rock = []
        flower = []
        totFlower = 0
        playerRect.topleft = (0, WINDOWHEIGHT - PLAYERHEIGHT)
        moveUp = moveDown = False
        rockAddCounter = 0
        flowerAddCounter = 0
        pygame.mixer.music.load('chuChu.mp3')
        pygame.mixer.music.play(-1, 0.0)
        
        while True:
            
    
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
    
                if event.type == KEYDOWN:
                    if event.key == K_LEFT or event.key == K_a:
                        moveRight = False
                        moveLeft = False
                    if event.key == K_RIGHT or event.key == K_d:
                        moveLeft = False
                        moveRight = False
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
                        moveDown = True
                    if event.key == K_DOWN or event.key == K_s:
                        moveDown = False
                
            
            flowerAddCounter += 1
            if flowerAddCounter == ADDNEWFLOWERRATE:
                flowerAddCounter = 0
                flowerSize = (FLOWERSIZE, FLOWERSIZE)
                newFlower = {'rect': pygame.Rect(WINDOWWIDTH, random.randint(0, WINDOWHEIGHT - FLOWERSIZE), FLOWERSIZE, FLOWERSIZE),
                            'speed': ROCKSPEED,
                            'surface':pygame.transform.scale(flowerImage, (FLOWERSIZE, FLOWERSIZE)),
                            }
    
                flower.append(newFlower)
                
            for f in flower:
                f['rect'].move_ip(-1*f['speed'],0)        
                    
            for f in flower[:]:
                if f['rect'].right < 0:
                    flower.remove(f)
                
            rockAddCounter +=1
            if rockAddCounter == ADDNEWROCKRATE:
                rockAddCounter = 0
                rockSize = (ROCKSIZE, ROCKSIZE)
                newRock = {'rect': pygame.Rect(WINDOWWIDTH, random.randint(0, WINDOWHEIGHT - ROCKSIZE), ROCKSIZE, ROCKSIZE),
                            'speed': ROCKSPEED,
                            'surface':pygame.transform.scale(rockImage, (ROCKSIZE, ROCKSIZE)),
                            }
    
                rock.append(newRock)
    
            for r in rock:
                r['rect'].move_ip(-1*r['speed'],0)
                
            for r in rock[:]:
                if r['rect'].right < 0:
                    rock.remove(r)
                    
            
            if moveUp and playerRect.top > 0:
                playerRect.move_ip(0, -1 * PLAYERMOVERATE)
            if moveDown and playerRect.bottom < WINDOWHEIGHT:
                playerRect.move_ip(0, PLAYERMOVERATE)
            
            #sfondo
            windowSurface.blit(backgroundStretchedImage, windowSurfaceRectangle)
            #giocatore
            windowSurface.blit(playerStretchedImage, playerRect)
            
    
            drawText('Score: %s' % (totFlower), font, windowSurface, 10, 0)
            drawText('Top Score: %s' % (topFiori), font, windowSurface, 10, 40)
            
            for r in rock:
                windowSurface.blit(r['surface'], r['rect'])
                
            for f in flower:
                windowSurface.blit(f['surface'], f['rect'])
                
            pygame.display.update()    
    
    
            if playerHasHitRock(playerRect, rock):
                if score > topScore:
                    topScore = score  
                pygame.mixer.music.stop()
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play(-1, 0.0)
        
                drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
                drawText('Premi un tasto per', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
                drawText(' giocare di nuovo', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 85)
                pygame.display.update()
                
                waitForPlayerToPressKey()
    
                pygame.mixer.music.stop()
                break
                
            
            if playerHasHitFlower(playerRect, flower):
                totFlower = totFlower + 1
                if totFlower > topFiori:
                    topFiori = totFlower
            
            
            if topFiori > 9:
                pygame.mixer.music.load('applausi.mp3')
                pygame.mixer.music.play(-1, 0.0)
                windowSurface.blit(backgroundStretchedImage, windowSurfaceRectangle)
                windowSurface.blit(playerStretchedImage, playerRect)
                    
                drawText('HAI SUPERATO IL LIVELLO !', font, windowSurface, 110, 230)
                drawText('Premi un tasto per', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
                drawText(' passare al secondo ', font, windowSurface, (WINDOWWIDTH / 3) - 95, (WINDOWHEIGHT / 3) + 95)
                pygame.display.update()
                pygame.mixer.music.stop()
                win = True
                break
                
            
            
            pygame.display.update()
            mainClock.tick(FPS)
           
            
def livelloDue():
    WINDOWWIDTH = 800
    WINDOWHEIGHT = 800
    TEXTCOLOR = (255, 255, 255)
    FPS = 50
    FISHMINSIZE = 40
    FISHMAXSIZE = 80
    FISHMINSPEED = 1
    FISHMAXSPEED = 8
    ADDNEWFISHRATE = 10
    PLAYERMOVERATE = 5
    PLAYERWIDTH = 60
    PLAYERHEIGHT = 80
    BACKGROUNDCOLOR = (255,181,197)
    
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
    
    def playerHasHitFish(playerRect, fish):
        for f in fish:
            if playerRect.colliderect(f['rect']):
                return True
        return False
    
    def drawText(text, font, surface, x, y):
        textobj = font.render(text, 1, TEXTCOLOR)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)
        
    pygame.init()
    mainClock = pygame.time.Clock()
    windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Schiva i pesci')
    pygame.mouse.set_visible(False)
    
    font = pygame.font.SysFont(None, 60)
    
    pygame.mixer.music.load('babyshark.mp3')
    
    windowSurface.fill(BACKGROUNDCOLOR)
    backgroundImage = pygame.image.load('mare.jpg')
    playerImage = pygame.image.load('tipo2.png')
    playerStretchedImage = pygame.transform.scale(playerImage, (PLAYERWIDTH, PLAYERHEIGHT))
    playerRect = playerStretchedImage.get_rect()
    fishImage = pygame.image.load('PESCI4.png')
    
    backgroundStretchedImage = pygame.transform.scale(backgroundImage,(WINDOWWIDTH, WINDOWHEIGHT))
    drawText('Livello 2', font, windowSurface, 300,150)
    drawText('Sei arrivato al secondo livello,', font, windowSurface, 120,230)
    drawText('per superarlo, schiva i pesci', font, windowSurface, 120,290)
    drawText('Premi un tasto per continuare', font, windowSurface, 120,400)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    
    windowSurfaceRectangle = windowSurface.get_rect()
    
    topScore = 0
    score = 0
    win = False
    
    while not win:
        
        fish = []
        score = 0
        playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
        moveLeft = moveRight = moveUp = moveDown = False
        reverseCheat = slowCheat = False
        fishAddCounter = 0
        pygame.mixer.music.load('babyshark.mp3')
        pygame.mixer.music.play(-1, 0.0)
        
        while True:
            score += 1 
    
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
    
                if event.type == KEYDOWN:
                    if event.key == K_z:
                        reverseCheat = True
                    if event.key == K_x:
                        slowCheat = True
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
                    if event.key == K_z:
                        reverseCheat = False
                        score = 0
                    if event.key == K_x:
                        slowCheat = False
                        score = 0
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
                
                if event.type == MOUSEMOTION:
                    playerRect.centerx = event.pos[0]
                    playerRect.centery = event.pos[1]
            if not reverseCheat and not slowCheat:
                fishAddCounter += 1
            if fishAddCounter == ADDNEWFISHRATE:
                fishAddCounter = 0
                fishSize = random.randint(FISHMINSIZE, FISHMAXSIZE)
                newFish = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - fishSize), 0 - fishSize, fishSize, fishSize),
                            'speed': random.randint(FISHMINSPEED, FISHMAXSPEED),
                            'surface':pygame.transform.scale(fishImage, (fishSize, fishSize)),
                            }
    
                fish.append(newFish)
            
            if moveLeft and playerRect.left > 0:
                playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
            if moveRight and playerRect.right < WINDOWWIDTH:
                playerRect.move_ip(PLAYERMOVERATE, 0)
            if moveUp and playerRect.top > 0:
                playerRect.move_ip(0, -1 * PLAYERMOVERATE)
            if moveDown and playerRect.bottom < WINDOWHEIGHT:
                playerRect.move_ip(0, PLAYERMOVERATE)
    
            for f in fish:
                if not reverseCheat and not slowCheat:
                    f['rect'].move_ip(0, f['speed'])
                elif reverseCheat:
                    f['rect'].move_ip(0, -5)
                elif slowCheat:
                    f['rect'].move_ip(0, 1)
    
            for f in fish[:]:
                if f['rect'].top > WINDOWHEIGHT:
                    fish.remove(f)
            
            
            windowSurface.blit(backgroundStretchedImage, windowSurfaceRectangle)
            windowSurface.blit(playerStretchedImage, playerRect)
    
            drawText('Score: %s' % (score), font, windowSurface, 10, 0)
            drawText('Top Score: %s' % (topScore), font, windowSurface, 10, 40)
            
            for f in fish:
                windowSurface.blit(f['surface'], f['rect'])
    
    
            if playerHasHitFish(playerRect, fish) and not win:
                if score > topScore:
                    topScore = score  
                pygame.mixer.music.stop()
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play(-1, 0.0)
        
                drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
                drawText('Premi un tasto per', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
                drawText(' giocare di nuovo', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 85)
                pygame.display.update()
                
                waitForPlayerToPressKey()
                pygame.display.update()
    
                pygame.mixer.music.stop()
                pygame.display.update()
                break
            
            if score > 500:
                pygame.mixer.music.load('applausi.mp3')
                pygame.mixer.music.play(-1, 0.0)
                windowSurface.blit(backgroundStretchedImage, windowSurfaceRectangle)
                windowSurface.blit(playerStretchedImage, playerRect)
                
                drawText('Score: %s' % (score), font, windowSurface, 10, 0)
                drawText('Top Score: %s' % (topScore), font, windowSurface, 10, 40)
                
                for f in fish:
                    windowSurface.blit(f['surface'], f['rect'])
                    
                drawText('HAI VINTO !!', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
                drawText('Premi un tasto per continuare', font, windowSurface, (WINDOWWIDTH / 3) - 65, (WINDOWHEIGHT / 3) + 50)
                pygame.display.update()
                pygame.mixer.music.stop()
                pygame.display.update()
                win = True
                break
                
            
            pygame.display.update()
            mainClock.tick(FPS)


def livelloTre():
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
    
    backgroundWin = pygame.image.load('plane3.png')
    backgroundStretchedImage1 = pygame.transform.scale(backgroundWin, (WINDOW_WIDTH, WINDOW_HEIGHT))
    
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
    
    pygame.mixer.music.load('champion.mp3')
    pygame.mixer.music.play(-1, 0.0)
    windowSurface.blit(backgroundStretchedImage1,backgroundStretchedImage1.get_rect())
    drawText ('Hai vinto', font , windowSurface ,300,250 )
    drawText ('sei riuscito a raggiungere l\'aereo,', font ,windowSurface , 100,310)
    drawText (' adesso puoi scappare dall\'isola.', font ,windowSurface , 100,360)
    pygame . display . update ()
    waitForPlayerToPressKey ()
    time.sleep(5)
    pygame.mixer.music.stop()
    pygame . display . update ()

            

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
    
def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # Pressing ESC quits.
                    terminate()
                return

pygame.init()

windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

backgroundImage = pygame.image.load('ESCAPE.jpg')
backgroundStretchedImage = pygame.transform.scale(backgroundImage, (WINDOWWIDTH, WINDOWHEIGHT))
windowSurface.blit(backgroundStretchedImage,backgroundStretchedImage.get_rect())

pygame.mouse.set_visible(True)
pygame.display.update()

waitForPlayerToPressKey()

backgroundImage1 = pygame.image.load('isolahome.jpg')
backgroundStretchedImage1 = pygame.transform.scale(backgroundImage1, (WINDOWWIDTH, WINDOWHEIGHT))
windowSurface.blit(backgroundStretchedImage1,backgroundStretchedImage1.get_rect())
pygame.display.update()

font = pygame.font.SysFont(None, 60)

drawText('Sei su un\'isola deserta,', font , windowSurface, 150, 150 )
drawText('il tuo obbiettivo è ', font,windowSurface , 170 , 195)
drawText('scappare e raggiungere l\'aereo, ', font,windowSurface , 100, 240)
drawText('per fare ciò dovrai affrontare ', font,windowSurface , 100, 285)
drawText('e superare tre prove.', font , windowSurface,150,330)
drawText('In queste ultime sarai: ', font,windowSurface , 150,375)
drawText('un esploratore, ', font,windowSurface , 170,420)
drawText('un subacqueo e ', font,windowSurface , 170,465)
drawText('un investigatore. ', font , windowSurface,170,510 )
drawText('Mi raccomando divertiti,  ', font,windowSurface , 150,555)
drawText('BUONA FORTUNA !!! ', font,windowSurface ,170,600 )

pygame.display.update()
waitForPlayerToPressKey()

livelloUno()
waitForPlayerToPressKey()

livelloDue()
waitForPlayerToPressKey()

livelloTre()
waitForPlayerToPressKey()
pygame.display.update()



