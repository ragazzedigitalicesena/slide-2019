import pygame, random, sys, time
from pygame.locals import *


pygame.init ()


WINDOWWIDTH = 1600
WINDOWHEIGHT = 900
BACKGROUND_IMAGE = pygame.image.load("immagineIniziale.png")
BRANDT_CON_PANNOCCHIE = pygame.image.load('brandtconpannocchie.jpg')
WHITE = (255, 255, 255)
BLACK = (0,0,0)
GREEN = (0, 255, 0)
GREEN2 = (0, 200, 0)
MARRONE = (184, 134, 11)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
CAMPO_DI_GRANO = pygame.image.load('campodigranofinale1.jpg')
DAVID_BRANDT = pygame.image.load('davidBrant.png')
PANNOCCHIA = pygame.image.load('pannocchia2.png')
MEME_DAVID_FINALE = pygame.image.load('memeDavidFinale')
MUCCHIO_DI_NIENTE = pygame.image.load('mucchiodiniente.jpg')
PAUSA = pygame.image.load('pausa.jpg')

PLAYERMOVERATE = 5

def terminate():
    pygame.quit()
    sys.exit()
    
    
    
def waitForPlayerToPressMouseButton():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT: #x dalla finestra
                terminate()
            if event.type == MOUSEBUTTONDOWN:
                return event.pos
            


#funzione da richiamare per aspettare che l utente prema un pulsante
def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT: #x dalla finestra
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # tasto esc della tastiera
                    terminate()
                return # esco dalla funzione

def drawLabirinto():
        pygame.draw.line(windowSurface, MARRONE, (0, 50), (1500, 50), 100)
        pygame.draw.line(windowSurface, MARRONE, (900, 50), (900, 320), 100)
        pygame.draw.line(windowSurface, MARRONE, (850, 200), (1500, 200), 100)
        pygame.draw.line(windowSurface, MARRONE, (1500, 150), (1500, 550), 100)
        pygame.draw.line(windowSurface, MARRONE, (1450, 350), (1700, 350), 100)
        pygame.draw.line(windowSurface, MARRONE, (950, 320), (400, 320), 100)
        pygame.draw.line(windowSurface, MARRONE, (600, 320), (600, 200), 100)
        pygame.draw.line(windowSurface, MARRONE, (550, 200), (800, 200), 100)
        pygame.draw.line(windowSurface, MARRONE, (400, 370), (400, 200), 100)
        pygame.draw.line(windowSurface, MARRONE, (450, 200), (0, 200), 100)
        pygame.draw.line(windowSurface, MARRONE, (600, 320), (600, 500), 100)
        pygame.draw.line(windowSurface, MARRONE, (550, 500), (1300, 500), 100)
        pygame.draw.line(windowSurface, MARRONE, (1150, 500), (1150, 350), 100)
        pygame.draw.line(windowSurface, MARRONE, (1100, 350), (1400, 350), 100)
        pygame.draw.line(windowSurface, MARRONE, (150, 150), (150, 500), 100)
        pygame.draw.line(windowSurface, MARRONE, (100, 500), (500, 500), 100)
        pygame.draw.line(windowSurface, MARRONE, (1300, 450), (1300, 750), 100)
        pygame.draw.line(windowSurface, MARRONE, (500, 450), (500, 700), 100)
        pygame.draw.line(windowSurface, MARRONE, (450, 750), (800, 750), 100)
        pygame.draw.line(windowSurface, MARRONE, (800, 800), (800, 600), 100)
        pygame.draw.line(windowSurface, MARRONE, (800, 650), (1000, 650), 100)
        pygame.draw.line(windowSurface, MARRONE, (1000, 600), (1000, 800), 100)
        pygame.draw.line(windowSurface, MARRONE, (1000, 750), (1600, 750), 100)
        pygame.draw.line(windowSurface, MARRONE, (350, 500), (350, 750), 100)
        pygame.draw.line(windowSurface, MARRONE, (400, 750), (150, 750), 100)
        pygame.draw.line(windowSurface, MARRONE, (150, 800), (150, 600), 100)
      
        

windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 0)

backgroundStretchedImage = pygame.transform.scale (BACKGROUND_IMAGE, (700, 900))
windowSurfaceRect = pygame.Rect(500, 0, 700, 900)
windowSurface.blit(backgroundStretchedImage, windowSurfaceRect)

pygame.display.update()

#pygame.font.get_fonts(gameplay)

basicFont1 = pygame.font.SysFont("gameplay", 90)
text1 = basicFont1.render("Benvenuto su", True, WHITE)
textRect1 = text1.get_rect()
textRect1.centerx = 780
textRect1.centery = 50

