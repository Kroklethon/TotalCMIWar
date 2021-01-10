import pygame
import ModulePersonne
import menu_de_droite


def renvoi_selec(mode_selection):
    print('yy')
    print(mode_selection)
    return mode_selection
#deplacer_combat#############################################################################################################################


def deplacer_combat(joueurs, tour, tableau, mode_selection, personnage_a_action, estEau,peut_attaquer):
    """
    entrée/sortie:
            entree: boolean -> definie le tour du joueur (qui joue)

    fonction de base qui vas géré les déplacement et le combat
    """
    a_attaque = False
    estdeplacer = False
    liste_tour = liste_joueur_jouable(tour,joueurs)
    pos = pygame.mouse.get_pos()
    perso = selection_sourie(pos, tableau)
    print(liste_tour)
    if mode_selection == True:
        tableau, mode_selection, estdeplacer,pion_selec ,a_attaque = interraction_selection(
            joueurs, liste_tour, perso, personnage_a_action, tableau, mode_selection, estEau,peut_attaquer)
    else:
        mode_selection, personnage_a_action, pion_selec = cree_selection(
            joueurs, liste_tour, perso, mode_selection,)
    return tableau, mode_selection, personnage_a_action, estdeplacer ,pion_selec ,a_attaque


def TrouverInstance(joueurs, nom_perso):
    """
    Cette fonction cherche l'instance d'un personnage par son nom,
    Eventuellement cela renvoie None si il n'existe pas (vide ou montagne) 
    """
    # est il dans joueurs[0] ou joueurs[1]
    reponse = None
    joueur = None

    for p in joueurs[0].getClasse():
        if p.nom == nom_perso:
            reponse = p
            joueur = joueurs[0]

        if reponse is not None:
            break

    if reponse is None:
        for p in joueurs[1].getClasse():
            if p.nom == nom_perso:
                reponse = p
                joueur = joueurs[1]

            if reponse is not None:
                break

    return reponse , joueur

#interraction_selection###########################################


def interraction_selection(joueurs, liste_tour, perso, personnage_a_action, tableau, mode_selection, estEau,peut_attaquer):
    """
    entrée/sortie:
            entree: boolean -> la liste des nom des joueur jouable
                    personnage -> personnage a traiter
                    personnage -> personnage en attente d'instruction
    fonction de base qui vas géré les déplacement et le combat 
    """
    a_attaque = False
    estdeplacer = False
    print("perso cible:")
    print(perso)
    print("zone initiale:")
    print(personnage_a_action)

    # instance, en cherchant dans les listes

    pion0, pion0_joueur = TrouverInstance(joueurs, perso[0])
    pion1, pion1_joueur= TrouverInstance(joueurs, personnage_a_action[0])

    if pion0 is not None:
        print(pion0.information())
    else:
        print("Pion0 => None")

    if pion1 is not None:
        print(pion1.information())
    else:
        print("Pion1 => None")

    """
        for p in joueurs[0].getClasse():
                print(p.information())
        for p in joueurs[1].getClasse():
                print(p.information())
        """
    if perso[1] - personnage_a_action[1] > -2 and perso[1] - personnage_a_action[1] < 2 and perso[2] - personnage_a_action[2] > -2 and perso[2] - personnage_a_action[2] < 2:  # test si il ya pas plus d'une case de dif
        if perso[0] != "vide" and perso[0] != "montagne":  # si on click sur un personnage
            # attaquer(perso,personnage_a_action)             #test attaque
            if pion0 != pion1 and peut_attaquer:
                pion0.set_pos(perso[1], perso[2])
                pion1.set_pos(personnage_a_action[1], personnage_a_action[2])
                a_attaque = attaquer(pion0, pion1,tableau,liste_tour ,pion1_joueur)
        if perso[0] == "vide" and not estEau:  # si on click sur une case vide
            tableau = deplacer(perso, personnage_a_action,
                               tableau)  # test deplacer
            estdeplacer = True  # si on click sur une case infranchissable
    mode_selection = False
    return tableau, mode_selection, estdeplacer , pion0, a_attaque
#cree_selection##########################################


