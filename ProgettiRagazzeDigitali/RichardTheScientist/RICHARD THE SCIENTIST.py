#IMPORT
import pygame, sys, random
from pygame.locals import *
import time
import pygame_textinput

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

def inputDaPygame():
    textinput = pygame_textinput.TextInput()
    clock = pygame.time.Clock()
    
    inputInserito = True
    
    while inputInserito:
    
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
    
        # Feed it with events every frame
#        textinput.update(events)
        # Blit its surface onto the screen
        windowSurface.blit(textinput.get_surface(), (140, 140))
    
        pygame.display.update()
        clock.tick(30)
        
        if textinput.update(events):
            inputInserito = False
            return textinput.get_text()

def inputDaPygame1():
    textinput = pygame_textinput.TextInput()
    clock = pygame.time.Clock()
    
    inputInserito = True
    
    while inputInserito:
    
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
    
        # Feed it with events every frame
#        textinput.update(events)
        # Blit its surface onto the screen
        windowSurface.blit(textinput.get_surface(), (400, 250))
    
        pygame.display.update()
        clock.tick(30)
        
        if textinput.update(events):
            inputInserito = False
            return textinput.get_text()
            
def getRandomWord(wordList):
    wordIndex = random.randint(0, len(words) - 1) 
    return words[wordIndex]

def getGuess(alreadyGuessed):
    while True:       
        introduzione='Inserisci una lettera.'
        drawText(introduzione,  font, windowSurface, 140,110)
        pygame.display.update()           
        
        guess = inputDaPygame()
          
        print(guess)
    
        guess = guess.lower()
        if len(guess) == 1 and guess not in alreadyGuessed and guess in 'abcdefghijklmnopqrstuvwxyz':
            return guess
        
def displayBoard(missedLetters, correctLetters, secretWord):

    numberOfMissedLetters = len(missedLetters)
    windowSurface.blit(backgroundStrechedImage, windowSurfaceRectangle)
    windowSurface.blit(HANGMAN_PICS[numberOfMissedLetters], hangmanRectangle)
    drawText('Lettere sbagliate: ' , font, windowSurface, 650, WINDOW_HEIGHT/3 + 100)
    xPosition = 1000
    for letters in missedLetters:
        drawText( letters, font, windowSurface, xPosition, WINDOW_HEIGHT/3 + 100)
        xPosition += 30
   
    guessedLetters = []
    for i in range(len(secretWord)) :
        if secretWord[i] in correctLetters:
            guessedLetters.append(secretWord[i])
        else:
            guessedLetters.append('_')
    guessedLettersStr=str(guessedLetters)
    drawText(guessedLettersStr, fontSmall, windowSurface, 650, WINDOW_HEIGHT/3 )
    return guessedLetters
 
def getGuessReazioni():
    while True:       
        introduzione='Completa la reazione.'
        drawText1(introduzione,  font, windowSurface, 100,110)
        pygame.display.update()           
        
        guess = inputDaPygame1()
        print(guess)

        return guess
#CARATTERISTICHE FINESTRA           

pygame.init()
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 1000

WHITE=(255,255,255)
BLACK=(0,0,0)
AZZURRO=(142,250,227)
font= pygame.font.SysFont(None, 48)
fontSmall=pygame.font.SysFont(None, 25)

mainClock = pygame.time.Clock()
windowSurface=pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('RICHARD THE SCIENTIST')
pygame.mouse.set_visible(True)

#FRASI CIVILI GIOCO 1
correctAnswer = ['Sei un chimico provetto!', 'Ti piace la chimica eh?', 'Bravo chimico!','Grande!','Vero, certamente!','Continua così'] 
wrongAnswer = ['Questa è un\'ironia che non mi piace', 'Errare humanum est, perseverare diabolicum.', 'Sono seriamente preoccupato per l\' esito di questo quiz.','Mh..sembra che tu non abbia studiato','Devi studiare di più','Questa è sbagliata!']   
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
PLAYER_WIDTH2=514
PLAYER_HEIGHT1=800
PLAYER_HEIGHT2=750
#IMMAGINI GIOCO 2
sfondoAula=pygame.image.load('sfondo-aula.jpg')
playerImage = pygame.image.load('Scientist-Transparent.png')
baddieImage1 = pygame.image.load('radiation.png')
baddieImage2 = pygame.image.load('simbolo_velenoso.png')
goodieImage1=pygame.image.load('beutapng.png')
goodieImage2=pygame.image.load('provetta-png.png')
goodieImage3=pygame.image.load('term.png')

