import pygame
import functions
import button

continuer=True
def menujeu():


	ecran = pygame.display.set_mode((900, 900))
	background = pygame.image.load("img/fondmenu.png")

	#bouton des fleche de selection
	boutonGj1=pygame.image.load("img/boutonselecgauche.png")
	boutonDj1=pygame.image.load("img/boutonselec.png")
	boutonGj2=pygame.image.load("img/boutonselecgauche.png")
	boutonDj2=pygame.image.load("img/boutonselec.png")
	#bouton des fleche de selection

	#bouton lancer
	boutonlancer=pygame.image.load("img/lancer.png")
	#bouton lancer
	ecran.blit(background,(0,0))


	while continuer:
		Joueur1 = joueur()
		Joueur2 = joueur()
		pygame.display.flip()
		##################################
		for event in pygame.event.get():
        ###
        if event.type == pygame.QUIT:
            continuer = False
        ###
        position_souris = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
        	###
        	if bouttonGj1.isOver(position_souris):
        		Joueur1.createClasse("info")
        	###
        	if bouttonDj1.isOver(position_souris):
        		Joueur1.createClasse("math")
        	###
        	if bouttonGj2.isOver(position_souris):
        		Joueur2.createClasse("info")
        	###
        	if bouttonDj2.isOver(position_souris):
        		Joueur2.createClasse("math")
        ################################## 
	pygame.quit()
	joueurs=[Joueur1,Joueur2]
	return joueurs
