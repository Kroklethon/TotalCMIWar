import pygame
import ModulePersonne
import menu_de_droite
def renvoi_selec(mode_selection):
        print('yy')
        print(mode_selection)
        return mode_selection
#deplacer_combat#############################################################################################################################
def deplacer_combat(tour,tableau,mode_selection,personnage_a_action,estEau):
        """
        entrée/sortie:
                entree: boolean -> definie le tour du joueur (qui joue)
        
        fonction de base qui vas géré les déplacement et le combat
        """
        estdeplacer=False
        liste_tour=liste_joueur_jouable(tour)
        pos = pygame.mouse.get_pos()
        perso = selection_sourie(pos,tableau)
        print(mode_selection)
        if mode_selection == True:
                tableau,mode_selection,estdeplacer=interraction_selection(liste_tour,perso,personnage_a_action,tableau,mode_selection,estEau)
        else:
                mode_selection,personnage_a_action=cree_selection(liste_tour,perso,mode_selection)
        return tableau,mode_selection,personnage_a_action,estdeplacer
#interraction_selection###########################################
def interraction_selection(liste_tour,perso,personnage_a_action,tableau,mode_selection,estEau):
        """
        entrée/sortie:
                entree: boolean -> la liste des nom des joueur jouable
                        personnage -> personnage a traiter
                        personnage -> personnage en attente d'instruction
        fonction de base qui vas géré les déplacement et le combat 
        """
        estdeplacer=False
        print("perso cible:")
        print(perso)
        print("zone initiale:")
        print(personnage_a_action)
        if perso[1] - personnage_a_action[1] > -2 and perso[1] - personnage_a_action[1] < 2 and perso[2] - personnage_a_action[2] > -2 and perso[2] - personnage_a_action[2] < 2: #test si il ya pas plus d'une case de dif
            if perso[0] != "vide" and perso[0] != "montagne":       #si on click sur un personnage
                    attaquer(perso,personnage_a_action)             #test attaque
            if perso[0] == "vide" and not estEau:                                #si on click sur une case vide
                    tableau=deplacer(perso,personnage_a_action,tableau)             #test deplacer
                    estdeplacer=True                                            #si on click sur une case infranchissable
        mode_selection = False
        return tableau,mode_selection,estdeplacer
#cree_selection##########################################
def cree_selection(liste_tour,perso,mode_selection):
        """
        entrée/sortie:
                entree: liste -> la liste des nom des joueur jouable
                personnage -> personnage a traiter
                
        fonction qui met en mode selection et instancie quel personnage a utiliser
        """
        personnage_a_action=0
        if perso[0] != "vide" and perso[0] != "montagne":       #si on a bien cliquer sur un personnage
                if perso[0] in liste_tour:                  #si le nom est dans la lsite ( a son tour de jouer)
                        mode_selection=True
                        personnage_a_action=perso
                        """menu_de_droite.affiche_menu_droite(perso)"""
        return mode_selection,personnage_a_action
#liste_joueur_jouable######################################
def liste_joueur_jouable(tour):
        """
        entrée/sortie:
                entree: boolean -> definie le tour du joueur (qui joue)
                sorite: liste -> retourne la liste des nom des joueur jouable
        fonction qui renvois la liste de spersonnage jouable
        """
        liste=[]
        if tour == True:
                liste= ["Evan","Flo","RomRom","Théo"]
        else:
                liste= ["Aurélien","Simon","Julien","Léa"]
        return liste
#deplacer_combat#############################################################################################################################       




#interraction_selection######################################################################################################################

#deplacer######################################################################################################################
def deplacer(tableau_perso,perso,tableau):
        """
        entree/sortie:
                entree: personnage -> personnage a déplacer
                        tableau -> position a aller
        fonction qui gere le déplacement
        """
        tableau[perso[1]][perso[2]]='vide'
        tableau[tableau_perso[1]][tableau_perso[2]]=perso[0]
        # print(perso[0])
        # print(tableau_perso[0])
        # print(tableau[tableau_perso[1]][tableau_perso[2]])

        return tableau
        #copier coller de l'autre fichier
#combatre######################################################################################################################
def attaquer(defenseur,attaquant):
        """
        entree/sortie:
                entree: personnage -> defenseur qui se fait attaquer
                        personnage-> personnage qui attaque
        fonction qui gère le combat 
        """
        

#interraction_selection######################################################################################################################

def selection_sourie(pos,tableau):
        #faire selection sourie
        #copier coller de l'autre fichier
        position=get_pos_grid(pos)
        posx,posy=position
        resultat=['vide',1,1]
        if posx <=30 and posy <= 30:
                resultat=['vide',posx,posy]
                resultat[0]=tableau[posx][posy]
        return resultat

def get_pos_grid(pos):
    posx,posy = pos
    x = posx // 30
    y = posy // 30
    return (x,y)