basicFont2 = pygame.font.SysFont("gameplay", 120)
text2 = basicFont2.render("DAVID'S WORLD", True, WHITE)
textRect2 = text1.get_rect()
textRect2.centerx = 720
textRect2.centery = 120

basicFont3 = pygame.font.SysFont('timesnewroman', 48)
text3 = basicFont3.render("Gioca ora", True, BLACK)
textRect3 = text3.get_rect()
textRect3.centerx = 800
textRect3.centery = 750

basicFont4 = pygame.font.SysFont("arial", 70)
text4 = basicFont4.render("Non è molto ma è un lavoro onesto", True, WHITE)
textRect4 = text4.get_rect()
textRect4.centerx = 100
textRect4.centery = 100

windowSurface.blit(text1, textRect1)
windowSurface.blit(text2, textRect2)
windowSurface.blit(text3, textRect3)



pygame.display.update()

clickTextRect3 = False
while not clickTextRect3:
    pos = waitForPlayerToPressMouseButton ()
    clickTextRect3 = textRect3.collidepoint(pos)

#primo livello

windowSurface.fill(WHITE)
pygame.display.update()

mainClock = pygame.time.Clock()




level1 = True

#schermata iniziale
while level1:
    
    moveLeft = False
    moveRight = False
    moveUp = False
    moveDown = False
    
    brandtConPannocchie = pygame.transform.scale(BRANDT_CON_PANNOCCHIE, (1100, 700))
    windowSurfaceRect = pygame.Rect(500, 300, 1100, 700)
    windowSurface.blit(brandtConPannocchie, windowSurfaceRect)
    
    
    
    davidbrandtRect = pygame.Rect(0, 5, 90, 80)
    davidbrandt = pygame.transform.scale(DAVID_BRANDT, (90, 80))
    
    backgroundgrano = pygame.transform.scale(CAMPO_DI_GRANO, (WINDOWWIDTH, WINDOWHEIGHT))
    windowSurfaceRect = pygame.Rect(0, 0, WINDOWWIDTH, WINDOWHEIGHT)
    
    
    
    pannocchiaRect = pygame.Rect(1480, 700, 120, 110)
    #pannocchiaRect.bottomleft = (WINDOWWIDTH, WINDOWHEIGHT)
    pannocchia = pygame.transform.scale(PANNOCCHIA, (120, 110))
    #windowSurface.blit(pannocchieStretchedImage, windowSurfaceRect) 
    
    
    
    basicFont5 = pygame.font.SysFont("arial", 60)
    text5 = basicFont5.render("Oh no!", False, BLUE)
    textRect5 = text5.get_rect()
    textRect5.topleft = (0, 5)
    windowSurface.blit(text5, textRect5)
    
    basicFont6 = pygame.font.SysFont("arial", 50)
    text6 = basicFont6.render("David ha perso la sua pannocchia preferita!", False, BLUE)
    textRect6 = text6.get_rect()
    textRect6.topleft = (0, 65)
    windowSurface.blit(text6, textRect6)
    
    basicFont7 = pygame.font.SysFont("arial", 50)
    text7 = basicFont6.render("Aiutalo a ritrovarla", False, BLUE)
    textRect7 = text7.get_rect()
    textRect7.topleft = (0, 125)
    windowSurface.blit(text7, textRect7)
    
    basicFont8 = pygame.font.SysFont("arial", 50)
    text8 = basicFont8.render("nel minor tempo possibile", False, BLUE)
    textRect8 = text8.get_rect()
    textRect8.topleft = (0, 185)
    windowSurface.blit(text8, textRect8)
    
    basicFont9 = pygame.font.SysFont("arial", 50)
    text9 = basicFont9.render("Tempo massimo: 30 sec", False, BLUE)
    textRect9 = text9.get_rect()
    textRect9.topleft = (0, 245)
    windowSurface.blit(text9, textRect9)
    
    
    
    
    
    

    pygame.display.update()
  
    #primo gioco
    time.sleep(3)
    
    timer = 700
    level12 = True
    while level12:
    
        
        
        for event in pygame.event.get():
                if event.type == KEYDOWN :
                    if event.key == K_LEFT:
                        moveRight = False
                        moveLeft = True
                    if event.key == K_RIGHT:
                        moveRight = True
                        moveLeft = False
                    if event.key == K_UP:
                        moveDown = False
                        moveUp = True 
                    if event.key == K_DOWN:
                        moveDown = True 
                        moveUp = False
                        
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
      
        if moveLeft and davidbrandtRect.left > 0  and (windowSurface.get_at(davidbrandtRect.topleft) == MARRONE and windowSurface.get_at(davidbrandtRect.bottomleft) == MARRONE):
            davidbrandtRect.move_ip(-1 * PLAYERMOVERATE, 0)
           # print(davidbrandtRect.topleft, davidbrandtRect.bottomleft)
        if moveRight and davidbrandtRect.right < WINDOWWIDTH and (windowSurface.get_at(davidbrandtRect.topright) == MARRONE and windowSurface.get_at(davidbrandtRect.bottomright) == MARRONE):
            davidbrandtRect.move_ip(PLAYERMOVERATE, 0)
           # print(davidbrandtRect.topright, davidbrandtRect.bottomright)
        if moveUp and davidbrandtRect.top > 0 and windowSurface.get_at((davidbrandtRect.x, davidbrandtRect.top)) == MARRONE:
            davidbrandtRect.move_ip(0, -1 * PLAYERMOVERATE)
           # print(davidbrandtRect, davidbrandtRect.right, davidbrandtRect.bottom)
        if moveDown and davidbrandtRect.bottom < WINDOWHEIGHT and windowSurface.get_at((davidbrandtRect.x, davidbrandtRect.bottom)) == MARRONE:
            davidbrandtRect.move_ip(0, PLAYERMOVERATE)
           # print(davidbrandtRect, davidbrandtRect.right, davidbrandtRect.bottom)
        
       
        windowSurface.blit(backgroundgrano, windowSurfaceRect)
        drawLabirinto()
        windowSurface.blit(pannocchia, pannocchiaRect)
        windowSurface.blit(davidbrandt, davidbrandtRect)
        
        mucchioDiNiente = pygame.transform.scale(MUCCHIO_DI_NIENTE, (800, 500))
        mucchioDiNienteRect = pygame.Rect(400, 300, 900, 600)
       
        memeDavidFinale = pygame.transform.scale(MEME_DAVID_FINALE, (800, 500))
        memeDavidFinaleRect = pygame.Rect(400, 300, 900, 600)
        
        basicFont10 = pygame.font.SysFont("None", 200)
        text10 = basicFont10.render("GAME OVER", False, BLACK, WHITE)
        textRect10 = text10.get_rect()      
        textRect10.centerx = 800
        textRect10.centery = 200
        
        basicFont11 = pygame.font.SysFont("None", 200)
        text11 = basicFont11.render("HAI VINTO!", False, BLACK, WHITE)
        textRect11 = text11.get_rect()
        textRect11.centerx = 800
        textRect11.centery = 200
       
        
        #print(timer)
        timer -= 1
        if timer <= 0:
          
            
            windowSurface.blit(mucchioDiNiente, mucchioDiNienteRect)
        
            windowSurface.blit(text10, textRect10)
            pygame.display.update()
            time.sleep(5)
            windowSurface.fill(WHITE)
            pygame.display.update()
            break
        
        if davidbrandtRect.colliderect(pannocchiaRect):
            windowSurface.blit(backgroundgrano, windowSurfaceRect)
            drawLabirinto()
            windowSurface.blit(davidbrandt, davidbrandtRect)
                       
            windowSurface.blit(memeDavidFinale, memeDavidFinaleRect)
            windowSurface.blit(text11, textRect11)
            
            pygame.display.update()
            time.sleep(3)
            windowSurface.fill(WHITE) 
            

            basicFont12 = pygame.font.SysFont("gameplay", 100)
            text12 = basicFont12.render("rigioca", False, RED)
            textRect12 = text12.get_rect()
            textRect12.centerx = 800
            textRect12.centery = 200
            windowSurface.blit(text12, textRect12)
            
            basicFont13 = pygame.font.SysFont("gameplay", 100)
            text13 = basicFont13.render("esci", False, RED)
            textRect13 = text13.get_rect()
            textRect13.centerx = 800
            textRect13.centery = 600
            windowSurface.blit(text13, textRect13)
            
            run = True
            while run:
                pygame.display.update()
                
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN :
                        pos = event.pos
                        if textRect12.collidepoint(pos):
                            level12 = False
                            run = False
                            windowSurface.fill(WHITE)
                            pygame.display.update()       

                            break
                        
                        if textRect13.collidepoint(pos):
                            level12 = False
                            level1 = False
                            run = False
                            break
    
            
#            if clickTextRect12 == True :
#                windowSurface.blit(backgroundgrano, windowSurfaceRect)
#                drawLabirinto()
#                windowSurface.blit(davidbrandt, davidbrandtRect)
#            else:
#                clickTextRect13 == True :
#                    terminate()
#            else: 
#                return
            
            pygame.display.update()            
            
            
            
            
                    
        
        pygame.display.update()
        mainClock.tick(40)


windowSurface.fill(WHITE)
pausaDavid = pygame.transform.scale (PAUSA, (900, 600))
windowSurfaceRect = pygame.Rect(300, 100, 900, 600)
windowSurface.blit(pausaDavid, windowSurfaceRect)
mainClock.tick(40)
pygame.display.update()
waitForPlayerToPressKey()









