import pygame, random, sys
from pygame.locals import *

WINDOWWIDTH = 1500
WINDOWHEIGHT = 1000
TEXTCOLOR = (255,0,0)
TITLESCOLOR = (0,0,0)
BACKGROUNDCOLOR = (255,193,23)
FPS = 60
OBSTACLESMINSIZE = 100
OBSTACLESMAXSIZE = 300
SONICSIZE = 300
ORMESIZE=65
BROWSERSIZE = 80
MARIOSIZE = 50
SONICMOVERATE = 20
ORMEMOVERATE=6
OBSTACLESSPEED = 8
OBSTACLESADDRATE = 120
MONEYSIZE = 50
MONEYADDRATE = 100
MONEYSPEED = 8
ADDNEWMARIORATE=80
MARIOMINSIZE=50
MARIOMAXSIZE=150
MARIOMINSPEED=10
MARIOMAXSPEED=18

def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: 
                    terminate()
                else:
                    return
            
def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect) 

def drawTitles(text, font, surface, x, y):
    textobj = font.render(text, 1, TITLESCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)  

def sonicHasHitObstacle( sonicRect , obstacles ): 
    for b in obstacles:
        if sonicRect.colliderect(b['rect']):
            return True
    return False        
            
def sonicHasHitMoney (sonicRect,money):
    for b in money:
        if sonicRect.colliderect(b['rect']):
            money.remove(b)
            return True
    return False 

def sonicHasHitMario(sonicRect, marios):
    for b in marios:
        if sonicRect.colliderect(b['rect']):
            return True
    return False


pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('World Tour')
pygame.mouse.set_visible(False)

font = pygame.font.SysFont(None, 70)
 
gameOverSound = pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('stones.mp3')
victorySound = pygame.mixer.Sound('blow.wav')
 
sonicImage = pygame.image.load('sonic.png')
sonicImageScaled = pygame.transform.scale(sonicImage, (200, 200))
sonicRect = sonicImageScaled.get_rect()
worldImage = pygame.image.load('planisfero.jpg')
milanImage = pygame.image.load('milan.jpg')
londonImage = pygame.image.load('london.jpg')
buenosAiresImage = pygame.image.load('buenos_aires.jpg')
newYorkImage = pygame.image.load('NYC.jpg')
tokyoImage = pygame.image.load('tokyo.jpg')
obstaclesImage = pygame.image.load('due_blocchi.png')
moneyImage = pygame.image.load('moneta.png')
marioImage = pygame.image.load('mario.png')
ormeImage = pygame.image.load('orme.png')
ormeImageScaled = pygame.transform.scale(ormeImage, (65, 65))
ormeRect = ormeImageScaled.get_rect()

moneyImageScaled = pygame.transform.scale(moneyImage, (40, 40))
moneyRect = pygame.Rect(1450, 122, 40, 40)


windowSurfaceRectangle = windowSurface.get_rect()
windowSurface.fill(BACKGROUNDCOLOR)
drawText ('WORLD TOUR', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3)) #misure???
drawText('Press a key to start.', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3) + 50) #misure??
pygame.display.update()
waitForPlayerToPressKey()

backgroundImage = pygame.image.load('planisfero.jpg')
backgroundStretchedImage = pygame.transform.scale(backgroundImage, (WINDOWWIDTH, WINDOWHEIGHT))
windowSurface.blit(backgroundStretchedImage, windowSurfaceRectangle)
pygame.display.update()
waitForPlayerToPressKey()

backgroundImage2 = pygame.image.load('milan.jpg')
backgroundStretchedImage2 = pygame.transform.scale(backgroundImage2, (WINDOWWIDTH, WINDOWHEIGHT))
drawTitles('MILAN ', font,backgroundStretchedImage2 , (WINDOWWIDTH -300),(WINDOWHEIGHT - 950))

windowSurface.blit(backgroundStretchedImage2, windowSurfaceRectangle)
pygame.display.update()

