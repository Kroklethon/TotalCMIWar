from ModulePersonne import Personne

class Geosciences(Personne):
    def __init__(self,nom="Greta thunberg",pv=70,pa=7,soins=5,magie=100):
        super(Geosciences, self).__init__(nom=nom, pv=pv, pa=pa)
        self.soins = soins
        self.magie= magie
    def information(self):
        return super().information() + " Soins = " + str(self.soins)+" Magie= "+str(self.magie)
    def peutattaquer(self,ennemi):
        return super().peutattaquer(ennemi)
    def draindevie(self,ennemi):
        super().attaque(ennemi)
        self.PV=self.PV+self.soins
    def guerison(self):
        self.PV=self.PV+ 2*self.soins
        
    
if __name__ == "__main__":
    persos = []
    for i in range(10):
       # if i%2 == 0:
          #  persos.append(Personne("Perso num " + str(i)))
        #else:
            persos.append(Geosciences("Geosciences " + str(i), pv=12+i, soins=15-i,magie=90+2*i-1))
    paul = Geosciences("Paul")
    bob = Geosciences("Bob")

    print(paul.nom + " est planqué en " + str(paul.get_pos()))
    print(bob.nom + " est caché en " + str(bob.get_pos()))
    for p in persos:
        if p.peutattaquer(bob):
            print("Le perso " + p.information() + " peut attaquer " + bob.information())
        if p.peutattaquer(paul):
            print("Le perso " + p.information() + " peut attaquer " + paul.information())
           

    for p in persos:
        print(p.information()) 

   
