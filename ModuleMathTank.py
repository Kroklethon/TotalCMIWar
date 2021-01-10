from ModuleMath import Math
from random import*


class MathTank(Math):
    def __init__(self, nom="Le Fléau", pv=115, pa=15, pd=5):
        super(MathTank, self).__init__(nom=nom, pv=pv, pa=pa)
        self.pd = pd
        self.modeAttaque[11] = ["Charge", self.charge]
        self.modeAttaque[12] = ["Demonstration", self.demonstration]
    def charge(self, ennemi):
        if super().peutattaquer(ennemi):
            if self.pd >= 1:
                ennemi.blesse(3*self.PA)
                self.pd = self.pd-1  # l'attaque l'epuise#
                print("Touché")
            else:
                print("Echec")

    def demonstration(self, ennemi):  # enchainement de coups au corps-à-corps#
        if super().peutattaquer(ennemi):
            for i in range(4):
                n = random()
                if n < (0.6):
                    # j'utilise equerre comme point d'attaque car equerre=20 et(1/4)*equerre est un entier (ps:c'est mieux que les pv soient des nombres entiers)
                    ennemi.blesse((1/4)*self.equerre)
                    print("Touché")
                else:
                    print("Echec")

    def information(self):
        return super().information() + " <Tank>"
