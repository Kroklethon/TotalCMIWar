import pygame
import ModulePersonne
import main_var
import boutton
pygame.init()

def affiche_menu_droite(perso,screen,varPA,tour):
    """
    fonction qui affiche le menu avec tout les information sur un personnage
    entrée:
                    -perso est une instance qui dérive de personne (un math ou un info ou une classe dérivée)
                    -persopos: position de la case ou se tyrouve le perso
                    -test_affichage: boolean qui definie si il y a un personnage a afficher les carac
    sortie: rien
    """
    #info = ["Evan", "Flo", "RomRom", "Théo"]
    #math = ["Aurélien", "Simon", "Julien", "Léa"]
    # bio=["ZIZI","BITE","CACA","CUCU"]

    boutton_passer_tour=boutton.button((255,1,1),915,715,270,50,"Passer tour")
    bouton=pygame.image.load("img/bouton1.png")
    bouton2=pygame.image.load("img/bouton2.png")
    boutonvarpa=pygame.image.load("img/boutonvarpa.png")
    menudroit=pygame.image.load("img/menudroit.png")
    bouton = pygame.transform.scale(bouton,(300,98))
    bouton2 = pygame.transform.scale(bouton2,(300,98))
    boutonvarpa=pygame.transform.scale(boutonvarpa,(300,100))
    menudroit=pygame.transform.scale(menudroit,(300,600))

    # print("Nom="+perso.nom)
    # print("PV="+str(perso.PV))
    # print("PA="+str(perso.PA))
    # print("Infos="+str(perso.information()))

    # TODO: il faut mettre les informations précédentes (voire plus) dans le joli parchemin
	# TODO: les lignes suivantes ne FONCTIONNENT PAS mais cela donne une idée...
    font1 = pygame.font.Font(None, 70)
    screen.blit(boutonvarpa, (900,800))
    screen.blit(menudroit, (900,1))
    boutton_passer_tour.draw(screen, (1,200,0)) #dessine bouton fin de tour
    screen.blit(bouton, (900,700))
    text = font1.render(str(varPA), True, (255, 255, 255))
    screen.blit(text, (975, 840))

    position_souris = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            var_lance_jeu = False 
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if boutton_passer_tour.isOver(position_souris):
                varPA = 5
                tour=boutton.interaction_fin_de_tour(tour) 

    if boutton_passer_tour.isOver(position_souris):
        screen.blit(bouton2, (900,700))
    
    if perso is not None:
        
        text = font1.render(str(perso.nom), True, (255, 255, 255))
        screen.blit(text, (950, 70))
        PV = font1.render("PV = " + str(perso.PV), True, (255, 255, 255))
        screen.blit(PV, (950, 140))
        PA = font1.render("PA = " + str(perso.PA), True, (255, 255, 255))
        screen.blit(PA, (950, 210))
        # infos = font1.render(str(perso.information()), True, (255, 255, 255))
        # screen.blit(infos, (100, 280))

    
	
	
    return varPA ,tour