#IMPORT
import pygame, sys, random
from pygame.locals import *
import time

#FUNZIONI DEL DE BELLO CIVILI

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
def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, WHITE)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)   
    return
def drawText1(text, font, surface, x, y):
    textobj = font.render(text, 1, BLACK)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)   
    return

#FUNZIONI GIOCO 1
def checkTheAnswer():
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
             return str(chr(event.key))
                      
#FUNZIONI GIOCO 2
            
def playerHasHitBaddie(playerRect, baddies):
    for b in baddies:
        if playerRect.colliderect(b['rect']):
            baddies.remove(b)
            return True
    return False

def playerHasHitGoodie(playerRect, goodies):
    for g in goodies:
        if playerRect.colliderect(g['rect']):
            goodies.remove(g)
            return True
    return False


#CARATTERISTICHE FINESTRA           

pygame.init()
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 1000

WHITE=(255,255,255)
BLACK=(0,0,0)
AZZURRO=(142,250,227)

font= pygame.font.SysFont(None, 48)

mainClock = pygame.time.Clock()
windowSurface=pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('NOME DEL GIOCO')
pygame.mouse.set_visible(True)

#FRASI CIVILI GIOCO 1
correctAnswer = ['Sei un chimico provetto!', 'Ti piace la chimica eh?','Bravo chimico!','Grande!','Vero, certamente!','Continua così'] 
wrongAnswer = ['Questa è un\'ironia che non mi piace', 'Errare humanum est, perseverare diabolicum.', 'Sono seriamente preoccupato per l\' esito di questo quiz.','Mh..sembra che tu non abbia studiato','Devi studiare i più','Questa è sbagliata!']   
nCorrectAnswer1=random.randint(0,len(correctAnswer)-1)
nCorrectAnswer2=random.randint(0,len(correctAnswer)-1)
nCorrectAnswer3=random.randint(0,len(correctAnswer)-1)
nCorrectAnswer4=random.randint(0,len(correctAnswer)-1)
nCorrectAnswer5=random.randint(0,len(correctAnswer)-1)

nWrongAnswer1=random.randint(0, len(wrongAnswer)-1)
nWrongAnswer2=random.randint(0, len(wrongAnswer)-1)
nWrongAnswer3=random.randint(0, len(wrongAnswer)-1)
nWrongAnswer4=random.randint(0, len(wrongAnswer)-1)
nWrongAnswer5=random.randint(0, len(wrongAnswer)-1)


#SFONDO GIOCO 1
backgroundImage=pygame.image.load('schermata_iniziale.jpg')
backgroundStrechedImage=pygame.transform.scale(backgroundImage, (WINDOW_WIDTH, WINDOW_HEIGHT))
windowSurfaceRectangle=windowSurface.get_rect()

#CARATTERISTICHE BADDIE E GOODIE
FPS = 60
SIZE=50
BADDIEMINSPEED = 4 
BADDIEMAXSPEED = 10
GOODIEMINSPEED= 4
GOODIEMAXSPEED= 10
ADDNEWBADDIERATE = 10
ADDNEWGOODIERATE= 15
PLAYERMOVERATE = 5
PLAYER_WIDTH=100
PLAYER_HEIGHT=150
PLAYER_WIDTH1=600
PLAYER_HEIGHT1=800

#IMMAGINI GIOCO 2
sfondoAula=pygame.image.load('sfondo-aula.jpg')
playerImage = pygame.image.load('Scientist-Transparent.png')
baddieImage1 = pygame.image.load('radiation.png')
baddieImage2 = pygame.image.load('simbolo_velenoso.png')
goodieImage1=pygame.image.load('beutapng.png')
goodieImage2=pygame.image.load('provetta-png.png')
goodieImage3=pygame.image.load('termometro.png')

playerRect = playerImage.get_rect() 
baddieImage1Rect=baddieImage1.get_rect()
baddieImage2Rect=baddieImage2.get_rect()
goodieImage1Rect=goodieImage1.get_rect()
goodieImage2Rect=goodieImage2.get_rect()
goodieImage3Rect=goodieImage3.get_rect()

playerStretchedImage=pygame.transform.scale(playerImage,(PLAYER_WIDTH, PLAYER_HEIGHT))
playerStretchedImage1=pygame.transform.scale(playerImage,(PLAYER_WIDTH1, PLAYER_HEIGHT1))
baddieStretchedImage1=pygame.transform.scale(baddieImage1,(SIZE,SIZE))
baddieStretchedImage2=pygame.transform.scale(baddieImage2,(SIZE,SIZE))
goodieStretchedImage1=pygame.transform.scale(goodieImage1,(SIZE,SIZE))
goodieStretchedImage2=pygame.transform.scale(goodieImage2,(SIZE,SIZE))
goodieStretchedImage3=pygame.transform.scale(goodieImage3,(SIZE,SIZE))

