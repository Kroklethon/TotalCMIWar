###################################importation###############################################################
import pygame
import main_var
import sys 
import boutton
import interraction
import functions
###################################importation###############################################################


###################################def variable##############################################################
var_pour_gen = 1
var_lance_jeu = True

sys.path.insert(var_pour_gen, '/gen_terrain')
pygame.init()
seed = functions.get_seed()
functions.get_map_image(seed)
screen = pygame.display.set_mode(main_var.size)

background = pygame.image.load("carte_couleur.png")
###################################def variable##############################################################


###################################code def jeu##############################################################
def creecase(var_pour_gen, posx, posy,tableau, rectangle):
	case_tabl = tableau[posx][posy]
	rect=rectangle
	if case_tabl['statue'] == 'montagne' :
		pygame.draw.rect(screen, main_var.montagne, rect, var_pour_gen)
	elif case_tabl['statue'] == 'joueur_1':
		pygame.draw.rect(screen, main_var.joueur_1, rect, var_pour_gen)
	elif case_tabl['statue'] == 'joueur_2':
		pygame.draw.rect(screen, main_var.joueur_2, rect, var_pour_gen)
	else:
		pygame.draw.rect(screen, main_var.white, rect, var_pour_gen)

def cree_table():
    """
    entree: rien
    sortie: rien 

    crée le tableau vide correspondant au case du tableau
    """
    tailletab = 30
    tailleligne = 30
    #####cration variable ######
    tableau = []                   #TABLEAU ->
    dico = {}                      #DICTIONNAIRE 
    dico['statue'] = 'vide'        #statue vide (case vide)
    #####cration variable ######
    tableau = [[dico] * tailleligne] * tailletab
    return tableau 

def drawGrid():
    blockSize = 30 #Set the size of the grid block
    for x in range(blockSize):
        for y in range(blockSize):
            rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
            pygame.draw.rect(screen, main_var.white, rect, var_pour_gen)

###################################code def jeu##############################################################



###################################lanceur de jeu############################################################
tableau_jeu = cree_table()
######################ici on crée des perso et une montagne#################
###joueur 1
tableau_jeu[3][6]['statue'] = 'joueur_1'
###joueur 2         
tableau_jeu[4][5]['statue'] = 'joueur_2'
print (tableau_jeu[4][5])
print(tableau_jeu[1][6])
######################provisoire pour la v1#################################
#bouton de test qui serivra plus tard a passer son tour#########################
#boutonfintour = boutton.button((0,255,0), 600, 600, 200, 80, 'passer son tour')#
#boutonfintour.draw(screen ,(0,0,0))                                            #
#bouton de test qui serivra plus tard a passer son tour#########################
tourjoueur1 = True #variable qui definie qui peut jouer ici c'est au tour du joueur 1
dragj1 = False
dragj2 = False
while var_lance_jeu == True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT: 
            sys.exit()

        position = pygame.mouse.get_pos()
        pos_grid = functions.get_pos_grid(position)

        #######################test pour le passer son tour#####################

        #if event.type == pygame.MOUSEBUTTONDOWN: # test si on clique sur le bouton et passe le tour
            #if boutonfintour.isover(position):
            #    if tourjoueur1 == True:
            #        tourjoueur1 = False
            #    else:
            #        tourjoueur1 = True
            #    print("tour passer")#provisoire

        #if event.type == pygame.MOUSEMOTION: # test si la sourie est dessus le bouton et change la couleur
            #if boutonfintour.isover(position):
            #    boutonfintour.color = (255,255,255)
            #else:
            #    boutonfintour.color = (255,0,0)

        #######################test pour le passer son tour#####################

        #################zone de test du jeu####################################

        if event.type == pygame.MOUSEBUTTONDOWN:
            #test si on clic sur le joueur souhaiter et passe en mode drag and drop
            if interraction.isoverj(tableau_jeu, position, 1) and tourjoueur1 == True:
                dragj1 = True
            if interraction.isoverj(tableau_jeu, position, 2) and tourjoueur1 == False:
                dragj2 = True
            # si en mode drag and drop et click dans zone libre 
            if dragj1 == True and interraction.isovertt(tableau_jeu, position) == False:
                interraction.setposj(tableau_jeu, position, 1)
                dragj1 = False
            if dragj2 == True and interraction.isovertt(tableau_jeu, position) == False:
                interraction.setposj(tableau_jeu, position, 2)
                dragj2 = False

        #################zone de test du jeu####################################

    screen.blit(background,(0,0))
    

    drawGrid()   
    pygame.display.update()

###################################lanceur de jeu############################################################
sys.exit()

