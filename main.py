import pygame
import main_var
import functions 
import sys 
sys.path.insert(1, 'gen_terrain')
pygame.init()
seed = functions.get_seed()
functions.get_map_image(seed)
screen = pygame.display.set_mode(main_var.size)

background = pygame.image.load("carte_couleur.png")

def drawGrid():
    blockSize = 30 #Set the size of the grid block
    for x in range(main_var.width):
        for y in range(main_var.height):
            rect = pygame.Rect(x*blockSize, y*blockSize,
                               blockSize, blockSize)
            pygame.draw.rect(screen, main_var.white, rect, 1)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.blit(background,(0,0))
    drawGrid()   
    pygame.display.update()



