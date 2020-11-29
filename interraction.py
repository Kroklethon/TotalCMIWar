import pygame
import ModulePersonne
mode_selection=False
personnage_a_action=0

#deplacer_combat#############################################################################################################################
def deplacer_combat(tour):
        """
        entrée/sortie:
                entree: boolean -> definie le tour du joueur (qui joue)
        
        fonction de base qui vas géré les déplacement et le combat
        """
        liste_tour=liste_joueur_jouable(tour)
        pos = pygame.mouse.get_pos()
        perso = selection_sourie(pos)
        if mode_selection == True:
                interraction_selection(liste_tour,perso)
        else:
                cree_selection(liste_tour,perso)
#interraction_selection###########################################
def interraction_selection(liste_tour,perso,personnage_a_action):
        """
        entrée/sortie:
                entree: boolean -> la liste des nom des joueur jouable
                        personnage -> personnage a traiter
                        personnage -> personnage en attente d'instruction
        fonction de base qui vas géré les déplacement et le combat 
        """
        if perso[0] != "vide" and perso[0] != "montagne":       #si on click sur un personnage
                attaquer(perso[1],personnage_a_action)             #test attaque
        elif perso[0] == "vide":                                #si on click sur une case vide
                deplacer(perso[1],personnage_a_action)             #test deplacer
                                                                #si on click sur une case infranchissable
        mode_selection = False
#cree_selection##########################################
def cree_selection(liste_tour,perso):
        """
        entrée/sortie:
                entree: liste -> la liste des nom des joueur jouable
                personnage -> personnage a traiter
                
        fonction qui met en mode selection et instancie quel personnage a utiliser
        """
        if perso[0] != "vide" and perso[0] != "montagne":       #si on a bien cliquer sur un personnage
                if perso[1].nom in liste_tour:                  #si le nom est dans la lsite ( a son tour de jouer)
                        mode_selection=True                     
                        personnage_a_action=perso
#liste_joueur_jouable###########################################
def liste_joueur_jouable(tour):
        """
        entrée/sortie:
                entree: boolean -> definie le tour du joueur (qui joue)
                sorite: liste -> retourne la liste des nom des joueur jouable
        fonction qui renvois la liste de spersonnage jouable
        """
        liste=[]
        if tour == True:
                liste=["hugo","flo","evan"]
        else:
                liste=["aurelien","julien","lea"]
        return liste
#deplacer_combat#############################################################################################################################       




#interraction_selection######################################################################################################################

#deplacer######################################################################################################################
def deplacer(tableau,perso):
        """
        entree/sortie:
                entree: personnage -> personnage a déplacer
                        tableau -> position a aller
        fonction qui gere le déplacement
        """
        #copier coller de l'autre fichier
#combatre######################################################################################################################
def attaquer(defenseur,attaquant):
        """
        entree/sortie:
                entree: personnage -> defenseur qui se fait attaquer
                        personnage-> personnage qui attaque
        fonction qui gère le combat 
        """
        #copier coller de l'autre fichier
#interraction_selection######################################################################################################################

def selection_sourie(pos):
        #faire selection sourie
        #copier coller de l'autre fichier
        tablo=["vide",5,5]
        return tablo