playerRect = playerImage.get_rect() 
baddieImage1Rect=baddieImage1.get_rect()
baddieImage2Rect=baddieImage2.get_rect()
goodieImage1Rect=goodieImage1.get_rect()
goodieImage2Rect=goodieImage2.get_rect()
goodieImage3Rect=goodieImage3.get_rect()

playerStretchedImage=pygame.transform.scale(playerImage,(PLAYER_WIDTH, PLAYER_HEIGHT))
playerStretchedImage1=pygame.transform.scale(playerImage,(PLAYER_WIDTH1, PLAYER_HEIGHT1))
playerStretchedImage2=pygame.transform.scale(playerImage,(PLAYER_WIDTH1, PLAYER_HEIGHT1))

baddieStretchedImage1=pygame.transform.scale(baddieImage1,(SIZE,SIZE))
baddieStretchedImage2=pygame.transform.scale(baddieImage2,(SIZE,SIZE))
goodieStretchedImage1=pygame.transform.scale(goodieImage1,(SIZE,SIZE))
goodieStretchedImage2=pygame.transform.scale(goodieImage2,(SIZE,SIZE))
goodieStretchedImage3=pygame.transform.scale(goodieImage3,(SIZE,SIZE))

playerRect = playerStretchedImage.get_rect()
playerRect1 = playerStretchedImage1.get_rect()
playerRect2 = playerStretchedImage2.get_rect()

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

HANGMAN_PICS=[hangman1, hangman2, hangman3, hangman4, hangman5, hangman6, hangman7, hangman8, hangman9, hangman10]
hangmanRectangle= pygame.Rect(140,180,450, 700)
     
correctLetters = []
missedLetters = []
words = ['aneuploidia','desossiribosio','citoplasma','ebullioscopia','ecosistema','coagulazione','cloroplasti','catalizzatore','autotrofo','stechiometria','pleitropia','biochimica', 'drosophila', 'neurospora', 'metionina', 'dissociazione', 'fenilchetonuria', 'praseodimio','amminoacido','cromatidio','esoscheletro']
secretWord = getRandomWord(words)

#SFONDO GIOCO2

sfondoAulaStretchedImage=pygame.transform.scale(sfondoAula, (WINDOW_WIDTH, WINDOW_HEIGHT))



#CARATTERISTICHE CIVILI
X_POSITION = 0
X_POSITION1=0
X_POSITION2=1000
Y_POSITION = WINDOW_HEIGHT/3
Y_POSITION1=300
Y_POSITION2=250
prof = pygame.Rect(X_POSITION, Y_POSITION, PLAYER_WIDTH, PLAYER_HEIGHT)
prof1 = pygame.Rect(X_POSITION, Y_POSITION1, PLAYER_WIDTH1, PLAYER_HEIGHT1)

#SFONDO GIOCO 4
sfondoLaboratorio=pygame.image.load('laboratorio.jpg')
windowSurfaceRectangle=windowSurface.get_rect()

sfondoLaboratorioStretchedImage=pygame.transform.scale(sfondoLaboratorio, (WINDOW_WIDTH, WINDOW_HEIGHT))


