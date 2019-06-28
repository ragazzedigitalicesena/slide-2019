#This is a  'Piovono hamburger' game
import pygame, sys, random
from pygame.locals import *

pygame.init()

def getImage(food):
    return pygame.image.load(food)

def getRect(image):
    return image.get_rect()

WINDOWWIDTH = 1200
WINDOWHEIGHT = 800
TEXTCOLOR = (127, 255, 212)
BACKGROUNDCOLOR = (0, 139, 139)
FPS1 = 60
FPS2 = 300
FPS3 = 360

background1Image = pygame.image.load('sfondoLivelloUno.jpg')
background1ImageR = background1Image.get_rect()
background2Image = pygame.image.load('sfondoLivelloDue.jpg')
background2ImageR = background2Image.get_rect()
background3Image = pygame.image.load('sfondoLivelloTre.jpg')
background3ImageR = background3Image.get_rect()

TACOSSIZE = 50
TACOSSPEED = 5
ADDNEWTACOSRATE = 4

tacodrillo = pygame.image.load('tacodrillo.png')
tacodrillo = tacodrillo.get_rect()

FOODSIZE = 50
FOODSPEED = 3
ADDNEWFOODRATE = 18

TOPBUNSIZE = 50
TOPBUNSPEED = 3
ADDNEWTOPBUNRATE = 6

BOTTOMBUNSIZE = 50
BOTTOMBUNSPEED = 3
ADDNEWBOTTOMBUNRATE = 6

BURGERSIZE = 50
BURGERSPEED  = 3
ADDNEWBURGERRATE = 6

PICKLESSIZE = 50
PICKLESSPEED = 3
ADDNEWPICKLESRATE = 4

CHEESESIZE = 50
CHEESESPEED = 3
ADDNEWCHEESERATE = 4

TOMATOESSIZE = 50
TOMATOESSPEED = 3
ADDNEWTOMATOESRATE = 4

ONIONSIZE = 50
ONIONSPEED = 3
ADDNEWONIONRATE = 4

SALADSIZE = 50
SALADSPEED = 3
ADDNEWSALADRATE = 4

PLAYERSMOVERATE = 5
Y_POSITION = 100
X_POSITION1 = 300
X_POSITION2 = 600
X_POSITION3 = 1000

PLAYERS_WIDTH = 100
PLAYERS_HEIGHT = 300
player1Image = pygame.Rect( X_POSITION1 , Y_POSITION ,PLAYERS_WIDTH , PLAYERS_HEIGHT )
player2Image = pygame.Rect( X_POSITION2 , Y_POSITION ,PLAYERS_WIDTH , PLAYERS_HEIGHT )
player3Image = pygame.Rect( X_POSITION3 , Y_POSITION ,PLAYERS_WIDTH , PLAYERS_HEIGHT )

player1Image = getImage('earlDevereaux.png')
player1Rect = getRect(player1Image)
player2Image = pygame.image.load('flintLockwood.png')
player2Rect = player2Image.get_rect()
player3Image = pygame.image.load('samSparks.png')
player3Rect = player3Image.get_rect()

topBunImage = pygame.image.load('paneSuperiore.png')
topBunRect = topBunImage.get_rect()
bottomBunImage = pygame.image.load('paneInferiore.png')
bottomBunRect = bottomBunImage.get_rect()
bottomBunStretchedImage = pygame . transform . scale ( bottomBunImage ,( 100 , 50 ))
burgerImage = pygame.image.load('carne.png')
burgerRect = burgerImage.get_rect()
picklesImage = pygame.image.load('cetriolini.png')
picklesRect = picklesImage.get_rect()
onionImage = pygame.image.load('cipolle.png')
onionRect = onionImage.get_rect()
cheeseImage = pygame.image.load('formaggio.png')
cheeseRect = cheeseImage.get_rect()
saladImage = pygame.image.load('insalata.png')
saladRect = saladImage.get_rect()
tomatoesImage = pygame.image.load('pomodori.png')
tomatoesRect = tomatoesImage.get_rect()

food1 = [bottomBunImage, burgerImage, topBunImage]
food2 = [bottomBunImage, cheeseImage, burgerImage, cheeseImage, tomatoesImage, saladImage, topBunImage]
food3 = [bottomBunImage, cheeseImage, burgerImage, tomatoesImage, cheeseImage, onionImage, picklesImage, saladImage, topBunImage]