playerRect = playerStretchedImage.get_rect()
playerRect1 = playerStretchedImage1.get_rect()
baddieImage1Rect = baddieStretchedImage1.get_rect()
baddieImage2Rect = baddieStretchedImage2.get_rect()
goodieImage1Rect = goodieStretchedImage1.get_rect()
goodieImage2Rect = goodieStretchedImage2.get_rect()
goodieImage3Rect = goodieStretchedImage3.get_rect()

baddieImage=[baddieImage1, baddieImage2]
goodieImage=[goodieImage1,goodieImage2,goodieImage3]


baddieStretchedImage=[baddieStretchedImage1,baddieStretchedImage2]
goodieStretchedImage=[goodieStretchedImage1,goodieStretchedImage2,goodieStretchedImage3]

baddieImageRect=[baddieImage1Rect,baddieImage2Rect]
goodieImageRect=[goodieImage1Rect,goodieImage2Rect,goodieImage3Rect]






#IMMAGINI GIOCO 3
hangman1=pygame.image.load('impiccato1.png')
hangman2=pygame.image.load('impiccato2.png')
hangman3=pygame.image.load('impiccato3.png')
hangman4=pygame.image.load('impiccato4.png')
hangman5=pygame.image.load('impiccato5.png')
hangman6=pygame.image.load('impiccato6.png')
hangman7=pygame.image.load('impiccato7.png')
hangman8=pygame.image.load('impiccato8.png')
hangman9=pygame.image.load('impiccato9.png')
hangman10=pygame.image.load('impiccato10.png')

#SCHERMATA INIZIALE


#SFONDO GIOCO2

sfondoAulaStretchedImage=pygame.transform.scale(sfondoAula, (WINDOW_WIDTH, WINDOW_HEIGHT))
windowSurface.blit(sfondoAulaStretchedImage ,windowSurfaceRectangle )


#CARATTERISTICHE CIVILI
X_POSITION = 0
Y_POSITION = WINDOW_HEIGHT/3
Y_POSITION1 = WINDOW_HEIGHT+300
PROF_WIDTH=300
PROF_HEIGHT=438
PROF_WIDTH1=00
PROF_HEIGHT1=800
prof = pygame.Rect(X_POSITION, Y_POSITION, PROF_WIDTH, PROF_HEIGHT)
prof1 = pygame.Rect(X_POSITION, Y_POSITION1, PROF_WIDTH1, PROF_HEIGHT1)

windowSurface.fill(AZZURRO)
windowSurface.blit(playerStretchedImage1, playerRect)
drawText('Benvenuti,',font, windowSurface, 700,200)
drawText('questo è il Richard The Scientist Game.',font, windowSurface, 700,300)
drawText('Buon divertimento!',font, windowSurface, 700,400)
pygame.display.update()

waitForPlayerToPressKey()
pygame.display.update()
#GIOCO 1

windowSurface.blit(backgroundStrechedImage, windowSurfaceRectangle)
text1=['Buongiorno chimico!','Prima di andare in laboratorio, devo assicurarmi che tu abbia studiato.','Devi rispondere a 5 domande che ti farò.','(Premi sulla tastiera la lettera corrispondente alla tua risposta.)']
drawText(text1[0] ,font, windowSurface, 100,200)
drawText(text1[1], font, windowSurface, 100,250)
drawText(text1[2], font, windowSurface, 100,300)
drawText(text1[3], font, windowSurface, 100,350)
pygame.display.update()

score=0
waitForPlayerToPressKey()

