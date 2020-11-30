import pygame
class button():
        #class generique de boutton 
                
        #initialisations

        

        #constructeurs
        def __init__(self,couleur,x,y,width,height,text=''):
                '''
                entrée:
                couleur      = type couleur (x,x,x) 
                x,y          = entiers placement du bouton
                width,height =ezntiers bordure du bouton
                text         =text a l'interieur du bouton
                sortie:rien

                constructeur qui sert a crée un boutton
                '''
                self.couleur = couleur
                self.x = x
                self.y = y
                self.width = width
                self.height = height
                self.text = text

        #methodes
        def draw(self,win,outline=None):
                '''
                entree:
                win     = windows = fenetre ou est afficher 
                outline = si on veux crée une outline on place ici
                sortie: rien

                fonction qui dessine un boutton 
                '''
                if outline:
                        pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)

                        pygame.draw.rect(win, self.couleur, (self.x,self.y,self.width,self.height),0)

                if self.text != '':
                        font = pygame.font.SysFont('comicsans', 60)
                        text = font.render(self.text, 1, (0,0,0))
                        win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

        def isOver(self, pos):
                '''
                entree:
                pos  = poisiton en pygame done position d'un element (x,y)
                sortie:
                resultat= boolean qui renvois true si on est bien au dessus du bouton

                fonction qui verifie si l'objet a la position (pos) est sur le boutton
                '''
                resultat = False
                if pos[0] > self.x and pos[0] < self.x + self.width:
                        if pos[1] > self.y and pos[1] < self.y + self.height:
                                resultat = True

                return resultat
        #################################################################
        #ce code a été pris venant d'une vidéo youtube                  #
        #lien: https://www.youtube.com/watch?v=4_9twnEduFA	        #
        #################################################################
def interaction_fin_de_tour(tourjoueur1):
        """
        entree/sortie:
                sortie: boolean -> a quel tour c'est en ce moment
                entrer: boolean-> position du boolean a ce moment
        """
        if tourjoueur1 == True:
                tourjoueur1 = False
        else:
                tourjoueur1 = True
        return tourjoueur1