hamburger1Image = pygame.image.load('hamburgerLivelloUno.png')
hamburger1Rect = hamburger1Image.get_rect()
hamburger1StretchedImage = pygame . transform . scale ( hamburger1Image ,( 100 , 100 ))
botBurImage = pygame.image.load('paneCarne.png')
botBurRect = botBurImage.get_rect()
botBurStretchedImage = pygame . transform . scale ( botBurImage ,( 100 , 75 ))

hamburger2Image = pygame.image.load('hamburgerLivelloDue.png')
hamburger2Rect= hamburger2Image.get_rect()
hamburger2StretchedImage = pygame . transform . scale ( hamburger2Image ,( 100 , 100 ))
botCheImage = pygame.image.load('paFo.png')
botCheRect = botCheImage.get_rect()
botCheStretchedImage = pygame . transform . scale ( botCheImage ,( 100 , 75 ))
botCheBurImage = pygame.image.load('paFoCa.png')
botCheBurRect = botCheBurImage.get_rect()
botCheBurStretchedImage = pygame . transform . scale ( botCheBurImage ,( 100 , 75 ))
botCheBurCheImage = pygame.image.load('paFoCaFo.png')
botCheBurCheRect = botCheBurCheImage.get_rect()
botCheBurCheStretchedImage = pygame . transform . scale ( botCheBurCheImage ,( 100 , 75 ))
botCheBurCheTomImage = pygame.image.load('paFoCaFoPo.png')
botCheBurCheTomRect = botCheBurCheTomImage.get_rect()
botCheBurCheTomStretchedImage = pygame . transform . scale ( botCheBurCheTomImage ,( 100 , 75 ))
botCheBurCheTomSaImage = pygame.image.load('paFoCaFoPoIn.png')
botCheBurCheTomSaRect = botCheBurCheTomSaImage.get_rect()
botCheBurCheTomSaStretchedImage = pygame . transform . scale ( botCheBurCheTomSaImage ,( 100 , 75 ))

hamburger3Image = pygame.image.load('hamburgerLivelloTre.png')
hamburger3Rect = hamburger3Image.get_rect()
hamburger3StretchedImage = pygame . transform . scale ( hamburger3Image ,( 100 , 100 ))
botCheImage = pygame.image.load('paFo.png')
botCheRect = botCheImage.get_rect()
botCheStretchedImage = pygame . transform . scale ( botCheImage ,( 100 , 75 ))
botCheBurImage = pygame.image.load('paFoCa.png')
botCheBurRect = botCheBurImage.get_rect()
botCheBurStretchedImage = pygame . transform . scale ( botCheBurImage ,( 100 , 75 ))
botCheBurTomImage = pygame.image.load('paFoCaPo.png')
botCheBurTomRect = botCheBurTomImage.get_rect()
botCheBurTomStretchedImage = pygame . transform . scale ( botCheBurTomImage ,( 100 , 75 ))
botCheBurTomBurImage = pygame.image.load('paFoCaPoCa.png')
botCheBurTomBurRect = botCheBurTomBurImage.get_rect()
botCheBurTomBurStretchedImage = pygame . transform . scale ( botCheBurTomBurImage ,( 100 , 75 ))
botCheBurTomBurCheImage = pygame.image.load('paFoCaPoCaFo.png')
botCheBurTomBurCheRect = botCheBurTomBurCheImage.get_rect()
botCheBurTomBurCheStretchedImage = pygame . transform . scale ( botCheBurTomBurCheImage ,( 100 , 75 ))
botCheBurTomBurCheOnImage = pygame.image.load('paFoCaPoCaFoCi.png')
botCheBurTomBurCheOnRect = botCheBurTomBurCheOnImage.get_rect()
botCheBurTomBurCheOnStretchedImage = pygame . transform . scale ( botCheBurTomBurCheOnImage ,( 100 , 75 ))
botCheBurTomBurCheOnPiImage = pygame.image.load('paFoCaPoCaFoCiCe.png')
botCheBurTomBurCheOnPiRect = botCheBurTomBurCheOnPiImage.get_rect()
botCheBurTomBurCheOnPiStretchedImage = pygame . transform . scale ( botCheBurTomBurCheOnPiImage ,( 100 , 75 ))
botCheBurTomBurCheOnPiSaImage = pygame.image.load('paFoCaPoCaFoCiCeIn.png')
botCheBurTomBurCheOnPiSaRect = botCheBurTomBurCheOnPiSaImage.get_rect()
botCheBurTomBurCheOnPiSaStretchedImage = pygame . transform . scale ( botCheBurTomBurCheOnPiSaImage ,( 100 , 75 ))

