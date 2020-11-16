import sys 
sys.path.insert(1, 'gen_terrain')
import algorithmes
import map_2D
from random import randint
import main_var

def get_seed():
    seed = randint(0,10000)
    return seed

def create_noise_map(seed):
    t, shape, seed = algorithmes.func_noise_map(main_var.shape,main_var.scale,main_var.octaves,main_var.persistence,main_var.lacunarity,seed,main_var.facteur_denivele)
    return t,shape,seed

def get_map_image(seed):
    map_2D.func_map_color_perlin(shape=(900,900),scale=50.0,octaves=5, persistence=0.5,lacunarity=2.0,seed=0,name='carte_couleur.png',hauteur_ocean=0,facteur_denivele=0.1,couleur_option='Réaliste')
    print("Map créée")

def drawGrid():
    WHITE =(255,255,255)
    blockSize = 20 #Set the size of the grid block
    for x in range(WINDOW_WIDTH):
        for y in range(WINDOW_HEIGHT):
            rect = pygame.Rect(x*blockSize, y*blockSize,
                               blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)