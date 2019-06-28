# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 12:07:21 2019

@author: scr.013
"""
import pygame, sys
from pygame.locals import *
pygame.init()
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
basicFont = pygame.font.SysFont(None, 48)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
text = basicFont.render('Hello World', True, WHITE, RED)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery
windowSurface.blit(text, textRect)
windowSurface.fill(WHITE)
pygame.draw.polygon(windowSurface, GREEN, ((146, 0), (291, 106), (236, 277),(56, 277), (0, 106)))
pygame.draw.line(windowSurface, BLUE, (60 , 60) , (120 , 60), 4)
pygame.draw.circle(windowSurface, BLUE, (300, 50), 20, 0)
pygame.draw.ellipse(windowSurface, RED, (300 , 250 , 40, 80), 1)
pygame.draw.rect(windowSurface, RED, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

