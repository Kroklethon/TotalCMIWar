import pygame
import main_var
from random import randint
def creecase(var_pour_gen, posx, posy,tableau):
	case_tabl = tableau[posx][posy]
	if case_tabl['statue'] == 'montagne' :
		pygame.draw.rect(screen, main_var.montagne, rect, var_pour_gen)
	elif case_tabl['statue'] == 'evan':
		pygame.draw.rect(screen, main_var.joueur_1, rect, var_pour_gen)
	elif case_tabl['statue'] == 'aurelien':
		pygame.draw.rect(screen, main_var.joueur_2, rect, var_pour_gen)
	else:
		pygame.draw.rect(screen, main_var.white, rect, var_pour_gen)
def drawGrid():
    blockSize = 30 #Set the size of the grid block
    for x in range(blockSize):
        for y in range(blockSize):
            rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
            creecase(var_pour_gen,x,y,tableau)
            
def get_pos_grid(pos):
    posx,posy = pos
    x = posx // 30
    y = posy // 30
    return (x,y)
