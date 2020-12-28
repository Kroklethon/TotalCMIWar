###################################importation###############################################################
import sys 
import pygame
import main_var
import initialisation
import interraction
import boutton
import ModulePersonne
import functions
import fondchargement
import menuchoix
from ModuleGeosciences import Geosciences
from ModuleInfo import Info
from ModuleMath import Math
from joueur import joueur
###################################importation###############################################################
pygame.init()
###################################def variable##############################################################
var_pour_gen = 1
var_lance_jeu = True

tab_hauteur,shape,seed = fondchargement.loadjeu(True)


tab = initialisation.cree_table()
###################################def variable##############################################################

###################################def personnage##############################################################
joueurchoix,var_lance_jeu=menuchoix.menujeu()
screen = pygame.display.set_mode(main_var.size)
color=(63, 34, 4)
screen.fill(color)
background = pygame.image.load("carte_couleur.png")

Joueur1 = joueur()
Joueur2 = joueur()

if joueurchoix[0] == "info":
    Joueur1.createClasse("info")
else:
    Joueur1.createClasse("math")
if joueurchoix[1] == "info":
    Joueur2.createClasse("info")
else:
    Joueur2.createClasse("math")

joueurs=[Joueur1,Joueur2]
functions.init_player(joueurs,tab,tab_hauteur)
###################################def personnage##############################################################

# print(tab)
###################################cree tableau##############################################################            
def creecase(var_pour_gen, posx, posy,tableau,rect,pos_mouse,tab_hauteur,mode_selec):
    case_tabl = tableau[posx][posy]
    x_mouse,y_mouse = pos_mouse
    if case_tabl == "montagne":
        pygame.draw.rect(screen, main_var.montagne, rect, 0)
    elif case_tabl in functions.list_name(Joueur1.getClasse()):
        pygame.draw.rect(screen, main_var.joueur_1, rect, 0)
    elif case_tabl in functions.list_name(Joueur2.getClasse()):
        pygame.draw.rect(screen, main_var.joueur_2, rect, 0)
    elif posx == x_mouse and posy == y_mouse and functions.is_water(pos_mouse,tab_hauteur) and mode_selec: 
        pygame.draw.rect(screen, main_var.souris, rect, 0)
    else:
        pygame.draw.rect(screen, main_var.white, rect, var_pour_gen)
def drawGrid(pos_mouse,tab_hauteur,mode_selec):
    blockSize = 30 #Set the size of the grid block
    for x in range(blockSize):
        for y in range(blockSize):
            rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
            creecase(var_pour_gen,x,y,tab,rect,pos_mouse,tab_hauteur,mode_selec)
            

###################################cree tableau##############################################################


###################################cree boutton##############################################################
boutton_passer_tour=boutton.button((255,1,1),915,715,270,50,"Passer tour")
bouton=pygame.image.load("img/bouton1.png")
bouton2=pygame.image.load("img/bouton2.png")
boutonvarpa=pygame.image.load("img/boutonvarpa.png")
menudroit=pygame.image.load("img/menudroit.png")
bouton = pygame.transform.scale(bouton,(300,98))
bouton2 = pygame.transform.scale(bouton2,(300,98))
boutonvarpa=pygame.transform.scale(boutonvarpa,(300,100))
menudroit=pygame.transform.scale(menudroit,(300,600))
###################################cree boutton##############################################################

pygame.font.init()
###################################variable##################################################################
tour = True #variable qui definie qui peut jouer ici c'est au tour du joueur 1
mode_selec=False
personnage_a_action=0
font1 = pygame.font.Font(None, 70)
varPA = 5
###################################variable##################################################################

###################################lanceur de jeu############################################################
while var_lance_jeu == True:
    screen.blit(boutonvarpa, (900,800))
    screen.blit(menudroit, (900,1))
    boutton_passer_tour.draw(screen, (1,200,0)) #dessine bouton fin de tour
    screen.blit(bouton, (900,700))
    text = font1.render(str(varPA), True, (255, 255, 255))
    screen.blit(text, (975, 840))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            var_lance_jeu = False 
            pygame.quit()
            sys.exit()
            
    #info_jeu#
        position_souris = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:        #quand le joeur clique
            estdeplacer=False
            if varPA > 0:
                tab,mode_selec,personnage_a_action,estdeplacer=interraction.deplacer_combat(tour,tab,mode_selec,personnage_a_action)
            if estdeplacer==True:
                varPA=varPA-1
            pos_grid = functions.get_pos_grid(position_souris)
            h = functions.get_height_case(pos_grid,tab_hauteur)
            if boutton_passer_tour.isOver(position_souris):
                varPA = 5
                tour=boutton.interaction_fin_de_tour(tour)      #programme qui gere l'interaction fin de tour
    #info-jeu#
    if boutton_passer_tour.isOver(position_souris):
        screen.blit(bouton2, (900,700))
    screen.blit(background,(0,0))
    
    drawGrid(functions.get_pos_grid(position_souris),tab_hauteur,mode_selec)
    pygame.display.update()
###################################lanceur de jeu############################################################

