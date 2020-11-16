###################################importation###############################################################
import pygame
import main_var
import functions 
import sys 
import boutton
import interaction
###################################importation###############################################################


###################################def variable##############################################################
var_pour_gen = 1
var_lance_jeu = True

sys.path.insert(var_pour_gen, '/gen_terrain')
pygame.init()
seed = functions.get_seed()
screen = pygame.display.set_mode(main_var.size)

background = pygame.image.load("carte_couleur.png")
###################################def variable##############################################################


###################################code def jeu##############################################################
def cree_table():
    """
    entree: rien
    sortie: rien 

    crée le tableau vide correspondant au case du tableau
    """
    #####cration variable ######
    tableau = []*main_var.width #TABLEAU ->
    dico = {}                      #DICTIONNAIRE 
    dico["statue"] = "vide"        #statue vide (case vide)
    #####cration variable ######
    for i in range(main_var.width):
        tableau[i] = [dico]*main_var.height          
    return tableau 

def drawGrid():
    blockSize = 30 #Set the size of the grid block
    for x in range(main_var.width):
        for y in range(main_var.height):
            rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
            functions.creercase(var_pour_gen, x, y)
###################################code def jeu##############################################################



###################################lanceur de jeu############################################################
tableau_jeu = cree_table()

#bouton de test qui serivra plus tard a passer son tour#########################
boutonfintour = boutton.button((0,255,0), 600, 600, 200, 80, "passer son tour")#
boutonfintour.draw(screen ,(0,0,0))                                            #
#bouton de test qui serivra plus tard a passer son tour#########################
tourjoueur1 = True #variable qui definie qui peut jouer ici c'est au tour du joueur 1
dragj1 = False
dragj2 = False
while var_lance_jeu == True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT: 
            sys.exit()

        position = pygame.mouse.get_pos()

        #######################test pour le passer son tour#####################

        if event.type == pygame.MOUSEBUTTONDOWN: # test si on clique sur le bouton et passe le tour
            if boutonfintour.isover(position):
                if tourjoueur1 == True:
                    tourjoueur1 = False
                else:
                    tourjoueur1 = True
                print("tour passer")#provisoire

        if event.type == pygame.MOUSEMOTION: # test si la sourie est dessus le bouton et change la couleur
            if boutonfintour.isover(position):
                boutonfintour.color = (255,255,255)
            else:
                boutonfintour.color = (255,0,0)

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
    
    ######################ici on crée des perso et une montagne#################
    ###joueur 1
    a = {}
    a["statue"] = "joueur_1"
    tableau_jeu[3][5] = a
    ###joueur 2         
    a = {}
    a["statue"] = "joueur_2"
    tableau_jeu[5][5] = a
    ###montagne
    a = {}
    a["statue"] = "montagne"
    tableau_jeu[4][4] = a
    ######################provisoire pour la v1#################################
    drawGrid()   
    pygame.display.update()

###################################lanceur de jeu############################################################
sys.exit()