score=0
windowSurface.fill(AZZURRO)
windowSurface.blit(playerStretchedImage1, playerRect1)
drawText1('Benvenuti,',font, windowSurface, 700,200)
drawText1('questo è il Richard The Scientist Game.',font, windowSurface, 700,300)
drawText1('Buon divertimento!',font, windowSurface, 700,400)
pygame.display.update()
waitForPlayerToPressKey()

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
    drawText('Punteggio: '+str(score), font,windowSurface,100, windowSurface.get_rect().centery-200)    
    if score>=300:
        drawText('Complimenti chimico! Ma non è ancora finita...', font,windowSurface,100, windowSurface.get_rect().centery)   
    else:
        drawText('Non hai studiato abbastanza.', font,windowSurface,100, windowSurface.get_rect().centery-100) 
        drawText('Dovrai impegnarti molto nella prossima prova.', font,windowSurface,100, windowSurface.get_rect().centery)
    pygame.display.update() 
    
    
    #GIOCO 2
    waitForPlayerToPressKey()
 
    windowSurface.blit( sfondoAulaStretchedImage ,windowSurfaceRectangle )
    drawText1('Raccogli gli strumenti che ti serviranno nel laboratorio', font, windowSurface, (WINDOW_WIDTH / 6), (WINDOW_HEIGHT / 3))
    drawText1('ed evita le sostanze tossiche', font, windowSurface, (WINDOW_WIDTH / 3), (WINDOW_HEIGHT / 3)+50)
    drawText1('Premi un tasto per iniziare.', font, windowSurface, (WINDOW_WIDTH / 3) - 30, (WINDOW_HEIGHT / 3)+100)
    pygame.display.update()
    
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

        
         
        if playerHasHitBaddie(playerRect, baddies):  
                 
           life -=1
           
           if life ==0:
               windowSurface.blit( sfondoAulaStretchedImage ,windowSurfaceRectangle )
               drawText1('Hai raccolto gli oggetti che ti serviranno in laboratorio.', font, windowSurface,100, windowSurface.get_rect().centery-150)
               drawText1("Prima di andarci dovrai superare quest'ultima prova.", font, windowSurface,100, windowSurface.get_rect().centery-100)
               pygame.display.update()
               
               break
        
      
        if playerHasHitGoodie(playerRect, goodies):
            score+=10
            
        mainClock.tick(FPS)
        pygame.display.update()
        
#gioco3
    
    waitForPlayerToPressKey()
    windowSurface.blit(backgroundStrechedImage, windowSurfaceRectangle)
    drawText('Indovina la parola segreta e riusciari ad entrare nel laboratorio!' ,font, windowSurface, 100,200)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    level3 = True
    while level3:
        windowSurface.blit(backgroundStrechedImage, windowSurfaceRectangle)
        parolaIndovinata = str(displayBoard(missedLetters, correctLetters, secretWord))
        if parolaIndovinata.find('_') == -1:
            print(correctLetters)
            drawText(correctAnswer[nCorrectAnswer1], fontSmall, windowSurface, 650, WINDOW_HEIGHT/3 + 150)
            drawText('La parola corretta è "' + secretWord+'".', fontSmall, windowSurface, 650, WINDOW_HEIGHT/3 + 200)
            score=score+500
            drawText('Punteggio: '+str(score), font, windowSurface, 650, WINDOW_HEIGHT/3 + 250)
            pygame.display.update()
            waitForPlayerToPressKey() 
            
            level3 = False
            
            
        
        if len(missedLetters) == 9:
            
            drawText('Hai finito i tentativi dopo ' + str(len(missedLetters)) + ' lettere sbagliate e ' + str(len(correctLetters)) + ' corrette.', fontSmall,windowSurface, 650, WINDOW_HEIGHT/3 + 150)
            drawText('La parola era "' + secretWord + '".', fontSmall,windowSurface, 650, WINDOW_HEIGHT/3 + 200)
            drawText('Punteggio: '+str(score), font, windowSurface, 650, WINDOW_HEIGHT/3 + 250)  
            pygame.display.update()
            waitForPlayerToPressKey()
                
            level3 = False
    
        if level3==True:         
            guess = getGuess(missedLetters + correctLetters)
           # pygame.display.update()           
        
            
            if guess in secretWord:
                correctLetters.append(guess)
            else:
                missedLetters.append(guess)
                displayBoard(missedLetters, correctLetters, secretWord)
            
        
        
