import pygame 
import ModulePersonne


def affiche_menu_droite(persopos):
	"""
	fonction qui affiche le menu avec tout les information sur un personnage
	entrre:
		-persopos: position de la case ou se tyrouve le perso
		-test_affichage: boolean qui definie si il y a un personnage a afficher les carac
	sortie: rien
	"""
	info=["Evan","Flo","RomRom","Théo"]
	math=["Aurélien","Simon","Julien","Léa"]
	bio=["ZIZI","BITE","CACA","CUCU"]

	nom=pygame.display.set_caption(perso[0].nom) #on peut faire du recursif????? je ne pense pas
	fenetre.blit(nom, (950,10))
	PV=pygame.display.set_caption(perso[0].PV)
	fenetre.blit(PV, (950,20))
	PA=pygame.display.set_caption(perso[0].PA)
	fenetre.blit(PA, (950,30))

	#info#
	if perso[0] in info:
		programmation=pygame.display.set_caption(perso[0].programmation)
		fenetre.blit(programmation, (950,40))
	if perso[0] in math:
		qi=pygame.display.set_caption(perso[0].qi)
		fenetre.blit(qi, (950,40))
	if perso[0] in bio:
		soins=pygame.display.set_caption(perso[0].soins)
		fenetre.blit(soins, (950,40))
		magie=pygame.display.set_caption(perso[0].magie)
		fenetre.blit(magie, (950,50))
#######################
