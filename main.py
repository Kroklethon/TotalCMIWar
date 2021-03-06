###################################importation###############################################################
import sys 
import os
import pygame
import main_var
import initialisation
import interraction
import boutton
import ModulePersonne
import functions
import fondchargement
import menuchoix
import menu_de_droite
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

###################################imageload##############################################################
evanimg = pygame.image.load('img/evan.png').convert()
evanimg = pygame.transform.scale(evanimg, (30, 30))

theoimg = pygame.image.load('img/theo.png').convert()
theoimg = pygame.transform.scale(theoimg, (30, 30))

romainimg = pygame.image.load('img/romain.png').convert()
romainimg = pygame.transform.scale(romainimg, (30, 30))

floimg = pygame.image.load('img/flo.png').convert()
floimg = pygame.transform.scale(floimg, (30, 30))

aurelienimg = pygame.image.load('img/aurelien.png').convert()
aurelienimg = pygame.transform.scale(aurelienimg, (30, 30))

julienimg = pygame.image.load('img/julien.png').convert()
julienimg = pygame.transform.scale(julienimg, (30, 30))

leaimg = pygame.image.load('img/lea.png').convert()
leaimg = pygame.transform.scale(leaimg, (30, 30))

simonimg = pygame.image.load('img/simon.png').convert()
simonimg = pygame.transform.scale(simonimg, (30, 30))
###################################imageload##############################################################

###################################cree tableau##############################################################            
def creecase(var_pour_gen, posx, posy,tableau,rect,pos_mouse,tab_hauteur,mode_selec):
    case_tabl = tableau[posx][posy]
    x_mouse,y_mouse = pos_mouse
    if case_tabl == "montagne":
        pygame.draw.rect(screen, main_var.montagne, rect, 0)
    elif case_tabl == "Evan":
        screen.blit(evanimg, (posx*30, posy*30)) 
    elif case_tabl == "Flo":
        screen.blit(floimg, (posx*30, posy*30))    
    elif case_tabl == "Théo":
        screen.blit(theoimg, (posx*30, posy*30))
    elif case_tabl == "RomRom":
        screen.blit(romainimg, (posx*30, posy*30))
    elif case_tabl == "Aurélien":
        screen.blit(aurelienimg, (posx*30, posy*30))
    elif case_tabl == "Julien":
        screen.blit(julienimg, (posx*30, posy*30))
    elif case_tabl == "Simon":
        screen.blit(simonimg, (posx*30, posy*30))
    elif case_tabl == "Léa":    
        screen.blit(leaimg, (posx*30, posy*30))
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
pion_selec = None
peut_attaquer = True
victoire = False
###################################variable##################################################################

###################################lanceur de jeu############################################################
while var_lance_jeu == True:
    for i in range(0,len(joueurs)):
        if joueurs[i].nb_perso_morts == 4:
            victoire = True
            gagnant = i
    if not victoire:        
        if tour:
            tour_str = "Joueur 1"
        else:
            tour_str = "Joueur 2"
        screen.fill((191,108,0))
        font1 = pygame.font.Font(None, 70)
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    victoire = True
                    gagnant = 0
                
        #info_jeu#
            position_souris = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_grid = functions.get_pos_grid(position_souris)
                estEau = functions.is_water(pos_grid,tab_hauteur)       #quand le joeur clique
                estdeplacer=False
                print(peut_attaquer)
                if varPA <= 1:
                    peut_attaquer = False
                if varPA > 0:
                    tab,mode_selec,personnage_a_action,estdeplacer,pion_selec ,a_attaque =interraction.deplacer_combat(joueurs,tour,tab,mode_selec,personnage_a_action,estEau,peut_attaquer)
                if estdeplacer==True:
                    varPA=varPA-1
                if a_attaque and peut_attaquer:
                    varPA -= 2
                if boutton_passer_tour.isOver(position_souris):
                    varPA = 5
                    peut_attaquer = True
                    tour=boutton.interaction_fin_de_tour(tour) 
        if boutton_passer_tour.isOver(position_souris):
            screen.blit(bouton2, (900,700)) 
                    #programme qui gere l'interaction fin de tour
        #info-jeu#
        if pion_selec is not None:
            
            text = font1.render(str(pion_selec.nom), True, (255, 255, 255))
            screen.blit(text, (950, 150))
            PV = font1.render("PV = " + str(pion_selec.PV), True, (255, 255, 255))
            screen.blit(PV, (950, 220))
            PA = font1.render("PA = " + str(pion_selec.PA), True, (255, 255, 255))
            screen.blit(PA, (950, 290))
            # infos = font1.render(str(pion_selec.information()), True, (255, 255, 255))
            # screen.blit(infos, (100, 280))
        
        screen.blit(background,(0,0))
        tour_render = font1.render(tour_str, True, (255, 255, 255))
        screen.blit(tour_render, (950, 600))
        # varPA , tour = menu_de_droite.affiche_menu_droite(pion_selec,screen,varPA,tour) 
        drawGrid(functions.get_pos_grid(position_souris),tab_hauteur,mode_selec)
    else:
        font1 = pygame.font.Font(None, 70)
        screen.fill(main_var.black)
        victory = font1.render("Victoire du Joueur " + str(gagnant+1), True, (255, 255, 255))
        screen.blit(victory, (375,450))
        restart = font1.render("Appuyez sur Entrée pour rejouer", True, (255, 255, 255))
        screen.blit(restart, (225,800))
        leave = font1.render("Appuyez sur Echap pour quitter", True, (255, 255, 255))
        screen.blit(leave, (225,850))
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                var_lance_jeu = False 
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    var_lance_jeu = False 
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_RETURN:
                    var_lance_jeu = False 
                    pygame.quit()
                    os.system('python main.py')
                    sys.exit()
                    



    pygame.display.update()
###################################lanceur de jeu############################################################

