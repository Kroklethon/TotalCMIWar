def positionj(tableau_jeu, statueobj):
	'''
	entrer:tableau a 2 dimention de cdictionnaire, rpz la grille du jeu
		   statue de la case (choix de ce qu'on veut chercher) que l'on cherche en coordonner
	sortie: tableau a 2 case 0 position x et 1 position y
	'''

	position = []
	trouver = False
	indice = 0

	while trouver = False and indice < len(tableau_jeu):
		indice2 = 0
		while trouver = False and indice2 <len(tableau_jeu[indice]):
			if tableau_jeu[indice][indice2].statue == statueobj:
				trouver = True
				prosition = position + [indice]
				prosition = position + [indice2]

	return position
	
def isoverj (tableau_jeu, position, joueur):
	'''
	entrer:	position d'un objet type position de pygame
			tableau a 2 dimention de cdictionnaire, rpz la grille du jeu
			joueur entier qui rpz soit le joueur 1 ou 2 
	sortie: boolean qui verifie si l'objet(position) est bien sur le joueur 1

	'''
	estaudessus = False

	if joueur = 1:
		posjoueur = positionj(tableau_jeu, joueur_1)
	if joueur = 2:
		posjoueur = positionj(tableau_jeu, joueur_2)

	if pos[0] > posjoueur[0] and pos[0] < posjoueur[0] + width:
        if pos[1] > posjoueur[1] and pos[1] < posjoueur[1] +height:
			estaudessus = True

	return estaudessus

def isovertt (tableau_jeu, position):
	'''
	entrer:	position d'un objet type position de pygame
			tableau a 2 dimention de cdictionnaire, rpz la grille du jeu
	sortie: boolean qui verifie si l'objet(position) est bien sur n'importequoi

	 
	'''
	estaudessus = False
	if tableau_jeu[int(pos[0])][int(pos[1])].statue == "vide":
			estaudessus = True
	return estaudessus

def setposj1 (tableau_jeu, position, joueur):
	'''
	entrer: position d'un objet type position de pygame
			tableau a 2 dimention de cdictionnaire, rpz la grille du jeu
			joueur entier qui rpz soit le joueur 1 ou 2 
	sortie: rien
	
	'''
	if joueur = 1:
		posjoueur = positionj(tableau_jeu, joueur_1)
		tableau_jeu[position[0]][position[1]].statue = "joueur_1" 
	if joueur = 2:
		posjoueur = positionj(tableau_jeu, joueur_2)
		tableau_jeu[position[0]][position[1]].statue = "joueur_2" 

	tableau_jeu[posjoueur[0]][posjoueur[1]].statue = "vide" 