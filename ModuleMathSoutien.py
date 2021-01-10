from ModuleMath import Math
from random import*


class MathSoutien(Math):
    def __init__(self, nom="Euler", pv=105, pa=12, pd=7):
        super(MathSoutien, self).__init__(nom=nom, pv=pv, pa=pa)
        self.pd = pd
        self.modeAttaque[9] = ["Lancer Equerre", self.lancerequerre]
        self.modeAttaque[10] = ["Grenade de math", self.grenadedemath]
    def lancerequerre(self, ennemi):
        if super().peutattaquer(ennemi):
            for i in range(2):  # deux lancers#
                n = random()
                if n < (1/2):
                    ennemi.blesse((1/2)*self.equerre)
                    print("Touché")
                else:
                    print("Echec")

    def grenadedemath(self, ennemi):
        if super().peutattaquer(ennemi):
            ennemi.blesse((3*self.PA))
            self.blesse(self.PA)  # les éclats de la grenade ça fait mal#

    def information(self):
        return super().information() + " <Soutien>"
