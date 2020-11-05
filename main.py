import pygame
import functions
import sys 
sys.path.insert(1, '/gen_terrain')
pygame.init()

size = width, height = 900, 900
speed = [1,1]
black = 0, 0, 0
screen = pygame.display.set_mode(size)
background = pygame.image.load("carte_couleur.png")

def drawGrid():
    white =(255,255,255)
    blockSize = 30 #Set the size of the grid block
    for x in range(width):
        for y in range(height):
            rect = pygame.Rect(x*blockSize, y*blockSize,
                               blockSize, blockSize)
            pygame.draw.rect(screen, white, rect, 1)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.blit(background,(0,0))
    drawGrid()   
    pygame.display.update()