chosenPlayer= None
playersImages =  [player1Image, player2Image, player3Image]
playersNames=['Earl Devereaux', 'Flint Lockwood', 'Sam Sparks']
listOfPlayerRect=[player1Rect, player2Rect, player3Rect]

        
def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT: #quit = 'x' rossa della finestra
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # Pressing ESC quits.
                    terminate()
                return

def playerHasHitFood1(chosenPlayerRect, foodChosen):
    for b in foodChosen:
        if chosenPlayerRect.colliderect(b['rect']): #se è stato colpito un cibo
            if(b['indiceImmagine'] == 2 or b['indiceImmagine'] == 0 or b['indiceImmagine'] == 1): #se il cibo colpito è un burger (2) o un panino sopra (0)
                return b['indiceImmagine'] #restituisci la posizione del cibo all'interno di food1
    return -1

def playerHasHitFood2(chosenPlayerRect, foodChosen):
    for b in foodChosen:
        if chosenPlayerRect.colliderect(b['rect']): #se è stato colpito un cibo
            if(b['indiceImmagine'] == 0 or b['indiceImmagine'] == 1 or b['indiceImmagine'] == 2 or b['indiceImmagine'] == 3 or b['indiceImmagine'] == 4 or b['indiceImmagine'] == 5 or b['indiceImmagine'] == 6): #se il cibo colpito è un burger (2) o un panino sopra (0)
                return b['indiceImmagine'] #restituisci la posizione del cibo all'interno di food1
    return -1

def playerHasHitFood3(chosenPlayerRect, foodChosen):
    for b in foodChosen:
        if chosenPlayerRect.colliderect(b['rect']): #se è stato colpito un cibo
            if(b['indiceImmagine'] == 0 or b['indiceImmagine'] == 1 or b['indiceImmagine'] == 2 or b['indiceImmagine'] == 3 or b['indiceImmagine'] == 4 or b['indiceImmagine'] == 5 or b['indiceImmagine'] == 6 or b['indiceImmagine'] == 7 or b['indiceImmagine'] == 8 or b['indiceImmagine'] == 9): #se il cibo colpito è un burger (2) o un panino sopra (0)
                return b['indiceImmagine'] #restituisci la posizione del cibo all'interno di food1
    return -1

def checkHit(chosenPlayerRect, foodShown):
    for f in foodShown:
        if chosenPlayerRect.colliderect(f['rect']):
            foodShown.remove(f)
            return True
    return False

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Set up pygame, the window, and the mouse cursor.
pygame.init()
mainClock = pygame.time.Clock() #gestisce la velocità del gioco
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT),0,0)
pygame.display.set_caption('Piovono hamburger') #titolo della finestra, in alto

# Set up the fonts.
font = pygame.font.SysFont('broadway', 48)

# Show the "Start" screen.
windowSurface.fill(BACKGROUNDCOLOR)
drawText('Piovono hamburger', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
drawText('Press a key to start.', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3) + 50)
pygame.display.update()
waitForPlayerToPressKey()

player1StretchedImage = pygame.transform.scale (player1Image,(PLAYERS_WIDTH, PLAYERS_HEIGHT))
player2StretchedImage = pygame.transform.scale (player2Image,(PLAYERS_WIDTH, PLAYERS_HEIGHT))
player3StretchedImage = pygame.transform.scale (player3Image,(PLAYERS_WIDTH, PLAYERS_HEIGHT))

ciboDaColpire = 0

while True:
   
    windowSurface.fill(BACKGROUNDCOLOR)

    player1Rect.topleft = (50,300)
    player2Rect.topleft = (500,300)
    player3Rect.topleft = (1000,300)
    
    windowSurface.blit(player1StretchedImage, player1Rect)
    windowSurface.blit(player2StretchedImage, player2Rect)
    windowSurface.blit(player3StretchedImage, player3Rect)
    
    drawText('Scegli un giocatore e muovilo con le frecce laterali', font, windowSurface, (WINDOWWIDTH / 10), (WINDOWHEIGHT / 10))
    pygame.display.update()
    
    isChosen = False

