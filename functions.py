import pygame
import main_var
import sys 
sys.path.insert(1, 'gen_terrain')
import algorithmes
import map_2D
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


def get_seed():
    seed = randint(0,100)
    return seed

def create_noise_map(game_seed):
    t, shape, seed = algorithmes.func_noise_map(main_var.shape,main_var.scale,main_var.octaves,main_var.persistence,main_var.lacunarity,game_seed,main_var.facteur_denivele)
    return t,shape

def get_map_image(game_seed):
    t, shape, seed =  map_2D.func_map_color_perlin(shape=(900,900),scale=100.0,octaves=5, persistence=0.5,lacunarity=2.0,seed=game_seed,name='carte_couleur.png',hauteur_ocean=0,facteur_denivele=0.1,couleur_option='Réaliste')
    print("Map créée")
    return t,shape,seed

def get_pos_grid(pos):
    posx,posy = pos
    x = posx // 30 + 1
    y = posy // 30 + 1
    return (x,y)

def get_height_case(case,t):
    x,y = case
    somme = 0
    if x<31 and y<31:
        for i in range(30):
            for j in range(30):
                val = (t[i*x][j*y])*100
                somme += val
    return somme/900
