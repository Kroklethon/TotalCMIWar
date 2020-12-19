import pygame
import functions
import button

continuer=True
def menujeu():

	stop=True
	ecran = pygame.display.set_mode((900, 900))
	background = pygame.image.load("img/fondmenu.png")

	#bouton des fleche de selection
	boutonGj1=pygame.image.load("img/boutonselecgauche.png")
	boutonDj1=pygame.image.load("img/boutonselec.png")
	boutonGj2=pygame.image.load("img/boutonselecgauche.png")
	boutonDj2=pygame.image.load("img/boutonselec.png")

	boutonGjover1=pygame.image.load("img/boutonselecgaucheover.png")
	boutonDjover1=pygame.image.load("img/boutonselecover.png")
	boutonGjover2=pygame.image.load("img/boutonselecgaucheover.png")
	boutonDjover2=pygame.image.load("img/boutonselecover.png")
	#bouton des fleche de selection

	#bouton lancer
	boutonlancer=pygame.image.load("img/lancer.png")
	#bouton lancer

	#image
	info = pygame.image.load("info.png")
	math = pygame.image.load("math.png")
	#image
	ecran.blit(background,(0,0))
	ecran.blit(info, (550,400))
	ecran.blit(math, (550,700))

	while continuer:
		Joueur1 = joueur()
		Joueur2 = joueur()
		pygame.display.flip()
		##################################
		screen.blit(boutonGj1, (500,400))
		screen.blit(boutonDj1, (800,400))
		screen.blit(boutonGj2, (500,700))
		screen.blit(boutonDj2, (800,700))
		##################################
		for event in pygame.event.get():
        ###
        if event.type == pygame.QUIT:
            continuer = False
            stop=False
        ###
        position_souris = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
        	###
        	if boutonGj1.isOver(position_souris):
        		Joueur1.createClasse("info")
        		ecran.blit(info, (550,400))
        	###
        	if boutonDj1.isOver(position_souris):
        		Joueur1.createClasse("math")
        		ecran.blit(math, (550,400))
        	###
        	if boutonGj2.isOver(position_souris):
        		Joueur2.createClasse("info")
        		ecran.blit(info, (550,700))
        	###
        	if boutonDj2.isOver(position_souris):
        		Joueur2.createClasse("math")
        		ecran.blit(math, (550,700))
        	if lancer.isOver(position_souris):
        		continuer=False
        ################################## 
        if boutonGj1.isOver(position_souris):
        	screen.blit(boutonGj1, (500,400))
        if boutonDj1.isOver(position_souris):
        	screen.blit(boutonDj1, (800,400))
        if boutonGj2.isOver(position_souris):
        	screen.blit(boutonGj2, (500,700))
        if boutonDj2.isOver(position_souris):
        	screen.blit(boutonDj2, (800,700))

	pygame.quit()
	joueurs=[Joueur1,Joueur2]
	return joueurs,stop
