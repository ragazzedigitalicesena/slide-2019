import pygame, random, sys, os
from pygame.locals import *
exec(os.path.join( os.path.dirname(sys.argv[0]), 'labirinto.py'))

pygame.init()

drawLabirinto()