import pygame, sys, time, random
from pygame.locals import *

pygame.init()
#grandezza finestra
WINDOW_WIDTH= 800
WINDOW_HEIGHT= 800
#posizione del giocatore
X_POSITION = 0
Y_POSITION = 0
#grandezza del giocatore
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_SIZE = 80
#colori
BLACK= (0, 0, 0)
WHITE= (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
TEXTCOLOR= (0, 0, 0)
BACKGROUND= (0, 225, 173)
TEXT_STORIA= (	0, 31, 226)
#velocità
MOVESPEED = 6
#nani
NEWDWARF = 40
DWARFSIZE = 50
ADDNEWDWARF = 6 
score=0
dwarfCounter = 0

#funzioni
def terminate():
    pygame.quit()
    sys.exit()

def drawText(text, font, surface, x, y, textColor, beckgroundTextColor=None):
    if beckgroundTextColor == None:
         textobj = font.render(text, 1, textColor)
    else :
        textobj = font.render(text, 1, textColor,beckgroundTextColor)#creare la scritta
        
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def waitForPlayerToPressKey():
    while True: 
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: 
                    terminate()
                return
            
def waitForPlayerToPressMouse():
    while True: 
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == MOUSEBUTTONDOWN:
                return
#orologio
mainClock = pygame.time.Clock()
start_time = pygame.time.get_ticks()
#musica
pygame.mixer.music.load('don.mp3')
pygame.mixer.music.play(0)
#schermata iniziale
windowSurface = pygame.display.set_mode((WINDOW_WIDTH , WINDOW_HEIGHT) , 0 , 32)
windowSurfaceRectangle = windowSurface.get_rect()
basicFont = pygame.font.SysFont('Arial', 30)
basicFontStartWindows = pygame.font.SysFont('Arial', 38)
text = 'SEI PRONTO A GIOCARE? PREMI INVIO'

windowSurface.fill(BACKGROUND)
drawText(text, basicFontStartWindows,windowSurface, 40, 400, BLACK)



pygame.display.update()
waitForPlayerToPressKey()
#storiella
backgroundImage = pygame.image.load('monialand.jpg')
backgroundStretchedImage = pygame.transform.scale( backgroundImage ,( WINDOW_WIDTH , WINDOW_HEIGHT ) )
windowSurface.blit( backgroundStretchedImage , windowSurfaceRectangle )
fontStoria= pygame.font.SysFont('Helvetica',20)
text='C\'era una volta una città chiamata Monialand, dove gli abitanti vivevano felici e contenti. '
drawText(text,fontStoria ,windowSurface, 40, 200,TEXT_STORIA, WHITE )
text='In un giorno di sole in cui gli abitanti di Monialand,'
drawText(text,fontStoria ,windowSurface, 40, 220, TEXT_STORIA,WHITE)
text=' giocavano tra di loro tranquilli e spensierati, arrivò... '   
drawText(text,fontStoria ,windowSurface, 40, 260, TEXT_STORIA,WHITE)
pygame.display.update()
#pygame.time.delay(4000)
waitForPlayerToPressKey()

backgroundImage = pygame.image.load('ulla.jpg')
backgroundStretchedImage = pygame.transform.scale( backgroundImage ,( WINDOW_WIDTH , WINDOW_HEIGHT ) )
windowSurface.blit( backgroundStretchedImage , windowSurfaceRectangle )
fontStoria= pygame.font.SysFont('Helvetica',20)
text='...la perfida collezionista chiamata Ulla. '
drawText(text,fontStoria ,windowSurface, 20, 600, TEXT_STORIA,WHITE)
text='Con il suo arrivo terrorizzò gli abitanti  '
drawText(text,fontStoria ,windowSurface, 20, 620, TEXT_STORIA,WHITE)
text='che si chiesero subito per quale strana ragione lei fosse venuta lì, '
drawText(text,fontStoria ,windowSurface, 20, 640, TEXT_STORIA,WHITE)
text='visto che aveva già preso tutto ciò che c\'era di prezioso nella città di Monialand.'
drawText(text,fontStoria ,windowSurface, 20, 660, TEXT_STORIA,WHITE)


pygame.display.update()
waitForPlayerToPressKey()



backgroundImage = pygame.image.load('ullaland.jpg')
backgroundStretchedImage = pygame.transform.scale( backgroundImage ,( WINDOW_WIDTH , WINDOW_HEIGHT ) )
windowSurface.blit( backgroundStretchedImage , windowSurfaceRectangle )
fontStoria= pygame.font.SysFont('Helvetica',20)     
text='Ulla era ritornata lì per recuperare il Soldo Monieta 20000, antica monieta reale andata perduta '
drawText(text,fontStoria ,windowSurface, 20, 680, TEXT_STORIA,WHITE)
text='in un combattimento tra due soldati. Per recuperarla erano necessari'
drawText(text,fontStoria ,windowSurface, 20, 640, TEXT_STORIA,WHITE)
text='dei nani rari che avevano il potere di fiutarla.'
drawText(text,fontStoria ,windowSurface, 20, 660, TEXT_STORIA,WHITE)

pygame.display.update()
waitForPlayerToPressKey()

#pygame.time.delay(4000)


backgroundImage = pygame.image.load('porte.jpg')
backgroundStretchedImage = pygame.transform.scale(backgroundImage, (WINDOW_WIDTH, WINDOW_HEIGHT))
windowSurfaceRectangle = windowSurface.get_rect()
windowSurface.blit(backgroundStretchedImage, windowSurfaceRectangle)
text = 'Quale porta scegli?'
drawText(text, basicFont, windowSurface,40, 400, WHITE)
text = 'Per andare in quella a sinistra premi il tasto sinistro del mouse.'
drawText(text, basicFont, windowSurface,40, 430, WHITE)
text='Per andare in quella destra  premi il tasto destro del mouse.'
drawText(text, basicFont, windowSurface,40, 460, WHITE)
pygame.display.update()
waitForPlayerToPressMouse()


pygame.mixer.music.stop()
#scelta delle porte
while True:
    for event in pygame.event.get():
       
        if event.type == MOUSEBUTTONDOWN:
            print(event.button)
            
            if event.button == 1:
                #’Hai premuto il tasto sinistro del mouse ’)
                pygame.mixer.music.load('mario.mp3')
                pygame.mixer.music.play(0)
                player = pygame.Rect(random.randint(0,WINDOW_WIDTH-PLAYER_SIZE ), random.randint(0, WINDOW_HEIGHT - PLAYER_SIZE), PLAYER_SIZE, PLAYER_SIZE)
                dwarf = pygame.Rect(random.randint(0, WINDOW_WIDTH - DWARFSIZE), random.randint(0, WINDOW_HEIGHT - DWARFSIZE), DWARFSIZE, DWARFSIZE)
                # primo livello
                playerImage = pygame.image.load('player1.png')
                playerStretchedImage = pygame.transform.scale(playerImage, (PLAYER_SIZE, PLAYER_SIZE))
                playerRect= playerStretchedImage.get_rect()
        
                dwarfImage = pygame.image.load('dwarf.png')
                dwarfStretchedImage = pygame.transform.scale(dwarfImage, (DWARFSIZE, DWARFSIZE))
                dwarfRect= dwarfImage.get_rect()
                windowSurface = pygame.display.set_mode((WINDOW_WIDTH , WINDOW_HEIGHT) , 0 , 32)
                windowSurfaceRectangle = windowSurface.get_rect()
                backgroundImage = pygame.image.load('corri.jpg')
                backgroundStretchedImage = pygame.transform.scale( backgroundImage ,( WINDOW_WIDTH , WINDOW_HEIGHT ) )
                windowSurface.blit ( backgroundStretchedImage , windowSurfaceRectangle )
                pygame.display.update()
        
                dwarfList = []
                dwarfAddCounter = 0
                
                moveLeft = False
                moveRight = False
                moveUp = False
                moveDown = False
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
                            if event.key == K_x:
                                player.top = random.randint(0, WINDOW_HEIGHT - player.height)
                                player.left = random.randint(0, WINDOW_WIDTH - player.width)
                        
                        for d in dwarfList:
                            if playerRect.colliderect(d['rect']):
                                score= score +1
                                dwarfList.remove(d)
                        dwarfAddCounter += 1
                        if dwarfAddCounter == ADDNEWDWARF:
                            dwarfAddCounter = 0
                            dwarfSize = random.randint(DWARFSIZE, DWARFSIZE)
                            newDwarf = {'rect': pygame.Rect(random.randint(0, WINDOW_WIDTH - DWARFSIZE),  random.randint(0, WINDOW_HEIGHT - DWARFSIZE), DWARFSIZE, DWARFSIZE),
                                        'surface':pygame.transform.scale(dwarfImage, (DWARFSIZE, DWARFSIZE))}
                            
                            dwarfList.append(newDwarf)
                    
                    if moveDown and playerRect.bottom < WINDOW_HEIGHT:
                        playerRect.top += MOVESPEED
                    if moveUp and playerRect.top > 0:
                        playerRect.top -= MOVESPEED      
                    if moveLeft and playerRect.left > 0:
                        playerRect.left -= MOVESPEED
                    if moveRight and playerRect.right < WINDOW_WIDTH:
                        playerRect.right += MOVESPEED
                    
                    windowSurface.blit ( backgroundStretchedImage , windowSurfaceRectangle )
                    windowSurface.blit ( playerStretchedImage , playerRect )
                    
                    for dwarf in dwarfList:
                        windowSurface.blit ( dwarf['surface'] , dwarf['rect'] )
                   
                    drawText('Nani Presi: %s' % (score), basicFont, windowSurface, 10, 0, WHITE)
                    
                    pygame.display.update()
                    
                    if(score >= 10):
                        print ('vittoria')
                        pygame.mixer.music.stop()
                        break
                    
                    mainClock.tick(40)
                    
        #after break    
                windowSurface.fill(BLACK)
                text='pronto per il prossimo livello?'
                drawText(text, basicFont, windowSurface,40, 400, WHITE)
                pygame.display.update()
                time.sleep(4)
               
                
                
        #secondo livello
                pygame.mixer.music.load('adams.mp3')
                pygame.mixer.music.play(1)
                backgroundImage = pygame.image.load('quiz.jpg')
                backgroundStretchedImage = pygame.transform.scale(backgroundImage, (WINDOW_WIDTH, WINDOW_HEIGHT))
                windowSurfaceRectangle = windowSurface.get_rect()
                windowSurface.blit(backgroundStretchedImage, windowSurfaceRectangle)
                pygame.display.update()
        
                basicFont = pygame.font.SysFont('Arial', 30)
        
                domande_sets = [
                ['Quanti stati ci sono all\'interno dell\'Unione Europea?', '27', '18', '25', '20'],
                ['La parola genetliaco cosa significa?', 'Compleanno', 'Matrimonio', 'Battesimo', 'Riguarda la genetica'],
                ['Joahn Gutenberg è diventato famoso per...', 'Aver inventato la stampa a caratteri mobili', 'Aver tradotto i caratteri cuneiformi', 'Aver scoperto la città di Troia', 'Aver tradotto l\'Iliade e l\'Odissea'],
                ['I colori detti primari sono?', 'Giallo, rosso, blu', 'Giallo, verde, blu', 'Rosso, verde, blu', 'Rosso, verde, viola']]
        
                for x in range (3): #for che va da 0 a 4, indica il numero delle domande, Caci cambialo in 5!!!!
                    domandaAcaso = random.randint(0, 3)
                    rispostaAcaso = [1, 2, 3, 4]
                    random.shuffle(rispostaAcaso)
                    corretta = 0
                    n = 0
                    for r in rispostaAcaso:
                        if r == 1:
                            corretta = n
                        n += 1
        
                risposta = ['a','b','c','d']
                text = domande_sets[domandaAcaso][0]
                drawText(text, basicFont ,windowSurface, 40, 310, BLACK, WHITE)
                text = 'a)' + domande_sets[domandaAcaso][rispostaAcaso[0]]
                drawText(text, basicFont ,windowSurface, 40, 340, BLACK, WHITE)
                text = 'b)' + domande_sets[domandaAcaso][rispostaAcaso[1]]
                drawText(text, basicFont ,windowSurface, 40, 370, BLACK, WHITE)
                text = 'c)' + domande_sets[domandaAcaso][rispostaAcaso[2]]
                drawText(text, basicFont ,windowSurface, 40, 400, BLACK, WHITE)
                text = 'd)' + domande_sets[domandaAcaso][rispostaAcaso[3]]
                drawText(text, basicFont ,windowSurface, 40, 430, BLACK, WHITE)
                pygame.display.update()
        
                key = pygame.key.get_pressed()
                condizione = True
                while condizione:
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            terminate()
                        if event.type == KEYDOWN :
                            if event.key == K_a :
                                playerChoise='a'
                                if risposta[corretta] == playerChoise:
                                    drawText('Hai scelto la risposta corretta! Complimenti, continua così!', basicFont, windowSurface, 200, 100, BLACK)
                                    pygame.display.update()
                                    condizione= False
                                elif risposta[corretta] != playerChoise :
                                    drawText('Hai sbagliato! La risposta corretta era la ', domande_sets[domandaAcaso][rispostaAcaso[corretta]], '.', basicFont, windowSurface, 200, 100, BLACK)
                                    pygame.display.update()
                                    condizione= False
                            if event.key == K_b :
                                playerChoise='b'
                                if risposta[corretta] == playerChoise:
                                    drawText('Hai scelto la risposta corretta! Complimenti, continua così!', basicFont, windowSurface, 200, 100, BLACK)
                                    pygame.display.update()
                                    condizione= False
                                elif risposta[corretta] != playerChoise:
                                    drawText('Hai sbagliato! La risposta corretta era la ', domande_sets[domandaAcaso][rispostaAcaso[corretta]], '.', basicFont, windowSurface, 200, 100, BLACK)
                                    pygame.display.update()
                                    condizione= False
                            if event.key == K_c :
                                playerChoise='c'
                                if risposta[corretta] == playerChoise:
                                    drawText('Hai scelto la risposta corretta! Complimenti, continua così!', basicFont, windowSurface, 200, 100, BLACK)
                                    pygame.display.update()
                                    condizione= False
                                elif risposta[corretta] != playerChoise:
                                    drawText('Hai sbagliato! La risposta corretta era la ', domande_sets[domandaAcaso][rispostaAcaso[corretta]], '.', basicFont, windowSurface, 200, 100, BLACK)
                                    pygame.display.update()
                                    condizione= False
                            if event.key == K_d :
                                playerChoise='d'
                                if risposta[corretta] == playerChoise:
                                    drawText('Hai scelto la risposta corretta! Complimenti, continua così!', basicFont, windowSurface, 200, 100, BLACK)
                                    pygame.display.update()
                                    condizione= False
                                elif risposta[corretta] != playerChoise:
                                    drawText('Hai sbagliato! La risposta corretta era la ', domande_sets[domandaAcaso][rispostaAcaso[corretta]], '.', basicFont, windowSurface, 200, 100, BLACK)
                                    pygame.display.update()
                                    condizione= False
        
                windowSurface.fill(BLACK)
                text='Bene sei riuscito a salvare Monialand, congratulazioni'
                drawText(text, basicFont, windowSurface,40, 400, WHITE)
                time.sleep(6)
                pygame.display.update()
                terminate()
    
            elif event.button == 3:
                pygame.mixer.music.load('adams.mp3')
                pygame.mixer.music.play(0)
                backgroundImage = pygame.image.load('quiz.jpg')
                backgroundStretchedImage = pygame.transform.scale(backgroundImage, (WINDOW_WIDTH, WINDOW_HEIGHT))
                windowSurfaceRectangle = windowSurface.get_rect()
                windowSurface.blit(backgroundStretchedImage, windowSurfaceRectangle)
                pygame.display.update()
        
                basicFont = pygame.font.SysFont('Arial', 30)
        
                domande_sets = [
                ['Quanti stati ci sono all\'interno dell\'Unione Europea?', '27', '18', '25', '20'],
                ['La parola genetliaco cosa significa?', 'Compleanno', 'Matrimonio', 'Battesimo', 'Riguarda la genetica'],
                ['Joahn Gutenberg è diventato famoso per...', 'Aver inventato la stampa a caratteri mobili', 'Aver tradotto i caratteri cuneiformi', 'Aver scoperto la città di Troia', 'Aver tradotto l\'Iliade e l\'Odissea'],
                ['I colori detti primari sono?', 'Giallo, rosso, blu', 'Giallo, verde, blu', 'Rosso, verde, blu', 'Rosso, verde, viola']]
        
                for x in range (3): #for che va da 0 a 4, indica il numero delle domande, Caci cambialo in 5!!!!
                    domandaAcaso = random.randint(0, 3)
                    rispostaAcaso = [1, 2, 3, 4]
                    random.shuffle(rispostaAcaso)
                    corretta = 0
                    n = 0
                    for r in rispostaAcaso: 
                        if r == 1:
                            corretta = n
                        n += 1
        
        
                risposta = ['a','b','c','d']
                print(domandaAcaso)
                text = domande_sets[domandaAcaso][0]
                drawText(text, basicFont ,windowSurface, 40, 310, BLACK, WHITE)
                text = 'a)' + domande_sets[domandaAcaso][rispostaAcaso[0]]
                drawText(text, basicFont ,windowSurface, 40, 340, BLACK, WHITE)
                text = 'b)' + domande_sets[domandaAcaso][rispostaAcaso[1]]
                drawText(text, basicFont ,windowSurface, 40, 370, BLACK, WHITE)
                text = 'c)' + domande_sets[domandaAcaso][rispostaAcaso[2]]
                drawText(text, basicFont ,windowSurface, 40, 400, BLACK, WHITE)
                text = 'd)' + domande_sets[domandaAcaso][rispostaAcaso[3]]
                drawText(text, basicFont ,windowSurface, 40, 430, BLACK, WHITE)
                pygame.display.update()
    
                key = pygame.key.get_pressed()
                condizione = True
                while condizione:
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            terminate()
                        if event.type == KEYDOWN :
                            if event.key == K_a :
                                playerChoise='a'
                                if risposta[corretta] == playerChoise:
                                    drawText('Hai scelto la risposta corretta! Complimenti, continua così!', basicFont, windowSurface, 200, 100, BLACK)
                                    pygame.display.update()
                                    condizione= False
                                elif risposta[corretta] != playerChoise :
                                    drawText('Hai sbagliato! La risposta corretta era la ', domande_sets[domandaAcaso][rispostaAcaso[corretta]], '.', basicFont, windowSurface, 200, 100, BLACK)
                                    pygame.display.update()
                                    condizione= False
                            if event.key == K_b :
                                playerChoise='b'
                                if risposta[corretta] == playerChoise:
                                    drawText('Hai scelto la risposta corretta! Complimenti, continua così!', basicFont, windowSurface, 200, 100, BLACK)
                                    pygame.display.update()
                                    condizione= False
                                elif risposta[corretta] != playerChoise:
                                    drawText('Hai sbagliato! La risposta corretta era la ', domande_sets[domandaAcaso][rispostaAcaso[corretta]], '.', basicFont, windowSurface, 200, 100, BLACK)
                                    pygame.display.update()
                                    condizione= False
                            if event.key == K_c :
                                playerChoise='c'
                                if risposta[corretta] == playerChoise:
                                    drawText('Hai scelto la risposta corretta! Complimenti, continua così!', basicFont, windowSurface, 200, 100, BLACK)
                                    pygame.display.update()
                                    condizione= False
                                elif risposta[corretta] != playerChoise:
                                    drawText('Hai sbagliato! La risposta corretta era la ', domande_sets[domandaAcaso][rispostaAcaso[corretta]], '.', basicFont, windowSurface, 200, 100, BLACK)
                                    pygame.display.update()
                                    condizione= False
                            if event.key == K_d :
                                playerChoise='d'
                                if risposta[corretta] == playerChoise:
                                    drawText('Hai scelto la risposta corretta! Complimenti, continua così!', basicFont, windowSurface, 200, 100, BLACK)
                                    pygame.display.update()
                                    condizione= False
                                elif risposta[corretta] != playerChoise:
                                    drawText('Hai sbagliato! La risposta corretta era la ', domande_sets[domandaAcaso][rispostaAcaso[corretta]], '.', basicFont, windowSurface, 200, 100, BLACK)
                                    pygame.display.update()
                                    condizione= False
            windowSurface.fill(BLACK)
            text='pronto per il prossimo livello?'
            drawText(text, basicFont, windowSurface,40, 400, WHITE)
            time.sleep(3)
            pygame.mixer.music.stop()
            pygame.display.update()
            #livello 2
            pygame.mixer.music.load('mario.mp3')
            pygame.mixer.music.play(0)
            player = pygame.Rect(random.randint(0,WINDOW_WIDTH-PLAYER_SIZE ), random.randint(0, WINDOW_HEIGHT - PLAYER_SIZE), PLAYER_SIZE, PLAYER_SIZE)
            dwarf = pygame.Rect(random.randint(0, WINDOW_WIDTH - DWARFSIZE), random.randint(0, WINDOW_HEIGHT - DWARFSIZE), DWARFSIZE, DWARFSIZE)
        
            playerImage = pygame.image.load('player1.png')
            playerStretchedImage = pygame.transform.scale(playerImage, (PLAYER_SIZE, PLAYER_SIZE))
            playerRect= playerStretchedImage.get_rect()
        
            dwarfImage = pygame.image.load('dwarf.png')
            dwarfStretchedImage = pygame.transform.scale(dwarfImage, (DWARFSIZE, DWARFSIZE))
            dwarfRect= dwarfImage.get_rect()
            windowSurface = pygame.display.set_mode((WINDOW_WIDTH , WINDOW_HEIGHT) , 0 , 32)
            windowSurfaceRectangle = windowSurface.get_rect()
            backgroundImage = pygame.image.load('corri.jpg')
            backgroundStretchedImage = pygame.transform.scale( backgroundImage ,( WINDOW_WIDTH , WINDOW_HEIGHT ) )
            windowSurface.blit ( backgroundStretchedImage , windowSurfaceRectangle )
            pygame.display.update()
        
            dwarfList = []
            dwarfAddCounter = 0
        
            moveLeft = False
            moveRight = False
            moveUp = False
            moveDown = False
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
                        if event.key == K_x:
                            player.top = random.randint(0, WINDOW_HEIGHT - player.height)
                            player.left = random.randint(0, WINDOW_WIDTH - player.width)
        
                    for d in dwarfList:
                        if playerRect.colliderect(d['rect']):
                            score= score +1
                            dwarfList.remove(d)
                    dwarfAddCounter += 1
                    if dwarfAddCounter == ADDNEWDWARF:
                        dwarfAddCounter = 0
                        dwarfSize = random.randint(DWARFSIZE, DWARFSIZE)
                        newDwarf = {'rect': pygame.Rect(random.randint(0, WINDOW_WIDTH - DWARFSIZE),  random.randint(0, WINDOW_HEIGHT - DWARFSIZE), DWARFSIZE, DWARFSIZE),
                                    'surface':pygame.transform.scale(dwarfImage, (DWARFSIZE, DWARFSIZE))}
        
                        dwarfList.append(newDwarf)
        
                if moveDown and playerRect.bottom < WINDOW_HEIGHT:
                    playerRect.top += MOVESPEED
                if moveUp and playerRect.top > 0:
                    playerRect.top -= MOVESPEED
                if moveLeft and playerRect.left > 0:
                    playerRect.left -= MOVESPEED
                if moveRight and playerRect.right < WINDOW_WIDTH:
                    playerRect.right += MOVESPEED
                
                windowSurface.blit ( backgroundStretchedImage , windowSurfaceRectangle )
                windowSurface.blit ( playerStretchedImage , playerRect )
                    
                for dwarf in dwarfList:
                    windowSurface.blit ( dwarf['surface'] , dwarf['rect'] )
                   
                    drawText('Nani Presi: %s' % (score), basicFont, windowSurface, 10, 0, WHITE)
                    
                pygame.display.update()
                    
                if(score >= 10):
                    print ('vittoria')
                    pygame.mixer.music.stop()
                    break
                    
                mainClock.tick(40)
                pygame.display.update()


            windowSurface.fill(BLACK)
            text='Bene sei riuscito a salvare Monialand, congratulazioni'
            drawText(text, basicFont, windowSurface,40, 400, WHITE)
            time.sleep(6)
            pygame.display.update()
            terminate()
