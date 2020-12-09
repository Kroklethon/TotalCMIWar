###################################importation###############################################################
import pygame
import main_var
import initialisation
import interraction
import boutton
import ModulePersonne
import functions
from ModuleGeosciences import Geosciences
from ModuleInfo import Info
from ModuleMath import Math
from joueur import joueur
###################################importation###############################################################



###################################def variable##############################################################
var_pour_gen = 1
var_lance_jeu = True
pygame.init()

seed = functions.get_seed()
tab_hauteur,shape,seed = functions.get_map_image(seed)
screen = pygame.display.set_mode(main_var.size)
background = pygame.image.load("carte_couleur.png")

tab = initialisation.cree_table()
###################################def variable##############################################################

###################################def personnage##############################################################
# Joueur1=ModulePersonne.Personne("evan")
# tab[Joueur1.posx][Joueur1.posy]="evan"
# Joueur2=ModulePersonne.Personne("aurelien")
# tab[Joueur2.posx][Joueur2.posy]="aurelien"
Joueur1 = joueur()
Joueur1.createClasse("info")
Joueur2 = joueur()
Joueur2.createClasse("math")
joueurs=[Joueur1,Joueur2]
functions.init_player(joueurs,tab)
###################################def personnage##############################################################

print(tab)
###################################cree tableau##############################################################            
def creecase(var_pour_gen, posx, posy,tableau,rect):
    case_tabl = tableau[posx][posy]
    if case_tabl == "montagne":
        pygame.draw.rect(screen, main_var.montagne, rect, 0)
    elif case_tabl in functions.list_name(Joueur1.getClasse()):
        pygame.draw.rect(screen, main_var.joueur_1, rect, 0)
    elif case_tabl in functions.list_name(Joueur2.getClasse()):
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
boutton_passer_tour=boutton.button((255,1,1),900,700,300,50,"Passer tour")
###################################cree boutton##############################################################



###################################lanceur de jeu############################################################
tour = True #variable qui definie qui peut jouer ici c'est au tour du joueur 1
while var_lance_jeu == True:
    boutton_passer_tour.draw(screen, (1,200,0)) #dessine bouton fin de tour
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            var_lance_jeu = False 
            pygame.quit()
    #info_jeu#
        position_souris = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:        #quand le joeur clique
            interraction.deplacer_combat(tour)          #programme qui gere le placecement et le combat
            pos_grid = functions.get_pos_grid(position_souris)
            h = functions.get_height_case(pos_grid,tab_hauteur)
            print(pos_grid)
            if boutton_passer_tour.isOver(position_souris):
                tour=boutton.interaction_fin_de_tour(tour)      #programme qui gere l'interaction fin de tour
    #info-jeu#
    if boutton_passer_tour.isOver(position_souris):
        boutton_passer_tour.draw(screen, (1,100,100)) #dessine bouton fin de tour
    screen.blit(background,(0,0))
    drawGrid()
    pygame.display.update()

###################################lanceur de jeu############################################################

