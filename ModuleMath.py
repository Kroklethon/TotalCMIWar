from ModulePersonne import Personne
from random import*

class Math(Personne):
    def __init__(self,nom="Gauss le boss",pv=90,pa=10,equerre=20):
        super(Math, self).__init__(nom=nom, pv=pv, pa=pa)
        self.equerre = equerre
        self.modeAttaque[1] = ["Coup d'équerre", self.Coupdequerre]
        self.modeAttaque[2] = ["Geometre en colere ",self.Geometreencolere]
    def information(self):
        return super().information() + "equerre" + str(self.equerre)
    def Geometreencolere(self,allie):
        if allie.PA<=16:
            allie.PA=allie.PA+3
    def Coupdequerre(self,ennemi):
        print("Attaque equerre")
        n=random()
        if super().peutattaquer(ennemi):
            if n<=(1/2):
                ennemi.blesse(equerre)
                print("Nice shot")
            else :
                print("Try again")
    

if __name__ == "__main__":
    persos = []
    for i in range(100):
        if i%2 == 0:
            persos.append(Personne("Perso num " + str(i)))
        else:
            persos.append(Math("Math num " + str(i), pv=12+i, equerre=20))
    v=Math("josef")
    for p in persos:
        if p.peutattaquer(v):
            print("Le perso " + p.information() + " peut attaquer " + v.information())
