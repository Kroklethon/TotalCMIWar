import pygame
import functions
def loadjeu(continuer):
	ecran = pygame.display.set_mode((900, 900))
	background = pygame.image.load("img/fondchargement.png")
	ecran.blit(background,(0,0))
	pygame.display.flip()
	seed = functions.get_seed()
	tab_hauteur,shape,seed = functions.get_map_image(seed)
	pygame.quit()
	return tab_hauteur,shape,seed