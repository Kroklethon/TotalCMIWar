import pygame
import functions
import boutton
import joueur
def menujeu():
        stop=True
        joueurs=["info","math"]
        continuer=True
        ecran = pygame.display.set_mode((900, 900))
        background = pygame.image.load("img/fondmenu.jpg")
        background=pygame.transform.scale(background,(900,900))

        #creation vrai bouton
        boutonGj1=boutton.button((255,1,1),500,200,89,89,"z")
        boutonDj1=boutton.button((255,1,1),800,200,89,89,"z")
        boutonGj2=boutton.button((255,1,1),500,500,89,89,"z")
        boutonDj2=boutton.button((255,1,1),800,500,89,89,"z")
        boutonlancer=boutton.button((255,1,1),400,800,89,89,"z")
        #creation vrai bouton

        #bouton des fleche de selection
        imgboutonGj1=pygame.image.load("img/boutonselecgauche.png")
        imgboutonDj1=pygame.image.load("img/boutonselec.png")
        imgboutonGj2=pygame.image.load("img/boutonselecgauche.png")
        imgboutonDj2=pygame.image.load("img/boutonselec.png")

        imgboutonGjover1=pygame.image.load("img/boutonselecovergauche.png")
        imgboutonDjover1=pygame.image.load("img/boutonselecover.png")
        imgboutonGjover2=pygame.image.load("img/boutonselecovergauche.png")
        imgboutonDjover2=pygame.image.load("img/boutonselecover.png")
        #bouton des fleche de selection

        #scale des bouton pour les image
        imgboutonGj1=pygame.transform.scale(imgboutonGj1,(89,89))
        imgboutonDj1=pygame.transform.scale(imgboutonDj1,(89,89))
        imgboutonGj2=pygame.transform.scale(imgboutonGj2,(89,89))
        imgboutonDj2=pygame.transform.scale(imgboutonDj2,(89,89))

        imgboutonGjover1=pygame.transform.scale(imgboutonGjover1,(89,89))
        imgboutonDjover1=pygame.transform.scale(imgboutonDjover1,(89,89))
        imgboutonGjover2=pygame.transform.scale(imgboutonGjover2,(89,89))
        imgboutonDjover2=pygame.transform.scale(imgboutonDjover2,(89,89))
        #scale des bouton pour les image

        #bouton lancer
        lancer=pygame.image.load("img/lancer.png")
        lancerover=pygame.image.load("img/lancerover.png")
        lancer=pygame.transform.scale(lancer,(150,90))
        lancerover=pygame.transform.scale(lancerover,(150,90))
        #bouton lancer

        #image
        info = pygame.image.load("img/infologo.png")
        math = pygame.image.load("img/mathlogo.png")
        #image
        ecran.blit(background,(0,0))
        ecran.blit(info, (620,200))
        ecran.blit(math, (620,500))
        ecran.blit(lancer, (400,800))

        while continuer:
                pygame.display.flip()
                ##################################
                ecran.blit(lancer, (400,800))
                ecran.blit(imgboutonGj1, (500,200))
                ecran.blit(imgboutonDj1, (800,200))
                ecran.blit(imgboutonGj2, (500,500))
                ecran.blit(imgboutonDj2, (800,500))
                ##################################
                for event in pygame.event.get():
                        ###
                        if event.type == pygame.QUIT:
                                continuer = False
                                stop=False
                        ###
                        position_souris = pygame.mouse.get_pos()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                ###
                                if boutonGj1.isOver(position_souris):
                                        joueurs[0]="info"
                                        ecran.blit(info, (620,200))
                                ###
                                if boutonDj1.isOver(position_souris):
                                        joueurs[0]="math"
                                        ecran.blit(math, (620,200))
                                ###
                                if boutonGj2.isOver(position_souris):
                                        joueurs[1]="info"
                                        ecran.blit(info, (620,500))
                                ###
                                if boutonDj2.isOver(position_souris):
                                        joueurs[1]="math"
                                        ecran.blit(math, (620,500))
                                if boutonlancer.isOver(position_souris):
                                		if joueurs[0]!=joueurs[1]:
                                                        continuer=False
                ################################## 
                if boutonGj1.isOver(position_souris):
                        ecran.blit(imgboutonGj1, (500,200))
                if boutonDj1.isOver(position_souris):
                        ecran.blit(imgboutonDj1, (800,200))
                if boutonGj2.isOver(position_souris):
                        ecran.blit(imgboutonGj2, (500,500))
                if boutonDj2.isOver(position_souris):
                        ecran.blit(imgboutonDj2, (800,500))
                if boutonlancer.isOver(position_souris):
                        ecran.blit(lancerover, (400,800))
        pygame.quit()
        return joueurs,stop