def cree_selection(joueurs, liste_tour, perso, mode_selection):
    """
    entrée/sortie:
            entree: liste -> la liste des nom des joueur jouable
            personnage -> personnage a traiter

    fonction qui met en mode selection et instancie quel personnage a utiliser
    """
    personnage_a_action = 0
    pion0 = None
    if perso[0] != "vide" and perso[0] != "montagne":  # si on a bien cliqué sur un personnage
        # si le nom est dans la lsite ( a son tour de jouer)
        if perso[0] in liste_tour:
            mode_selection = True
            personnage_a_action = perso

            pion0,joueur_pion0 = TrouverInstance(joueurs, perso[0])
            if pion0 is not None:
                pion0.set_pos(perso[1], perso[2])
                #menu_de_droite.affiche_menu_droite(pion0)
           
    return mode_selection, personnage_a_action,pion0
#liste_joueur_jouable######################################


def liste_joueur_jouable(tour,joueurs):
    """
    entrée/sortie:
            entree: boolean -> definie le tour du joueur (qui joue)
            sorite: liste -> retourne la liste des nom des joueur jouable
    fonction qui renvois la liste de spersonnage jouable
    """
    if joueurs[0].getType() == "info":
        liste_j1 = ["Evan", "Flo", "RomRom", "Théo"]
        liste_j2 = ["Aurélien", "Simon", "Julien", "Léa"]
    else:
        liste_j1 = ["Aurélien", "Simon", "Julien", "Léa"]
        liste_j2 = ["Evan", "Flo", "RomRom", "Théo"]
    if tour:
        liste = liste_j1
    else : 
        liste = liste_j2
    return liste
#deplacer_combat#############################################################################################################################


#interraction_selection######################################################################################################################

#deplacer######################################################################################################################
def deplacer(tableau_perso, perso, tableau):
    """
    entree/sortie:
            entree: personnage -> personnage a déplacer
                    tableau -> position a aller
    fonction qui gere le déplacement
    """
    tableau[perso[1]][perso[2]] = 'vide'
    tableau[tableau_perso[1]][tableau_perso[2]] = perso[0]
    # print(perso[0])
    # print(tableau_perso[0])
    # print(tableau[tableau_perso[1]][tableau_perso[2]])

    return tableau
    # copier coller de l'autre fichier
#combatre######################################################################################################################


def attaquer(defenseur, attaquant,tableau,liste_tour , joueur_defenseur):
    """
    entree/sortie:
            entree: personnage -> defenseur qui se fait attaquer
                    personnage-> personnage qui attaque
    fonction qui gère le combat 
    """

    """
        TODO: ajouter eventuellement un message d'information qui ressemble à
        """
    if defenseur.nom not in liste_tour:
        # liste des attaques possibles
        listeAttaques = ""
        for m in attaquant.modeAttaque:
            if listeAttaques:
                listeAttaques += ","
            listeAttaques += str(m) + ":" + attaquant.modeAttaque[m][0]

        print(attaquant.nom + " attaque " +
            defenseur.nom + " ===> " + listeAttaques)

        # =================================== la méthode qui effectue l'attaque
        numero_attaque = 0  # actuellement numero_attaque est 0, mais
        # normalement numero_attaque fait partie de la liste qui vient de attaquant.modeAttaque

        attaquant.attaque(defenseur, numero_attaque)
        a_attaque = True
        # ===================================

        """
            TODO: il faut tester l'état du defenseur 
            
            defenseur.PV  (entier) pour les points de vie restants
            defenseur.en_vie (booléen) pour savoir si il est en vie (ou mort !)
            """

        """
            TODO: ajouter eventuellement un message d'information qui ressemble à
            """
        print(defenseur.information())

        if defenseur.en_vie:
            print(defenseur.nom + " a " + str(defenseur.PV) + " points de vie")
        else:
            print(defenseur.nom + " a rejoint ses ancetres")
            tableau[defenseur.posx][defenseur.posy] = 'vide'
            joueur_defenseur.nb_perso_morts -= 1
    else:
        a_attaque = False
        print("Les deux personnages sont dans la même équipe")

    return a_attaque
#interraction_selection######################################################################################################################

def selection_sourie(pos, tableau):
    # faire selection sourie
    # copier coller de l'autre fichier
    position = get_pos_grid(pos)
    posx, posy = position
    resultat = ['vide', 1, 1]
    if posx <= 30 and posy <= 30:
        resultat = ['vide', posx, posy]
        resultat[0] = tableau[posx][posy]
    return resultat


def get_pos_grid(pos):
    posx, posy = pos
    x = posx // 30
    y = posy // 30
    return (x, y)