while True:    
    for event in pygame.event.get(): 
        if event.type==QUIT:
            terminate()
    
    windowSurface.blit(backgroundStrechedImage, windowSurfaceRectangle)
    text2=['1- Qual è la formula del solfato rameico?', 'a- Cu(SO4)3', 'b- Cu(SO4)2','c- CuSO4','d- Cu2SO4']
    drawText(text2[0] ,font, windowSurface, 100,200)
    drawText(text2[1], font, windowSurface, 100,250)
    drawText(text2[2], font, windowSurface, 100,300)
    drawText(text2[3], font, windowSurface, 100,350)
    drawText(text2[4], font, windowSurface, 100,400)
    pygame.display.update()
    
    answer=checkTheAnswer()
    
   
    if answer == 'c':  
        drawText(correctAnswer[nCorrectAnswer1], font,windowSurface,100, windowSurface.get_rect().centery)
        score = score + 100
        drawText('Punteggio: ' + str(score), font,windowSurface,100, windowSurface.get_rect().centery + 100)
    else:
        drawText(wrongAnswer[nWrongAnswer1], font, windowSurface,100, windowSurface.get_rect().centery)
        drawText('Punteggio: '+ str(score), font,windowSurface,100, windowSurface.get_rect().centery + 100)
    pygame.display.update()
    waitForPlayerToPressKey()
     
    windowSurface.blit(backgroundStrechedImage, windowSurfaceRectangle)
    text3=['2- Qual è il numero di ossidazione dell\'ossigeno nei perossidi?','a- -2','b- -1','c- -1/2', 'd- +1']
    drawText(text3[0] ,font, windowSurface, 100,200)
    drawText(text3[1], font, windowSurface, 100,250)
    drawText(text3[2], font, windowSurface, 100,300)
    drawText(text3[3], font, windowSurface, 100,350)
    drawText(text3[4], font, windowSurface, 100,400)
    pygame.display.update()
    
    answer=checkTheAnswer()
    print(answer)
     
    if answer == 'b':
        drawText(correctAnswer[nCorrectAnswer2], font,windowSurface, 100, windowSurface.get_rect().centery)
        score = score + 100
        drawText('Punteggio: '+str(score), font,windowSurface,100, windowSurface.get_rect().centery + 100)
    else:         
        drawText(wrongAnswer[nWrongAnswer2], font, windowSurface, 100, windowSurface.get_rect().centery)
        drawText('Punteggio: '+str(score), font,windowSurface,100, windowSurface.get_rect().centery + 100)
    pygame.display.update() 
    waitForPlayerToPressKey()
     
    windowSurface.blit(backgroundStrechedImage, windowSurfaceRectangle)
    text4=['3- In una mole di azoto (N2) (MM=28u) quanti atomi ci sono?','a- 12,044 * 10^23','b- 6,022 * 10^23','c- 28', 'd- 2']
    drawText(text4[0] ,font, windowSurface, 100,200)
    drawText(text4[1], font, windowSurface, 100,250)
    drawText(text4[2], font, windowSurface, 100,300)
    drawText(text4[3], font, windowSurface, 100,350)
    drawText(text4[4], font, windowSurface, 100,400)
    pygame.display.update()
    
    answer=checkTheAnswer()
    print(answer)
     
    if answer == 'a':
        drawText(correctAnswer[nCorrectAnswer3], font,windowSurface, 100, windowSurface.get_rect().centery)
        score = score + 100
        drawText('Punteggio: '+str(score), font,windowSurface,100, windowSurface.get_rect().centery + 100)
    else:         
        drawText(wrongAnswer[nWrongAnswer3], font, windowSurface, 100, windowSurface.get_rect().centery)
        drawText('Punteggio: '+str(score), font,windowSurface,100, windowSurface.get_rect().centery + 100)
    pygame.display.update() 
    waitForPlayerToPressKey()
     
    windowSurface.blit(backgroundStrechedImage, windowSurfaceRectangle)
    text5=['4- Scegli l\'affermazione errata.', 'L\'agente ossidante:','a- Si riduce','b- Acquista elettroni','c- Aumenta il proprio numero di ossidazione']
    drawText(text5[0] ,font, windowSurface, 100,200)
    drawText(text5[1], font, windowSurface, 100,250)
    drawText(text5[2], font, windowSurface, 100,300)
    drawText(text5[3], font, windowSurface, 100,350)
    drawText(text5[4], font, windowSurface, 100,400)
    pygame.display.update()
    
    answer=checkTheAnswer()
    print(answer)
     
    if answer == 'c':
        drawText(correctAnswer[nCorrectAnswer4], font,windowSurface, 100, windowSurface.get_rect().centery)
        score = score + 100
        drawText('Punteggio: '+str(score), font,windowSurface,100, windowSurface.get_rect().centery + 100)
    else:         
        drawText(wrongAnswer[nWrongAnswer4], font, windowSurface, 100, windowSurface.get_rect().centery)
        drawText('Punteggio: '+str(score), font,windowSurface,100, windowSurface.get_rect().centery + 100)
    pygame.display.update() 
    waitForPlayerToPressKey()
     
    windowSurface.blit(backgroundStrechedImage, windowSurfaceRectangle)
    text6=['5- Qual è la formula della molarità(M)?','a- n/m(solvente)','b- n/m(solvente)','c- n/V(solvente)', 'd- n/V(soluzione)']
    drawText(text6[0] ,font, windowSurface, 100,200)
    drawText(text6[1], font, windowSurface, 100,250)
    drawText(text6[2], font, windowSurface, 100,300)
    drawText(text6[3], font, windowSurface, 100,350)
    drawText(text6[4], font, windowSurface, 100,400)
    pygame.display.update()
    
    answer=checkTheAnswer()
    print(answer)
     
    if answer == 'd':
        drawText(correctAnswer[nCorrectAnswer5], font,windowSurface, 100, windowSurface.get_rect().centery)
        score = score + 100
       
    else:         
        drawText(wrongAnswer[nWrongAnswer5], font, windowSurface, 100, windowSurface.get_rect().centery)
    pygame.display.update()
    
    waitForPlayerToPressKey()    
    windowSurface.blit(backgroundStrechedImage, windowSurfaceRectangle)
    drawText('Punteggio: '+str(score), font,windowSurface,100, windowSurface.get_rect().centery-100)    
    if score>=300:
        drawText('Complimenti chimico! Ma non è ancora finita...', font,windowSurface,100, windowSurface.get_rect().centery)   
    else:
        drawText('Non hai studiato abbastanza.', font,windowSurface,100, windowSurface.get_rect().centery) 
        drawText('Dovrai impegnarti molto nella prossima prova.', font,windowSurface,100, windowSurface.get_rect().centery + 100)
    pygame.display.update() 
    
    
    #GIOCO 2
    waitForPlayerToPressKey()
 
    windowSurface.blit( sfondoAulaStretchedImage ,windowSurfaceRectangle )
    drawText1('Raccogli gli strumenti che ti serviranno nel laboratorio', font, windowSurface, (WINDOW_WIDTH / 6), (WINDOW_HEIGHT / 3))
    drawText1('ed evita le sostanze tossiche', font, windowSurface, (WINDOW_WIDTH / 5), (WINDOW_HEIGHT / 3)+50)
    drawText1('Premi un tasto per iniziare.', font, windowSurface, (WINDOW_WIDTH / 3) - 30, (WINDOW_HEIGHT / 3) + 100)
    pygame.display.update()
    
    score = 0
    life=3
    baddies = []
    goodies = []
    playerRect.topleft = (550,650)
    moveLeft = moveRight = moveUp = moveDown = False
    
    baddieAddCounter = 0
    goodieAddCounter= 0

    waitForPlayerToPressKey()  
    while True:

        windowSurface.blit( sfondoAulaStretchedImage ,windowSurfaceRectangle )
        windowSurface.blit(playerStretchedImage, playerRect)
        
        drawText1('Punteggio:  '+str(score), font, windowSurface, 10, 0)
        drawText1('Vite:  '+str(life), font, windowSurface, 10, 50)
          
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
                    
        baddieAddCounter +=1    
        if baddieAddCounter == ADDNEWBADDIERATE:
            baddieAddCounter = 0
            randomBaddieImage = baddieImage[random.randint(0,1)]
            newBaddie = {'rect': pygame.Rect(random.randint(0, WINDOW_WIDTH - SIZE), 0 - SIZE, SIZE, SIZE),
                        'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                        'surface':pygame.transform.scale(randomBaddieImage, (SIZE, SIZE))}

            baddies.append(newBaddie)
            
        goodieAddCounter +=1    
        if goodieAddCounter == ADDNEWGOODIERATE:
            goodieAddCounter= 0
            randomGoodieImage = goodieImage[random.randint(0,2)]
            newGoodie= {'rect':pygame.Rect(random.randint(0, WINDOW_WIDTH - SIZE),0 - SIZE, SIZE, SIZE),
                       'speed':random.randint(GOODIEMINSPEED, GOODIEMAXSPEED),
                       'surface':pygame.transform.scale(randomGoodieImage,(SIZE, SIZE))}
            
            goodies.append(newGoodie)
            
            
            
       
      
        if moveLeft and playerRect.left > 0:
           
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
        if moveRight and playerRect.right < 1200:
          
            playerRect.move_ip(PLAYERMOVERATE, 0)
            
        for b in baddies:
                b['rect'].move_ip(0, b['speed'])
                
        for g in goodies:
                g['rect'].move_ip(0, g['speed'])


        for b in baddies:
            windowSurface.blit(b['surface'], b['rect'])
             
        for g in goodies:
            windowSurface.blit(g['surface'], g['rect'])

        pygame.display.update()
         
        if playerHasHitBaddie(playerRect, baddies):  
                 
           life -=1
           
           if life ==0:
               windowSurface.blit( sfondoAulaStretchedImage ,windowSurfaceRectangle )
               drawText1('GAME OVER', font, windowSurface, windowSurface.get_rect().centerx-100, windowSurface.get_rect().centery-150)
               pygame.display.update()
               time.sleep(3)
               
        
      
        if playerHasHitGoodie(playerRect, goodies):
            score+=10
            
        
        pygame.display.update()
        mainClock.tick(FPS)
        
     
#    pygame.mixer.music.stop()
#    gameOverSound.play()
#        drawText('Premi un tasto per giocare di nuovo.', font, windowSurface, (WINDOW_WIDTH / 3) - 80, (WINDOW_HEIGHT / 3) + 50)
        pygame.display.update()

#    gameOverSound.stop()
