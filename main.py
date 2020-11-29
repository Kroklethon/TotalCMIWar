###################################importation###############################################################
import pygame
import main_var
import initialisation
import interraction
import boutton
import ModulePersonne
import functions
###################################importation###############################################################



###################################def variable##############################################################
var_pour_gen = 1
var_lance_jeu = True
pygame.init()
screen = pygame.display.set_mode(main_var.size)
background = pygame.image.load("carte_couleur.png")
tab = initialisation.cree_table()
###################################def variable##############################################################

###################################def personnage##############################################################
evan=ModulePersonne.Personne("evan")
tab[evan.posx][evan.posy]="evan"
aurelien=ModulePersonne.Personne("aurelien")
tab[aurelien.posx][aurelien.posy]="aurelien"
###################################def personnage##############################################################

print(tab)
###################################cree tableau##############################################################            
def creecase(var_pour_gen, posx, posy,tableau,rect):
	case_tabl = tableau[posx][posy]
	if case_tabl == 'montagne' :
		pygame.draw.rect(screen, main_var.montagne, rect, 0)
	elif case_tabl == 'evan':
		pygame.draw.rect(screen, main_var.joueur_1, rect, 0)
	elif case_tabl == 'aurelien':
		pygame.draw.rect(screen, main_var.joueur_2, rect, 0)
	else:
		pygame.draw.rect(screen, main_var.white, rect, var_pour_gen)
def drawGrid():
    blockSize = 30 #Set the size of the grid block
    for x in range(blockSize):
        for y in range(blockSize):
            rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
            creecase(var_pour_gen,x,y,tab,rect)
            

###################################cree tableau##############################################################


###################################cree boutton##############################################################
boutton_passer_tour=boutton.button((255,1,1),900,700,300,50,"passer tour")
###################################cree boutton##############################################################



###################################lanceur de jeu############################################################
tour = True #variable qui definie qui peut jouer ici c'est au tour du joueur 1
mode_selec=False
personnage_a_action=0
while var_lance_jeu == True:
    boutton_passer_tour.draw(screen, (1,200,0)) #dessine bouton fin de tour
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            var_lance_jeu = False 
            pygame.quit()
    #info_jeu#
        position_sourie = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:        #quand le joeur clique
            tab,mode_selec,personnage_a_action=interraction.deplacer_combat(tour,tab,mode_selec,personnage_a_action)          #programme qui gere le placecement et le combat
            if boutton_passer_tour.isOver(position_sourie):
                tour=boutton.interaction_fin_de_tour(tour)      #programme qui gere l'interaction fin de tour
    #info-jeu#
    if boutton_passer_tour.isOver(position_sourie):
        boutton_passer_tour.draw(screen, (1,100,100)) #dessine bouton fin de tour
    screen.blit(background,(0,0))
    drawGrid()
    pygame.display.update()

###################################lanceur de jeu############################################################