topScore = 0
win = False
while not win:
    obstacles = []
    timer = 0
    score = 0
    sonicRect.bottomleft = (50, 1000)
    moveLeft = moveRight = moveUp = moveDown = False
    obstaclesAddCounter = 0
    pygame.mixer.music.play(-1, 0.0)
   
    #1 livello
    while True: 
        timer +=1
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
                    moveDown = False

            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                        terminate()

                if event.key == K_LEFT or event.key == K_a:
                    moveRight =  moveUp = moveLeft = False
                    moveDown = True
                if event.key == K_RIGHT or event.key == K_d:
                    moveRight = moveUp =moveLeft = False
                    moveDown =  True
                if event.key == K_UP or event.key == K_w:
                    moveRight = moveUp = moveLeft =False
                    moveDown = True
                if event.key == K_DOWN or event.key == K_s:
                    moveRight = moveUp =moveLeft = False
                    moveDown =  True
                    
        if moveLeft and sonicRect.left > 0:
            sonicRect.move_ip(-1 * SONICMOVERATE, 0)
        if moveRight and sonicRect.right < WINDOWWIDTH:
            sonicRect.move_ip(SONICMOVERATE, 0)
        if moveUp and sonicRect.top > 0:
            sonicRect.move_ip(0, -1 * SONICMOVERATE)
        if moveDown and sonicRect.bottom < WINDOWHEIGHT:
            sonicRect.move_ip(0, SONICMOVERATE)            

        obstaclesAddCounter +=1
        if obstaclesAddCounter == OBSTACLESADDRATE:
            obstaclesAddCounter = 0
            obstaclesSize = random.randint(OBSTACLESMINSIZE, OBSTACLESMAXSIZE)
            newObstacles = {'rect': pygame.Rect(WINDOWWIDTH, WINDOWHEIGHT - obstaclesSize, obstaclesSize, obstaclesSize),
                        'speed': OBSTACLESSPEED,
                        'surface':pygame.transform.scale(obstaclesImage, (obstaclesSize, obstaclesSize)),
                        }

            obstacles.append(newObstacles)
            
        for b in obstacles:
            b['rect'].move_ip(-1*b['speed'],0)
            
        for b in obstacles[:]:
            if b['rect'].right < 0:
                obstacles.remove(b)
    
        windowSurface.blit(backgroundStretchedImage2, windowSurfaceRectangle)
        windowSurface.blit(sonicImageScaled, sonicRect)
       
        for b in obstacles:
            windowSurface.blit(b['surface'], b['rect'])
        pygame.display.update()
        
      
     
        if sonicHasHitObstacle( sonicRect , obstacles ):
            if score > topScore:
                topScore = score
            pygame.mixer.music.stop()
            gameOverSound.play()
            
            drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
            drawText('Press a key to play again.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
            pygame.display.update()
            waitForPlayerToPressKey() 
           
            
            break
        
        if timer == 800:
            
            pygame.mixer.music.stop()
            victorySound.play()
          
            drawText('YOU WIN!!', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
            drawText('Press a key to continue.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
            pygame.display.update()
            waitForPlayerToPressKey() 
            win = True
        
           
            break 
            
            
            
        mainClock . tick (FPS)
        pygame.display.update()
   
waitForPlayerToPressKey()  
gameOverSound.stop()
victorySound.stop()


money=[]

backgroundImage3 = pygame.image.load('london.jpg')
backgroundStretchedImage3 = pygame.transform.scale(backgroundImage3, (WINDOWWIDTH, WINDOWHEIGHT))
windowSurface.blit(backgroundStretchedImage3, windowSurfaceRectangle)
pygame.display.update()
waitForPlayerToPressKey() 

#2 livello
topScore = 0
win = False
moneyAddCounter=0
totMoney=0
while not win:
    money = []
    obstacles = []
    timer = 0
    score = 0
    sonicRect.bottomleft = (50, 1000)
    moveLeft = moveRight = moveUp = moveDown = False
    obstaclesAddCounter = 0
    pygame.mixer.music.play(-1, 0.0)
   
   
    while True: 
        timer +=1
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
                    moveDown = False

            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                        terminate()

                if event.key == K_LEFT or event.key == K_a:
                    moveRight =  moveUp = moveLeft = False
                    moveDown = True
                if event.key == K_RIGHT or event.key == K_d:
                    moveRight = moveUp =moveLeft = False
                    moveDown =  True
                if event.key == K_UP or event.key == K_w:
                    moveRight = moveUp = moveLeft =False
                    moveDown = True
                if event.key == K_DOWN or event.key == K_s:
                    moveRight = moveUp =moveLeft = False
                    moveDown =  True
                    
        if moveLeft and sonicRect.left > 0:
            sonicRect.move_ip(-1 * SONICMOVERATE, 0)
        if moveRight and sonicRect.right < WINDOWWIDTH:
            sonicRect.move_ip(SONICMOVERATE, 0)
        if moveUp and sonicRect.top > 0:
            sonicRect.move_ip(0, -1 * SONICMOVERATE)
        if moveDown and sonicRect.bottom < WINDOWHEIGHT:
            sonicRect.move_ip(0, SONICMOVERATE)        
            

        windowSurface.blit(backgroundStretchedImage3, windowSurfaceRectangle)
        drawTitles('LONDON', font,windowSurface , (WINDOWWIDTH -300),(WINDOWHEIGHT - 950))
        drawTitles('Money earned: %s' %( totMoney ),font,windowSurface , 10,(WINDOWHEIGHT - 950))
        drawTitles('Collect 5 money', font, backgroundStretchedImage3, 10,(WINDOWHEIGHT - 880))

        windowSurface.blit(sonicImageScaled, sonicRect)
            

        moneyAddCounter +=1
        if moneyAddCounter == MONEYADDRATE:
            moneyAddCounter = 0
            moneySize = MONEYSIZE
            newMoney = {'rect': pygame.Rect(WINDOWWIDTH, random.randint(0,WINDOWHEIGHT - moneySize), moneySize, moneySize),
                        'speed': MONEYSPEED,
                        'surface':pygame.transform.scale(moneyImage, (moneySize, moneySize)),
                        }

            money.append(newMoney)
            
        for b in money:
            b['rect'].move_ip(-1*b['speed'],0)
            
        for b in money[:]:
            if b['rect'].right < 0:
                money.remove(b)
       
        for b in money:
            windowSurface.blit(b['surface'], b['rect'])
#           
        
       
        obstaclesAddCounter +=1
        if obstaclesAddCounter == OBSTACLESADDRATE:
            obstaclesAddCounter = 0
            obstaclesSize = random.randint(OBSTACLESMINSIZE, OBSTACLESMAXSIZE)
            newObstacles = {'rect': pygame.Rect(WINDOWWIDTH, WINDOWHEIGHT - obstaclesSize, obstaclesSize, obstaclesSize),
                        'speed': OBSTACLESSPEED,
                        'surface':pygame.transform.scale(obstaclesImage, (obstaclesSize, obstaclesSize)),
                        }

            obstacles.append(newObstacles)
            
        for b in obstacles:
            b['rect'].move_ip(-1*b['speed'],0)
            
        for b in obstacles[:]:
            if b['rect'].right < 0:
                obstacles.remove(b)
    
       
       
        for b in obstacles:
            windowSurface.blit(b['surface'], b['rect'])
       
        
        
        pygame.display.update()
        
        
        if sonicHasHitMoney (sonicRect,money):
           totMoney +=1 
           
        
    
        
    
        if sonicHasHitObstacle( sonicRect , obstacles ):
            totMoney=0
            pygame.mixer.music.stop()
            gameOverSound.play()
            
            drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
            drawText('Press a key to play again.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
            pygame.display.update()
            waitForPlayerToPressKey() 
           
            
            break
        
        if totMoney == 5:  
            
            pygame.mixer.music.stop()
            victorySound.play()
          
            drawText('YOU WIN!!', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
            drawText('Press a key to continue.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
            pygame.display.update()
            waitForPlayerToPressKey() 
            win = True
        
           
            break 
            
            
            
        mainClock . tick (FPS)
        pygame.display.update()
        
        
#3 livello
backgroundImage5 = pygame.image.load('buenos_aires.jpg')
backgroundStretchedImage5 = pygame.transform.scale(backgroundImage5, (WINDOWWIDTH, WINDOWHEIGHT))
drawTitles('BUENOS AIRES', font,backgroundStretchedImage5 , (WINDOWWIDTH -450),(WINDOWHEIGHT - 950))
windowSurface.blit(backgroundStretchedImage5, windowSurfaceRectangle)

def disegnaLabirinto():
    pygame . draw . line ( windowSurface , TITLESCOLOR , (50,100) ,(1450,100) , 5)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (190,950) ,(1450,950) , 5)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (50,100) ,(50,950) , 5)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (1450,185) ,(1450,950) , 5)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (50,865) ,(190,865) , 4)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (190,865) ,(190,780) , 4)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (190,780) ,(750,780) , 4)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (750,865) ,(750,610) , 4)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (330,950) ,(330,865) , 4)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (330,865) ,(470,865) , 4)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (610,950) ,(610,865) , 4)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (890,950) ,(890,780) , 4)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (50,695) ,(330,695) , 4)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (470,695) ,(610,695) , 4)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (610,695) ,(610,610) , 4)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (610,610) ,(190,610) , 4)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (190,610) ,(190,525) , 4)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (190,525) ,(50,525) , 4)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (330,525) ,(750,525) , 4)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (750,525) ,(750,440) , 4)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (750,440) ,(890,440) , 4)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (470,525) ,(470,440) , 4)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (470,440) ,(190,440) , 4)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (190,440) ,(190,270) , 4)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (50,270) ,(330,270) , 4)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (330,270) ,(330,185) , 4)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (330,185) ,(190,185) , 4)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (330,355) ,(750,355) , 4)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (610,355) ,(610,440) , 4)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (470,355) ,(470,100) , 4)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (610,185) ,(610,270) , 4)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (610,270) ,(1030,270) , 4)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (1030,270) ,(1030,610) , 4)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (890,270) ,(890,355) , 4)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (1170,100) ,(1170,355) , 4)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (1170,185) ,(750,185) , 4)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (890,610) ,(890,525) , 4)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (890,525) ,(1310,525) , 4)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (890,695) ,(1030,695) , 4)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (1030,695) ,(1030,865) , 4)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (1030,865) ,(1450,865) , 4)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (1310,185) ,(1310,610) , 4)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (1310,610) ,(1170,610) , 4)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (1170,610) ,(1170,780) , 4)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (1170,780) ,(1310,780) , 4)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (1170,695) ,(1450,695) , 4)
    pygame . draw . line ( windowSurface , TITLESCOLOR , (1310,440) ,(1170,440) , 4)
    
    pygame.display.update()