#Livello 1    
    while isChosen == False:
        
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                
                pos = pygame.mouse.get_pos()
                if pos[0] > 50 and pos[0] < 150:
                    chosenPlayer = player1Image
                    isChosen = True
                    print("Giocatore1")
                if pos[0] > 500 and pos[0] < 600: 
                    chosenPlayer = player2Image
                    isChosen = True
                    print("Giocatore2")
                if pos[0] > 1000 and pos[0] < 1100: 
                    chosenPlayer = player3Image
                    isChosen = True
                    print("Giocatore3")
                
                
    backgroundStretchedImage = pygame . transform . scale ( background1Image ,( WINDOWWIDTH , WINDOWHEIGHT ))
    windowSurface . blit ( backgroundStretchedImage ,background1ImageR )
    windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect())

    soundLevel1 = pygame.mixer.music.load('SuperMario64(1).mp3')
    soundLevel1 = pygame.mixer.music.play()

    chosenStretchPlayer = pygame . transform . scale ( chosenPlayer ,( PLAYERS_WIDTH,PLAYERS_HEIGHT ))
    chosenPlayerRect = pygame.Rect(0,0,PLAYERS_WIDTH,PLAYERS_HEIGHT)
    chosenPlayerRect.bottomleft = (0,WINDOWHEIGHT)
    
    windowSurface.blit(chosenStretchPlayer, chosenPlayerRect)
    pygame.display.update()


    moveLeft = moveRight = False
    foodShown = []
    food1AddCounter = 0
    ciboDaColpire = 0
    finish=True
    while finish:
    
        for event in pygame.event.get():
           if event.type == QUIT:
               terminate()

           if event.type == KEYDOWN: #cosa fare quando l'utente preme il tasto
               if event.key == K_LEFT or event.key == K_a:
                   moveRight = False
                   moveLeft = True
               if event.key == K_RIGHT or event.key == K_d:
                   moveLeft = False
                   moveRight = True
           #KEYUP
           if event.type == KEYUP: #cosa fare quando l'utente preme il tasto
               if event.key == K_LEFT or event.key == K_a:
                   moveRight = False
                   moveLeft = False
               if event.key == K_RIGHT or event.key == K_d:
                   moveLeft = False
                   moveRight = False
                   
       
        # Move the player around.
        if moveLeft and chosenPlayerRect.left > 0:
            chosenPlayerRect.move_ip(-1 * PLAYERSMOVERATE, 0)
        if moveRight and chosenPlayerRect.right < WINDOWWIDTH:
            chosenPlayerRect.move_ip(PLAYERSMOVERATE, 0)
            
               # Move the baddies down.
        for b in foodShown:
            b['rect'].move_ip(0, b['speed'])
           

        # Delete baddies that have fallen past the bottom.
        for b in foodShown[:]:
            if b['rect'].top > WINDOWHEIGHT:
                foodShown.remove(b)
        
       
        food1AddCounter += 1
        if food1AddCounter == ADDNEWFOODRATE:
            food1AddCounter = 0
            food1Size = FOODSIZE
            indiceImmagineScelta = random.randint(0,2)
            randomFood1Image = food1[indiceImmagineScelta]
            newFood1 = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - food1Size), 0 - food1Size, food1Size, food1Size),
                        'speed': FOODSPEED,
                        'surface':pygame.transform.scale(randomFood1Image, (food1Size, food1Size)),
                        'indiceImmagine': indiceImmagineScelta,
                        }
            
            foodShown.append(newFood1)
        
      
        # Check if any of the baddies have hit the player.
        ciboColpito = playerHasHitFood1(chosenPlayerRect, foodShown)
       
        if checkHit(chosenPlayerRect, foodShown):
           
            if ciboColpito == ciboDaColpire:
            
                if ciboDaColpire == 2:
                
                    ciboDaColpire = 0
                
                if ciboDaColpire == 1:
                    
                    ciboDaColpire = 2
                    
                if ciboDaColpire == 0:
                   
                    ciboDaColpire = 1
            else:
                soundLosing = pygame.mixer.music.load('SuperMarioBrosDie.wav')
                soundLosing = pygame.mixer.music.play()
                drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
                drawText('Press a key to play again.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
                pygame.display.update()
                waitForPlayerToPressKey()

                backgroundStretchedImage = pygame . transform . scale ( background1Image ,( WINDOWWIDTH , WINDOWHEIGHT ))
                windowSurface . blit ( backgroundStretchedImage ,background1ImageR )
                windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect())
                
                soundLevel1 = pygame.mixer.music.load('SuperMario64(1).mp3')
                soundLevel1 = pygame.mixer.music.play()
                
                chosenStretchPlayer = pygame . transform . scale ( chosenPlayer ,( PLAYERS_WIDTH,PLAYERS_HEIGHT ))
                chosenPlayerRect = pygame.Rect(0,0,PLAYERS_WIDTH,PLAYERS_HEIGHT)
                chosenPlayerRect.bottomleft = (0,WINDOWHEIGHT)
                
                windowSurface.blit(chosenStretchPlayer, chosenPlayerRect)
                pygame.display.update()
                
                
                moveLeft = moveRight = False
                foodShown = []
                food1AddCounter = 0
                ciboDaColpire = 0

                ciboColpito = -1
        
         #sfondo normale
        windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect())
             
        if ciboDaColpire == 0:
            windowSurface.blit(bottomBunStretchedImage, bottomBunStretchedImage.get_rect())
       
        elif ciboDaColpire == 1:    
            windowSurface.blit(botBurStretchedImage, botBurStretchedImage.get_rect())
            
        elif ciboDaColpire == 2:
            windowSurface.blit(botBurStretchedImage, botBurStretchedImage.get_rect())
            

            
        
        
        if ciboColpito == 2:
           
            windowSurface.blit(hamburger1StretchedImage, hamburger1StretchedImage.get_rect())
            soundVictory = pygame.mixer.music.load('VICTORY(1).mp3')
            soundVictory = pygame.mixer.music.play()
            drawText('YOU ARE THE WINNER!', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
            drawText('Press a key to play the next level.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
            pygame.display.update()
            waitForPlayerToPressKey()
            finish =False
       
        
        # Draw each foodie.
        for b in foodShown:
           # print('b')
            windowSurface.blit(b['surface'], b['rect'])
            
        #giocatore
        windowSurface.blit(chosenStretchPlayer, chosenPlayerRect)
        pygame.display.update()
        
        mainClock.tick(FPS1)
    
    print('VITTORIA')
    
##Livello 2
    backgroundStretchedImage = pygame . transform . scale ( background2Image ,( WINDOWWIDTH , WINDOWHEIGHT ))
    windowSurface . blit ( backgroundStretchedImage ,background2ImageR )
    windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect())

    soundLevel2 = pygame.mixer.music.load('BigBlue(2).mp3')
    soundLevel2 = pygame.mixer.music.play()

    chosenStretchPlayer = pygame . transform . scale ( chosenPlayer ,( PLAYERS_WIDTH,PLAYERS_HEIGHT ))
    chosenPlayerRect = pygame.Rect(0,0,PLAYERS_WIDTH,PLAYERS_HEIGHT)
    chosenPlayerRect.bottomleft = (0,WINDOWHEIGHT)
    
    windowSurface.blit(chosenStretchPlayer, chosenPlayerRect)
    pygame.display.update()


    moveLeft = moveRight = False
    foodShown = []
    food2AddCounter = 0
    ciboDaColpire = 0
    
    while True:
    
        for event in pygame.event.get():
           if event.type == QUIT:
               terminate()

           if event.type == KEYDOWN: #cosa fare quando l'utente preme il tasto
               if event.key == K_LEFT or event.key == K_a:
                   moveRight = False
                   moveLeft = True
               if event.key == K_RIGHT or event.key == K_d:
                   moveLeft = False
                   moveRight = True
           #KEYUP
           if event.type == KEYUP: #cosa fare quando l'utente preme il tasto
               if event.key == K_LEFT or event.key == K_a:
                   moveRight = False
                   moveLeft = False
               if event.key == K_RIGHT or event.key == K_d:
                   moveLeft = False
                   moveRight = False
                   
       
        # Move the player around.
        if moveLeft and chosenPlayerRect.left > 0:
            chosenPlayerRect.move_ip(-1 * PLAYERSMOVERATE, 0)
        if moveRight and chosenPlayerRect.right < WINDOWWIDTH:
            chosenPlayerRect.move_ip(PLAYERSMOVERATE, 0)
            
               # Move the baddies down.
        for b in foodShown:
            b['rect'].move_ip(0, b['speed'])
           

        # Delete baddies that have fallen past the bottom.
        for b in foodShown[:]:
            if b['rect'].top > WINDOWHEIGHT:
                foodShown.remove(b)
        
       
        food2AddCounter += 1
        if food2AddCounter == ADDNEWFOODRATE:
            food2AddCounter = 0
            food2Size = FOODSIZE
            indiceImmagineScelta = random.randint(0,6)
            randomFood2Image = food2[indiceImmagineScelta]
            newFood2 = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - food2Size), 0 - food2Size, food2Size, food2Size),
                        'speed': FOODSPEED,
                        'surface':pygame.transform.scale(randomFood2Image, (food2Size, food2Size)),
                        'indiceImmagine': indiceImmagineScelta,
                        }
            
            foodShown.append(newFood2)
        
      
        # Check if any of the baddies have hit the player.
        ciboColpito = playerHasHitFood2(chosenPlayerRect, foodShown)
       
        if checkHit(chosenPlayerRect, foodShown):
           
            if ciboColpito == ciboDaColpire:
                if ciboDaColpire == 6:
                    ciboDaColpire = 0
                
                if ciboDaColpire == 5:
                    ciboDaColpire = 6                
                
                if ciboDaColpire == 4:                    
                    ciboDaColpire = 5
                    
                if ciboDaColpire == 3:                   
                    ciboDaColpire = 4
                
                if ciboDaColpire == 2:                
                    ciboDaColpire = 3
                
                if ciboDaColpire == 1:
                    ciboDaColpire = 2
                    
                if ciboDaColpire == 0:                   
                    ciboDaColpire = 1
            else:
                soundLosing = pygame.mixer.music.load('SuperMarioBrosDie.wav')
                soundLosing = pygame.mixer.music.play()
                drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
                drawText('Press a key to play again.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
                pygame.display.update()
                waitForPlayerToPressKey()
                
                backgroundStretchedImage = pygame . transform . scale ( background2Image ,( WINDOWWIDTH , WINDOWHEIGHT ))
                windowSurface . blit ( backgroundStretchedImage ,background2ImageR )
                windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect())
            
                soundLevel2 = pygame.mixer.music.load('BigBlue(2).mp3')
                soundLevel2 = pygame.mixer.music.play()
            
                chosenStretchPlayer = pygame . transform . scale ( chosenPlayer ,( PLAYERS_WIDTH,PLAYERS_HEIGHT ))
                chosenPlayerRect = pygame.Rect(0,0,PLAYERS_WIDTH,PLAYERS_HEIGHT)
                chosenPlayerRect.bottomleft = (0,WINDOWHEIGHT)
                
                windowSurface.blit(chosenStretchPlayer, chosenPlayerRect)
                pygame.display.update()
            
            
                moveLeft = moveRight = False
                foodShown = []
                food2AddCounter = 0
                ciboDaColpire = 0
                
                ciboColpito = -1
        
         #sfondo normale
        windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect())
             
        if ciboDaColpire == 0:
            windowSurface.blit(bottomBunStretchedImage, bottomBunStretchedImage.get_rect())
       
        elif ciboDaColpire == 1:    
            windowSurface.blit(botCheStretchedImage, botCheStretchedImage.get_rect())
            
        elif ciboDaColpire == 2:
            windowSurface.blit(botCheBurStretchedImage, botCheBurStretchedImage.get_rect())
        
        elif ciboDaColpire == 3:
            windowSurface.blit(botCheBurCheStretchedImage, botCheBurCheStretchedImage.get_rect())
       
        elif ciboDaColpire == 4:    
            windowSurface.blit(botCheBurCheTomStretchedImage, botCheBurCheTomStretchedImage.get_rect())
            
        elif ciboDaColpire == 5:
            windowSurface.blit(botCheBurCheTomSaStretchedImage, botCheBurCheTomSaStretchedImage.get_rect())
            
        elif ciboDaColpire == 6:
            windowSurface.blit(hamburger2StretchedImage, hamburger2StretchedImage.get_rect())
            

            
        
        
        if ciboColpito == 6:
           
            windowSurface.blit(hamburger2StretchedImage, hamburger2StretchedImage.get_rect())
            soundVictory = pygame.mixer.music.load('VICTORY(1).mp3')
            soundVictory = pygame.mixer.music.play()
            drawText('YOU ARE THE WINNER!', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
            drawText('Press a key to play the next level.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
            pygame.display.update()
            waitForPlayerToPressKey()
            break
       
        
        # Draw each foodie.
        for b in foodShown:
           # print('b')
            windowSurface.blit(b['surface'], b['rect'])
            
        #giocatore
        windowSurface.blit(chosenStretchPlayer, chosenPlayerRect)
        pygame.display.update()
        
        mainClock.tick(FPS2)
    
    print('VITTORIA')
            

#Livello 3
    backgroundStretchedImage = pygame . transform . scale ( background3Image ,( WINDOWWIDTH , WINDOWHEIGHT ))
    windowSurface . blit ( backgroundStretchedImage ,background3ImageR )
    windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect())

    soundLevel3 = pygame.mixer.music.load('KingDDD(3).mp3')
    soundLevel3 = pygame.mixer.music.play()

    chosenStretchPlayer = pygame . transform . scale ( chosenPlayer ,( PLAYERS_WIDTH,PLAYERS_HEIGHT ))
    chosenPlayerRect = pygame.Rect(0,0,PLAYERS_WIDTH,PLAYERS_HEIGHT)
    chosenPlayerRect.bottomleft = (0,WINDOWHEIGHT)
    
    windowSurface.blit(chosenStretchPlayer, chosenPlayerRect)
    pygame.display.update()


    moveLeft = moveRight = False
    foodShown = []
    food3AddCounter = 0
    ciboDaColpire = 0
    
    while True:
    
        for event in pygame.event.get():
           if event.type == QUIT:
               terminate()

           if event.type == KEYDOWN: #cosa fare quando l'utente preme il tasto
               if event.key == K_LEFT or event.key == K_a:
                   moveRight = False
                   moveLeft = True
               if event.key == K_RIGHT or event.key == K_d:
                   moveLeft = False
                   moveRight = True
           #KEYUP
           if event.type == KEYUP: #cosa fare quando l'utente preme il tasto
               if event.key == K_LEFT or event.key == K_a:
                   moveRight = False
                   moveLeft = False
               if event.key == K_RIGHT or event.key == K_d:
                   moveLeft = False
                   moveRight = False
                   
       
        # Move the player around.
        if moveLeft and chosenPlayerRect.left > 0:
            chosenPlayerRect.move_ip(-1 * PLAYERSMOVERATE, 0)
        if moveRight and chosenPlayerRect.right < WINDOWWIDTH:
            chosenPlayerRect.move_ip(PLAYERSMOVERATE, 0)
            
               # Move the baddies down.
        for b in foodShown:
            b['rect'].move_ip(0, b['speed'])
           

        # Delete baddies that have fallen past the bottom.
        for b in foodShown[:]:
            if b['rect'].top > WINDOWHEIGHT:
                foodShown.remove(b)
        
       
        food3AddCounter += 1
        if food3AddCounter == ADDNEWFOODRATE:
            food3AddCounter = 0
            food3Size = FOODSIZE
            indiceImmagineScelta = random.randint(0,8)
            randomFood3Image = food3[indiceImmagineScelta]
            newFood3 = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - food3Size), 0 - food3Size, food3Size, food3Size),
                        'speed': FOODSPEED,
                        'surface':pygame.transform.scale(randomFood3Image, (food3Size, food3Size)),
                        'indiceImmagine': indiceImmagineScelta,
                        }
            
            foodShown.append(newFood3)
        
      
        # Check if any of the baddies have hit the player.
        ciboColpito = playerHasHitFood3(chosenPlayerRect, foodShown)
       
        if checkHit(chosenPlayerRect, foodShown):
           
            if ciboColpito == ciboDaColpire:
                if ciboDaColpire == 9:
                    ciboDaColpire = 0
                    
                if ciboDaColpire == 8:
                    ciboDaColpire = 9
                    
                if ciboDaColpire == 7:                   
                    ciboDaColpire = 8
                    
                if ciboDaColpire == 6:
                    ciboDaColpire = 7
                
                if ciboDaColpire == 5:
                    ciboDaColpire = 6                
                
                if ciboDaColpire == 4:                    
                    ciboDaColpire = 5
                    
                if ciboDaColpire == 3:                   
                    ciboDaColpire = 4
                
                if ciboDaColpire == 2:                
                    ciboDaColpire = 3
                
                if ciboDaColpire == 1:
                    ciboDaColpire = 2
                    
                if ciboDaColpire == 0:                   
                    ciboDaColpire = 1
                    
            else:
                soundLosing = pygame.mixer.music.load('SuperMarioBrosDie.wav')
                soundLosing = pygame.mixer.music.play()
                drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
                drawText('Press a key to play again.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
                pygame.display.update()
                waitForPlayerToPressKey()
                
                backgroundStretchedImage = pygame . transform . scale ( background3Image ,( WINDOWWIDTH , WINDOWHEIGHT ))
                windowSurface . blit ( backgroundStretchedImage ,background3ImageR )
                windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect())
            
                soundLevel3 = pygame.mixer.music.load('KingDDD(3).mp3')
                soundLevel3 = pygame.mixer.music.play()
            
                chosenStretchPlayer = pygame . transform . scale ( chosenPlayer ,( PLAYERS_WIDTH,PLAYERS_HEIGHT ))
                chosenPlayerRect = pygame.Rect(0,0,PLAYERS_WIDTH,PLAYERS_HEIGHT)
                chosenPlayerRect.bottomleft = (0,WINDOWHEIGHT)
                
                windowSurface.blit(chosenStretchPlayer, chosenPlayerRect)
                pygame.display.update()
            
            
                moveLeft = moveRight = False
                foodShown = []
                food3AddCounter = 0
                ciboDaColpire = 0
                
                ciboColpito = -1
        
         #sfondo normale
        windowSurface.blit(backgroundStretchedImage, backgroundStretchedImage.get_rect())
             
        if ciboDaColpire == 0:
            windowSurface.blit(bottomBunStretchedImage, bottomBunStretchedImage.get_rect())
       
        elif ciboDaColpire == 1:    
            windowSurface.blit(botCheStretchedImage, botCheStretchedImage.get_rect())
            
        elif ciboDaColpire == 2:
            windowSurface.blit(botCheBurStretchedImage, botCheBurStretchedImage.get_rect())
        
        elif ciboDaColpire == 3:
            windowSurface.blit(botCheBurTomStretchedImage, botCheBurTomStretchedImage.get_rect())
       
        elif ciboDaColpire == 4:    
            windowSurface.blit(botCheBurTomBurStretchedImage, botCheBurTomBurStretchedImage.get_rect())
            
        elif ciboDaColpire == 5:
            windowSurface.blit(botCheBurTomBurCheStretchedImage, botCheBurTomBurCheStretchedImage.get_rect())
            
        elif ciboDaColpire == 6:
            windowSurface.blit(botCheBurTomBurCheOnStretchedImage, botCheBurTomBurCheOnStretchedImage.get_rect())
        
        elif ciboDaColpire == 7:    
            windowSurface.blit(botCheBurTomBurCheOnPiStretchedImage, botCheBurTomBurCheOnPiStretchedImage.get_rect())
            
        elif ciboDaColpire == 8:
            windowSurface.blit(botCheBurTomBurCheOnPiSaStretchedImage, botCheBurTomBurCheOnPiSaStretchedImage.get_rect())
            
        elif ciboDaColpire == 9:
            windowSurface.blit(hamburger3StretchedImage, hamburger3StretchedImage.get_rect())
            

            
        
        
        if ciboColpito == 9:
           
            windowSurface.blit(hamburger3StretchedImage, hamburger3StretchedImage.get_rect())
            soundVictory = pygame.mixer.music.load('VICTORY(1).mp3')
            soundVictory = pygame.mixer.music.play()
            drawText('YOU ARE THE WINNER!', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
            drawText('Congratulazioni! Hai finito questo gioco!', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
            pygame.display.update()
            waitForPlayerToPressKey()
            break
       
        
        # Draw each foodie.
        for b in foodShown:
           # print('b')
            windowSurface.blit(b['surface'], b['rect'])
            
        #giocatore
        windowSurface.blit(chosenStretchPlayer, chosenPlayerRect)
        pygame.display.update()
        
        mainClock.tick(FPS3)
    
    print('VITTORIA')
            

                        
    
    
pygame.display.update()
