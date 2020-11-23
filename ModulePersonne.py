import random

XMIN=0
XMAX=29
YMIN=0
YMAX=29
class Personne(object):
    def __init__(self,nom="John Doe",pv=100,pa=5):
        self.posx=random.randint(XMIN, XMAX)
        self.posy=random.randint(YMIN, YMAX)
        self.PV=pv
        self.nom=nom##pas obligé
        self.PA=pa
        self.en_vie = True

    def dansPlateau(x, y):
        return x >= XMIN and x <= XMAX and y >= YMIN and Y <= YMAX
    
    def position(self):
        self.posx=random.randint(XMIN, XMAX)
        self.posy=random.randint(YMIN, YMAX)
    def get_pos(self):
        return (self.posx,self.posy)
    def set_pos(self,posx,posy):
        (self.posx,self.posy)=(posx,posy)
    def position_affichage(self):
        return "Position"+str(p.get_pos())
    def deplacement(self,dx,dy):
        if Personne.dansPlateau(self.posx, self.posy):
            self.posx=self.posx+dx
            self.posy=self.posy+dy
        else:
            return "deplacement impossible"
    def peutattaquer(self,ennemi):
        return abs(self.posx-ennemi.posx)<=1 and abs(self.posy-ennemi.posy)<=1
    def blesse(self, blessure):
        self.PV = max(0,self.PV-blessure)
        if self.PV <= 0:
            self.en_vie = False
    def attaque(self,ennemi):
        if self.peutattaquer(ennemi):
            ennemi.blesse(self.PA)
    def information(self, full=True):
        statut = "( )" if self.en_vie else "(+)"
        if full:
            return statut + self.nom + " (pv=" + str(self.PV) + " pa=" + str(self.PA) + " pos=" + str(self.get_pos()) + ")"
        else:
            return statut + self.nom

if __name__ == "__main__":
    persos = []
    for i in range(1000):
        persos.append(Personne("Perso num " + str(i)))    

    paul = Personne("Paul")
    bob = Personne("Bob")

    print(paul.nom + " est planqué en " + str(paul.get_pos()))
    print(bob.nom + " est caché en " + str(bob.get_pos()))
    for p in persos:
        if p.peutattaquer(bob):
            print("Le perso " + p.information() + " peut attaquer " + bob.information())
        if p.peutattaquer(paul):
            print("Le perso " + p.information() + " peut attaquer " + paul.information())
           
    
    
               
        
                