topScore = 0
win = False
while not win:
    
    ormeRect.bottomleft = (87, 940)
    moveLeft = moveRight = moveUp = moveDown = False
    pygame.mixer.music.play(-1, 0.0)
    
    
    
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
    
        if moveDown and ormeRect.bottom < WINDOWHEIGHT and (windowSurface.get_at(ormeRect.bottomright) != TITLESCOLOR and windowSurface.get_at(ormeRect.bottomleft) != TITLESCOLOR):
            ormeRect.top = ormeRect.top + ORMEMOVERATE
            print(ormeRect.x, ormeRect.y)
        if moveUp and ormeRect.top > 0 and (windowSurface.get_at(ormeRect.topright) != TITLESCOLOR and windowSurface.get_at(ormeRect.topleft) != TITLESCOLOR):
            ormeRect.top = ormeRect.top - ORMEMOVERATE
            print(ormeRect.x, ormeRect.y)
        if moveLeft and ormeRect.left > 0 and (windowSurface.get_at(ormeRect.bottomleft) != TITLESCOLOR and windowSurface.get_at(ormeRect.topleft) != TITLESCOLOR):
            ormeRect.left = ormeRect.left - ORMEMOVERATE
            print(ormeRect.x, ormeRect.y)
        if moveRight and ormeRect.right < WINDOWWIDTH and (windowSurface.get_at(ormeRect.topright) != TITLESCOLOR and windowSurface.get_at(ormeRect.bottomright) != TITLESCOLOR):
            ormeRect.right = ormeRect.right + ORMEMOVERATE
            print(ormeRect.x, ormeRect.y)
            
            
        backgroundImage5 = pygame.image.load('buenos_aires.jpg')
        windowSurface.blit(backgroundStretchedImage5, windowSurfaceRectangle)
        disegnaLabirinto()
        windowSurface.blit(ormeImageScaled, ormeRect)
        windowSurface.blit(moneyImageScaled, moneyRect)
        
        if ormeRect.colliderect(moneyRect):
            pygame.mixer.music.stop()
            victorySound.play()
          
            drawText('YOU WIN!!', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
            drawText('Press a key to continue.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
            pygame.display.update()
            waitForPlayerToPressKey() 
            win = True
            break


        mainClock . tick (FPS)
        pygame.display.update()
   
waitForPlayerToPressKey()  
victorySound.stop()
        







pygame.display.update()











#4 livello 
backgroundImage4 = pygame.image.load('NYC.jpg')
backgroundStretchedImage4 = pygame.transform.scale(backgroundImage4, (WINDOWWIDTH, WINDOWHEIGHT))
#drawTitles('NEW YORK', font,backgroundStretchedImage4 , (WINDOWWIDTH -450),(WINDOWHEIGHT - 950))
#drawTitles('Money earned: %s' %( money ),font,backgroundStretchedImage4 , 10,(WINDOWHEIGHT - 950))
#drawTitles('Collect 10 money', font, backgroundStretchedImage4 , 10,(WINDOWHEIGHT - 880))
windowSurface.blit(backgroundStretchedImage4, windowSurfaceRectangle)
pygame.display.update()

topScore = 0
win = False
moneyAddCounter=0
totMoney=0
while not win:
    money = []
    obstacles = []
    timer = 0
    score = 0
    sonicRect.bottomleft = (50, 1000)
    moveLeft = moveRight = moveUp = moveDown = False
    obstaclesAddCounter = 0
    pygame.mixer.music.play(-1, 0.0)
   
   
    while True: 
        timer +=1
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
                    moveDown = False

            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                        terminate()

                if event.key == K_LEFT or event.key == K_a:
                    moveRight =  moveUp = moveLeft = False
                    moveDown = True
                if event.key == K_RIGHT or event.key == K_d:
                    moveRight = moveUp =moveLeft = False
                    moveDown =  True
                if event.key == K_UP or event.key == K_w:
                    moveRight = moveUp = moveLeft =False
                    moveDown = True
                if event.key == K_DOWN or event.key == K_s:
                    moveRight = moveUp =moveLeft = False
                    moveDown =  True
                    
        if moveLeft and sonicRect.left > 0:
            sonicRect.move_ip(-1 * SONICMOVERATE, 0)
        if moveRight and sonicRect.right < WINDOWWIDTH:
            sonicRect.move_ip(SONICMOVERATE, 0)
        if moveUp and sonicRect.top > 0:
            sonicRect.move_ip(0, -1 * SONICMOVERATE)
        if moveDown and sonicRect.bottom < WINDOWHEIGHT:
            sonicRect.move_ip(0, SONICMOVERATE)        
            
        #background
        windowSurface.blit(backgroundStretchedImage4, windowSurfaceRectangle)
        drawTitles('NEW YORK', font,backgroundStretchedImage4 , (WINDOWWIDTH -450),(WINDOWHEIGHT - 950))
        drawTitles('Money earned: %s' %( totMoney ),font,windowSurface , 10,(WINDOWHEIGHT - 950))
        drawTitles('Collect 10 money', font, backgroundStretchedImage4 , 10,(WINDOWHEIGHT - 880))
        #sonic
        windowSurface.blit(sonicImageScaled, sonicRect)
            
        #monetine
        moneyAddCounter +=1
        if moneyAddCounter == MONEYADDRATE:
            moneyAddCounter = 0
            moneySize = MONEYSIZE
            newMoney = {'rect': pygame.Rect(WINDOWWIDTH, random.randint(0,WINDOWHEIGHT - moneySize), moneySize, moneySize),
                        'speed': MONEYSPEED,
                        'surface':pygame.transform.scale(moneyImage, (moneySize, moneySize)),
                        }

            money.append(newMoney)
            
        for b in money:
            b['rect'].move_ip(-1*b['speed'],0)
            
        for b in money[:]:
            if b['rect'].right < 0:
                money.remove(b)
       
        for b in money:
            windowSurface.blit(b['surface'], b['rect'])
#            windowSurface.blit(pygame.transform.scale(moneyImage, (moneySize, moneySize)),
#                              pygame.Rect(WINDOWWIDTH, random.randint(0,WINDOWHEIGHT - moneySize), moneySize, moneySize))
#        
        
        #ostacoli
        obstaclesAddCounter +=1
        if obstaclesAddCounter == OBSTACLESADDRATE:
            obstaclesAddCounter = 0
            obstaclesSize = random.randint(OBSTACLESMINSIZE, OBSTACLESMAXSIZE)
            newObstacles = {'rect': pygame.Rect(WINDOWWIDTH, WINDOWHEIGHT - obstaclesSize, obstaclesSize, obstaclesSize),
                        'speed': OBSTACLESSPEED,
                        'surface':pygame.transform.scale(obstaclesImage, (obstaclesSize, obstaclesSize)),
                        }

            obstacles.append(newObstacles)
            
        for b in obstacles:
            b['rect'].move_ip(-1*b['speed'],0)
            
        for b in obstacles[:]:
            if b['rect'].right < 0:
                obstacles.remove(b)
    
       
       
        for b in obstacles:
            windowSurface.blit(b['surface'], b['rect'])
       
        
        #update finale
        pygame.display.update()
        
        if sonicHasHitMoney (sonicRect,money):
           totMoney +=1  
           
        
    
        
    
        if sonicHasHitObstacle( sonicRect , obstacles ):
            totMoney=0
            pygame.mixer.music.stop()
            gameOverSound.play()
            
            drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
            drawText('Press a key to play again.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
            pygame.display.update()
            waitForPlayerToPressKey() 
           
            
            break
        
        if totMoney==10 : 
            
            pygame.mixer.music.stop()
            victorySound.play()
          
            drawText('YOU WIN!!', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
            drawText('Press a key to continue.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
            pygame.display.update()
            waitForPlayerToPressKey() 
            win = True
        
           
            break 
            
            
            
        mainClock . tick (FPS)
        pygame.display.update()
        
        
        
        



#livello finale

backgroundImage6 = pygame.image.load('tokyo.jpg')
backgroundStretchedImage6 = pygame.transform.scale(backgroundImage6, (WINDOWWIDTH, WINDOWHEIGHT))
drawTitles('TOKYO ', font,backgroundStretchedImage6 , (WINDOWWIDTH -300),(WINDOWHEIGHT - 950))
windowSurface.blit(backgroundStretchedImage6, windowSurfaceRectangle)
pygame.display.update()

topScore = 0
while True:
    marios = []
    score = 0
    timer=0
    sonicRect.bottomleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    marioAddCounter = 0
    pygame.mixer.music.play(-1, 0.0)

    while True: 
        score += 1
        timer+=1# Increase score.

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

            if event.type == KEYUP:
               
                if event.key == K_ESCAPE:
                        terminate()

                if event.key == K_LEFT or event.key == K_a:
                    moveLeft = False
                if event.key == K_RIGHT or event.key == K_d:
                    moveRight = False
               

        marioAddCounter +=1   
        if marioAddCounter == ADDNEWMARIORATE:
            marioAddCounter = 0
            marioSize = random.randint(MARIOMINSIZE, MARIOMAXSIZE)
            newMario = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - marioSize), 0 - marioSize, marioSize, marioSize),
                        'speed': random.randint(MARIOMINSPEED, MARIOMAXSPEED),
                        'surface':pygame.transform.scale(marioImage, (marioSize, marioSize)),
                        }

            marios.append(newMario)

        # Move the player around.
        if moveLeft and sonicRect.left > 0:
            sonicRect.move_ip(-1 * SONICMOVERATE, 0)
        if moveRight and sonicRect.right < WINDOWWIDTH:
            sonicRect.move_ip(SONICMOVERATE, 0)
        

        # Move the baddies down.
        for b in marios:
                b['rect'].move_ip(0, b['speed'])

        # Delete baddies that have fallen past the bottom.
        for b in marios[:]:
            if b['rect'].top > WINDOWHEIGHT:
                marios.remove(b)

        # Draw the game world on the window.
        windowSurface.blit(backgroundStretchedImage6, windowSurfaceRectangle)

       
        

        # Draw the player's rectangle.
        
        windowSurface.blit(sonicImageScaled, sonicRect)

        # Draw each baddie.
        for b in marios:
            windowSurface.blit(b['surface'], b['rect'])

        pygame.display.update()
        
        
        if sonicHasHitMario( sonicRect , marios ):
               
            pygame.mixer.music.stop()
            mainClock.tick(FPS)
            gameOverSound.play()
            
            drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
            drawText('Press a key to play again.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
            pygame.display.update()
            waitForPlayerToPressKey()
            gameOverSound.stop()
           
           
            
            break


        if timer == 800:
            
            pygame.mixer.music.stop()
            mainClock.tick(FPS)
            victorySound.play()
          
            drawText('YOU WIN!!', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
 
            pygame.display.update()
            waitForPlayerToPressKey()
            victorySound.stop()
           
           
           
            break 
            
            
        pygame.display.update()


 


    

        
        
        
        
        
     
        