#GIOCO 4
    windowSurface.blit(sfondoLaboratorioStretchedImage ,windowSurfaceRectangle )

    text1=["Sei arrivato all'ultimo livello ."]
    drawText1(text1[0] ,font, windowSurface, 100,200)
    drawText1('Ora potrò verificare le tue conoscenze.' ,font, windowSurface, 100,250)
    pygame.display.update()
    waitForPlayerToPressKey()  
    
    windowSurface.blit(sfondoLaboratorioStretchedImage, windowSurfaceRectangle)
    
    drawText1('SO3 + H2O --->' ,font, windowSurface, 100,250)
    
    risposta =getGuessReazioni()
    pygame.display.update()
    rispostaCorretta=('H2SO4')
    if risposta==rispostaCorretta:
        drawText1(correctAnswer[nCorrectAnswer1], font,windowSurface,100, windowSurface.get_rect().centery)
        score = score + 100
        drawText1('Punteggio: ' + str(score), font,windowSurface,100, windowSurface.get_rect().centery + 100)
    else:
        drawText1(wrongAnswer[nWrongAnswer1], font, windowSurface,100, windowSurface.get_rect().centery)
        drawText1('Punteggio: '+ str(score), font,windowSurface,100, windowSurface.get_rect().centery + 100)
    pygame.display.update()
    waitForPlayerToPressKey()        
    
    windowSurface.blit(sfondoLaboratorioStretchedImage, windowSurfaceRectangle)
    
    drawText1('HCl + NaOH --->' ,font, windowSurface, 100,250)
    
    risposta =getGuessReazioni()
    pygame.display.update()
    rispostaCorretta=('NaCl+H2O') or ('H2O+NaCl')
    if risposta==rispostaCorretta:
        drawText1(correctAnswer[nCorrectAnswer2], font,windowSurface,100, windowSurface.get_rect().centery)
        score = score + 100
        drawText1('Punteggio: ' + str(score), font,windowSurface,100, windowSurface.get_rect().centery + 100)
    else:
        drawText1(wrongAnswer[nWrongAnswer2], font, windowSurface,100, windowSurface.get_rect().centery)
        drawText1('Punteggio: '+ str(score), font,windowSurface,100, windowSurface.get_rect().centery + 100)
    pygame.display.update()
    waitForPlayerToPressKey()       
    
    windowSurface.blit(sfondoLaboratorioStretchedImage, windowSurfaceRectangle)
    
    drawText1('AgNO3 + NaCl --->' ,font, windowSurface, 100,250)
    
    risposta =getGuessReazioni()
    pygame.display.update()
    rispostaCorretta=('AgCl+NaNO3') or ('NaNO3+AgCl')
    if risposta==rispostaCorretta:
        drawText1(correctAnswer[nCorrectAnswer3], font,windowSurface,100, windowSurface.get_rect().centery)
        score = score + 100
        drawText1('Punteggio: ' + str(score), font,windowSurface,100, windowSurface.get_rect().centery + 100)
    else:
        drawText1(wrongAnswer[nWrongAnswer3], font, windowSurface,100, windowSurface.get_rect().centery)
        drawText1('Punteggio: '+ str(score), font,windowSurface,100, windowSurface.get_rect().centery + 100)
    pygame.display.update()
    waitForPlayerToPressKey()        
        
    windowSurface.blit(sfondoLaboratorioStretchedImage, windowSurfaceRectangle)
    
    drawText1('As2S3+H2SO4 --->' ,font, windowSurface, 100,250)
    
    risposta =getGuessReazioni()
    pygame.display.update()
    rispostaCorretta=('As2(SO4)3+H2S') or ('H2S+As2(SO4)3')
    if risposta==rispostaCorretta:
        drawText1(correctAnswer[nCorrectAnswer4], font,windowSurface,100, windowSurface.get_rect().centery)
        score = score + 100
        drawText1('Punteggio: ' + str(score), font,windowSurface,100, windowSurface.get_rect().centery + 100)
        
    else:
        drawText1(wrongAnswer[nWrongAnswer4], font, windowSurface,100, windowSurface.get_rect().centery)
        drawText1('Punteggio: '+ str(score), font,windowSurface,100, windowSurface.get_rect().centery + 100)
    
    pygame.display.update()
        
    break
playerRect2.topleft = (700,100)
windowSurface.blit( sfondoAulaStretchedImage ,windowSurfaceRectangle )
windowSurface.blit(playerStretchedImage2, playerRect2)
drawText1('Il tuo punteggio è: ' +str(score)+'.',font, windowSurface,100, windowSurface.get_rect().centery-100)
drawText1('E\' stato un vero piacere condividere',font, windowSurface,100, windowSurface.get_rect().centery)         
drawText1('il laboratorio con te!',font, windowSurface,100, windowSurface.get_rect().centery+50)         
waitForPlayerToPressKey()
pygame.display.update()
#drawText('GAME OVER', font, windowSurface, (WINDOW_WIDTH / 3), (WINDOW_HEIGHT / 3))
#drawText('Premi un tasto per giocare ancora.', font, windowSurface, (WINDOW_WIDTH / 3) - 80, (WINDOW_HEIGHT / 3) + 50)
#pygame.display.update()
#waitForPlayerToPressKey()
    

    
    #    gameOverSound.stop()
